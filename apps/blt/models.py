from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from datetime import datetime
import requests



class Address(models.Model):
    """This is the class for the Address object

    Attributes:
        aid: An integer that holds the unique address for the object
        transactions: A list for filled with transaction objects that
        value: Amount of bitcoin Address currently has
        rating: SECRET WEAPON
    """
    aid = models.CharField(max_length=200, db_index=True, unique=True)
    value = models.BigIntegerField(default = 0, db_index = True)
    rating = models.BigIntegerField(default = 0, db_index = True)

    @property
    def amountOfTransactions(self):
        numTotalInteractions = 0
        for s in self.sent:
            numTotalInteractions += 1
        for r in self.received:
            numTotalInteractions +=1
        return numTotalInteractions



    def save(self, **kwargs):
        if not self.pk:
            response = requests.get('https://blockchain.info/q/addressbalance/' + self.aid)
            value = response.json()
            self.value = value
        super(Address, self).save(**kwargs)

class Transaction(models.Model):
    """This is the class for the Transaction object

    Attributes:
        tid: A integer that holds the unique ID for the Transaction
        transaction_date: Datetime object that holds when the transaction occured
        value: An integer that holds the amount of bitcoin that was transfered
    """
    tid = models.CharField(max_length=200, db_index=True)
    value = models.BigIntegerField(default = 0, db_index = True)
    no = models.IntegerField(default = 0, db_index = True)
    transaction_date = models.CharField(max_length=200, db_index=True)

    @property
    def receivers(self):
        return UserReceiveTran.objects.filter(tid = self.tid)

    @property
    def senders(self):
        return UserSendTran.objects.filter(tid = self.tid)

    def save(self, **kwargs):
        if not self.pk:
            response = requests.get('https://blockchain.info/rawtx/' + self.tid)
            transaction_data = response.json()
            for user in transaction_data['inputs']:
                try:
                    curr = user['prev_out']['value']
                    self.value = self.value + curr
                    newAddress, created = Address.objects.get_or_create(aid = user['prev_out']['addr'])
                    newAddress.save()
                    newUserSend = UserSendTran(tid = self.tid, value = curr, user = newAddress)
                    newUserSend.save()
                except:
                    continue
            for user in transaction_data['out']:
                curr = user['value']
                newAddress, created = Address.objects.get_or_create(aid = user['addr'])
                newAddress.save()
                newUserReceive = UserReceiveTran(tid = self.tid, value = curr, user = newAddress)
                newUserReceive.save()

        super(Transaction, self).save(**kwargs)


class UserSendTran(models.Model):
    tid = models.CharField(max_length=200, db_index=True)
    value = models.BigIntegerField(default = 0, db_index = True)
    user = models.ForeignKey(Address, related_name='sent',on_delete=models.CASCADE)

class UserReceiveTran(models.Model):
    tid = models.CharField(max_length=200, db_index=True)
    value = models.BigIntegerField(default = 0, db_index = True)
    user = models.ForeignKey(Address, related_name='received', on_delete=models.CASCADE)

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from datetime import datetime
import requests


class Transaction(models.Model):
    """This is the class for the Transaction object

    Attributes:
        tid: A integer that holds the unique ID for the Transaction
        transaction_date: Datetime object that holds when the transaction occured
        value: An integer that holds the amount of bitcoin that was transfered
    """
    tid = models.CharField(max_length=200, db_index=True, unique=True)
    value = models.IntegerField(default = 0, db_index = True)
    transaction_date = models.DateTimeField(auto_now = False)
    senders = models.ManyToManyField(UserSendTran)
    receivers = models.ManyToManyField(UserReceiveTran)

    def save(self, **kwargs):
        if not self.pk:
            response = requests.get('https://www.blockchain.com/btc/tx/' + self.tid)
            transaction_data = response.json()
            for user in transaction_data['inputs']:
                curr = user['prev_out']['value']
                self.value = self.value + curr
                newAddress, created = Address.objects.get_or_create(aid = user['prev_out']['addr'])
                newAddress.save()
                newUserSend = UserSendTran(tid = self.tid, value = curr, user = newAddress)
                self.senders.add(newUserSend)
            for user in transaction_data['out']:
                curr = user['value']
                newAddress, created = Address.objects.get_or_create(aid = user['addr'])
                newAddress.save()
                newUserReceive = UserReceiveTran(tid = self.tid, value = curr, user = newAddress)
                self.receivers.add(UserReceiveTran)

        super(Transaction, self).save(**kwargs)


class UserSendTran(models.Model):
    tid = models.CharField(max_length=200, db_index=True)
    value = models.IntegerField(default = 0, db_index = True)
    user = models.ForeignKey(Address, related_name='sent')

class UserReceiveTran(models.Model):
    tid = models.CharField(max_length=200, db_index=True)
    value = models.IntegerField(default = 0, db_index = True)
    user = models.ForeignKey(Address, related_name='received')


class Address(models.Model):
    """This is the class for the Address object

    Attributes:
        aid: An integer that holds the unique address for the object
        transactions: A list for filled with transaction objects that
        value: Amount of bitcoin Address currently has
        rating: SECRET WEAPON
    """
    aid = models.CharField(max_length=200, db_index=True, unique=True)
    value = models.IntegerField(default = 0, db_index = True)
    rating = models.IntegerField(default = 1, db_index = True)

    def save(self, **kwards):
        if not self.pk:
            response = requests.get('https://blockchain.info/q/addressbalance/' + self.aid)
            value = response.json()
            self.value = value
        super(Address, self).save(**kwargs)

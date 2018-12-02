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
    value = models.PositiveIntegerField(default = 1, db_index = True)
    transaction_date = models.DateTimeField(auto_now = False)



class Address(models.Model):
    """This is the class for the Address object

    Attributes:
        aid: An integer that holds the unique address for the object
        transactions: A list for filled with transaction objects that
        value: Amount of bitcoin Address currently has
        rating: SECRET WEAPON
    """
    aid = models.CharField(max_length=200, db_index=True, unique=True)
    value = models.PositiveIntegerField(default = 1, db_index = True)
    rating = models.PositiveIntegerField(default = 1, db_index = True)

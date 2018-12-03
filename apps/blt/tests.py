from django.test import TestCase
from apps.blt.models import Transaction, UserSendTran, UserReceiveTran, Address

class TransactionTestCase(TestCase):
    def setUp(self):
        Transaction.objects.create(tid = 'b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da')
        Transaction.objects.create(tid = '57e72ece04874f12f4340973c19ae66d9f34094a0bf0630a0182e4bf88c59dee')

from django.test import TestCase
from datetime import datetime
from apps.blt.models import Transaction, UserSendTran, UserReceiveTran, Address

class TransactionTestCase(TestCase):
    def setUp(self):
        Transaction.objects.create(tid = 'b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da')
        Transaction.objects.create(tid = '57e72ece04874f12f4340973c19ae66d9f34094a0bf0630a0182e4bf88c59dee')
        Transaction.objects.create(tid = 'd873345c1aecbaee3333fbab8a03ad0900cd37bbc0fca1884e211de85f970db9')

    def test_transactions(self):
        t1 = Transaction.objects.get(tid = 'b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da')
        t2 = Transaction.objects.get(tid = 'd873345c1aecbaee3333fbab8a03ad0900cd37bbc0fca1884e211de85f970db9')
        a1 = Address.objects.get(aid = '1FwYmGEjXhMtxpWDpUXwLx7ndLNfFQncKq')
        a2 = Address.objects.get(aid = '178HGmCfR26dSSiFxJQah1U588p2CjgX7f')
        self.assertEqual(a1.value, 0)
        self.assertEqual(a2.value, 0)
        print(t2.senders[0].tid)

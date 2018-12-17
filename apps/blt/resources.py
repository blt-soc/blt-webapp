from import_export import resources
from .models import Transaction

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        skip_unchanged = True
        import_id_fields = ('tid', 'no',)
        fields = ('tid', 'transaction_date', 'value', 'no',)

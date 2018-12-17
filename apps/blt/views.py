from django.shortcuts import render
from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        transaction_resource = TransactionResource()
        dataset = Dataset()
        new_transactions = request.FILES['myfile']

        imported_data = dataset.load(new_transactions.read())
        result = transaction_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            transaction_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

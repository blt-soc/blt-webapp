from django.contrib import admin

from .models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ['aid','value']

admin.site.register(Address, AddressAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['tid', 'value']

admin.site.register(Transaction, TransactionAdmin)

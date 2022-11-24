from django.contrib import admin

from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_display = [
        'client_name', 'client_org', 'number', 'sum', 'date', 'service'
    ]


admin.site.register(Bill, BillAdmin)

import pandas as pd
import datetime as dt

from django.core.exceptions import ValidationError

from .models import Bill


def _get_formatted_date(date):
    try:
        formatted_date = dt.datetime.strptime(
            date, '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        formatted_date = date
    return formatted_date


def _save_bills_in_db(bills):
    Bill.objects.bulk_create(bills, batch_size=100)


def process_file_with_bills(file):
    reader = pd.read_csv(file)
    bills = []
    for _, row in reader.iterrows():
        bill = Bill(
            client_name=row['client_name'],
            client_org=row['client_org'],
            number=row['№'],
            sum=row['sum'],
            date=_get_formatted_date(row['date']),
            service=row['service'],
        )
        try:
            bill.full_clean()
            bills.append(bill)
        except ValidationError:
            continue
    _save_bills_in_db(bills)

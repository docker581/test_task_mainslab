from django.db import models
from django.core.exceptions import ValidationError


def validate_service(service_name):
    if service_name == '-':
        raise ValidationError('Недопустимое значение («-»)')


class Bill(models.Model):
    client_name = models.CharField(
        max_length=127,
        verbose_name='Наименование клиента',
    )
    client_org = models.CharField(
        max_length=255,
        verbose_name='Наименование клиентской организации',
    )
    number = models.IntegerField(verbose_name='Номер счета')
    sum = models.FloatField(verbose_name='Сумма')
    date = models.DateField(verbose_name='Дата')
    service = models.CharField(
        max_length=255,
        verbose_name='Услуга',
        validators=[validate_service],
    )

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'Клиент {self.client_name}, организация {self.client_org}'

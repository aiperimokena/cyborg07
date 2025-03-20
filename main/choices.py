from django.db import models

class OrderStatusEnum(models.TextChoices):
    IN_PROCESSING = ('in_processing', 'In process')
    DENIED = ('denied', 'Denied')
    ACCEPTED = ('accepted', 'Acepted')
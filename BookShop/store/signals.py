import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Book)
def log_book_saved(sender, instance, created, raw, **kwargs):
    if raw:
        return
    if created:
        logger.info(f'Создана книга "{instance.title}" ({instance.pk}, {instance.price})')
    else:
        logger.info(f'Изменена книга "{instance.title}" ({instance.pk})')

@receiver(post_delete, sender=Book)
def log_book_deleted(sender, instance, **kwargs):
    logger.warning(f'Удалена книга "{instance.title}" ({instance.pk})')
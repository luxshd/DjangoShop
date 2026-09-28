from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Создаёт группы Customers и Managers"

    def handle(self, *args, **options):
        customers, _ = Group.objects.get_or_create(name="Customers")
        customers.permissions.set(Permission.objects.filter(codename__in=["view_book", "view_category"]))

        managers, _ = Group.objects.get_or_create(name="Managers")
        managers.permissions.set(Permission.objects.filter(
            codename__in=["view_book", "add_book", "change_book", "can_change_price", "view_category", "add_category"]))
        self.stdout.write(self.style.SUCCESS("Группы созданы"))
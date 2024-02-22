from django.core.management import BaseCommand
from users.models import User, UserRole


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            id=3,
            email='test',
            first_name='test',
            is_staff=False,
            is_superuser=False,

        )
        User.role = UserRole.MODERATOR
        user.set_password('123qwerty')
        user.save()

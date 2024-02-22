from django.core.management import BaseCommand
from users.models import User, Client, UserRole
from materials.models import Materials
from course.models import Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        "удаляем все созданные ранее обьекты"
        Course.objects.all().delete()
        Materials.objects.all().delete()
        User.objects.all().delete()
        Client.objects.all().delete()

        course_for_create = []
        materials_for_create = []
        user_for_create = []
        client_for_create = []

        "создаем курсы"
        courses_list = [
            {
                "name": "English",
                "text": "Very good",
                "pk": 1
            },

            {
                "name": "Magic",
                "text": "Cool",
                "pk": 2
            }
        ]
        for item in courses_list:
            course_for_create.append(Course(**item))
        Course.objects.bulk_create(course_for_create)

        "создаем материалы"
        material_list = [
            {
                "name": "Get intermedia",
                "text": "You can speek english",
                "course_id": 1,
                "pk": 1

            },
            {
                "name": "Leviosa",
                "text": "You can fly",
                "course_id": 2,
                "pk": 2
            }
        ]
        for item in material_list:
            materials_for_create.append(Materials(**item))
        Materials.objects.bulk_create(materials_for_create)

        "создаем пользователя"
        user_list = [
            {
                "email": "Test@mail.ru",
                "FIO": "Ivan Ivanov",
                "password":"123",
                "role": UserRole.MODERATOR,
                "pk": 1
            },
            {
                "email": "New@mail.ru",
                "FIO": "Diana Dorzh",
                "password": "123",
                "pk": 2

            }
        ]
        for item in user_list:
            user_for_create.append(User(**item))
        User.objects.bulk_create(user_for_create)

        "создаем клиента"
        client_list = [
            {
                #"user_id": 1,
                "courses_id": 1,
                "materials_id": 1,
                "day_pay": '2024-02-12',
                "method_pay": 'cash',
                "money": 50000

            },
            {
                #"user_id": 2,
                "courses_id": 2,
                "materials_id": 2,
                "day_pay": '2023-02-12',
                "method_pay": 'card',
                "money": 5000000
            }
        ]

        for item in client_list:
            client_for_create.append(Client(**item))
        Client.objects.bulk_create(client_for_create)

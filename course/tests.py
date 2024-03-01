from rest_framework import status
from rest_framework.test import APITestCase
from config import settings
from config.settings import AUTH_USER_MODEL
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            pk=5
        )

    def test_create_course(self):
        """Тест на создание курса
        (для проверки теста необходимо закомментировать права доступа)"""
        data = {
            "name": "Test",
            "text": "Test",
            "owner_id": self.user.pk

        }
        responce = self.client.post(
            '/course/',
            data=data)
        print(responce.json())

        self.assertEquals(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_course(self):
        """Тестирование вывода списка курсов"""
        responce = self.client.get(
            '/course/'
        )

        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

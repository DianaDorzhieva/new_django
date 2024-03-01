from rest_framework import status
from rest_framework.test import APITestCase
from config import settings
from config.settings import AUTH_USER_MODEL


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_course(self):
        """Тест на создание курса
        (для проверки теста необходимо закомментировать права доступа)"""
        data = {
            "name": "Test",
            "text": "Test"

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

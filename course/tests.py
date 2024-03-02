from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            pk=5
        )
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тест на создание курса"""

        data = {"name": "Test", "text": "Test"}
        responce = self.client.post('/course/', data=data)
        self.assertEquals(responce.status_code, status.HTTP_201_CREATED)
        self.assertEquals(responce.json(),
                          {'id': 1, 'count_materials': 0, 'materials': [], 'name': 'Test',
                           'img': None, 'text': 'Test', 'owner': 5})
        self.assertTrue(Course.objects.all().exists())

    def test_list_course(self):
        """Тестирование вывода списка курсов"""

        responce = self.client.get('/course/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_update_course(self):
        """Тестирование изменения информации курса"""

        course = Course.objects.create(name='Test Course', text='Test text', owner=self.user)
        responce = self.client.patch(f'/course/{course.id}/', {'text': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        """Тестирование удаление курса"""
        self.client.force_authenticate(user=self.user)
        course = Course.objects.create(name='Test Course', text='Test text', owner=self.user)
        responce = self.client.delete(f'/course/{course.id}/')
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            pk=5
        )
        self.client.force_authenticate(user=self.user)

    def test_create_subscript(self):
        """Тест на создание подписки"""
        course = Course.objects.create(name='Test Course', text='Test text', owner=self.user)
        responce = self.client.post('/subscript/', {'course_id': course.id})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)


    def test_delete_subscript(self):
        """Тест на удаление подписки (по сути тоже самое что и на создание)"""
        course = Course.objects.create(name='Test Course', text='Test text', owner=self.user)
        responce = self.client.post('/subscript/', {'course_id': course.id})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

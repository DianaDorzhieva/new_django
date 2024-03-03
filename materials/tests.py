from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Materials
from course.models import Course
from users.models import User


class MaterialsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            pk=5
        )
        self.course = Course.objects.create(
            name='Test Course',
            text='Test text',
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_list_materials(self):
        """Тестирование вывода списка материалов/уроков"""
        responce = self.client.get('/materials/materials/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_create_materials(self):
        """Тестирование создания списка материалов/уроков"""
        data = {"name": "Test", "text": "Test", "course": self.course, "owner": self.user}
        responce = self.client.post('/materials/materials/create/', data=data)
        print(responce)
        self.assertEquals(responce.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Materials.objects.all().exists())

    def test_update_materials(self):
        """Тестирование изменения списка материалов/уроков """
        materials = Materials.objects.create(name="Test", text="Test", course=self.course,
                                             owner=self.user)
        responce = self.client.patch(f'/materials/materials/update/{materials.id}/',
                                     {'text': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_materials(self):
        """Тестирование удаления списка материалов/уроков """
        materials = Materials.objects.create(name="Test", text="Test", course=self.course,
                                             owner=self.user)
        responce = self.client.delete(f'/materials/materials/delete/{materials.id}/')
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)

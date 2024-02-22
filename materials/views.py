from rest_framework import generics
from materials.models import Materials
from materials.serliazers import MaterialsSerializer
from rest_framework.permissions import IsAuthenticated

from users.permission import IsModerator, IsOwner


class MaterialsCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialsSerializer
    #permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]

    def perform_create(self, serializer):
        new_materials = serializer.save()
        new_materials.owner = self.request.user
        new_materials.save()


class MaterialsListAPIView(generics.ListAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]


class MaterialsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]


class MaterialsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]


class MaterialsDestroyAPIView(generics.DestroyAPIView):
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]

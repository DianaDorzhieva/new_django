from rest_framework import viewsets, generics
from materials.models import Materials
from materials.serliazers import MaterialsSerializer


class MaterialsCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialsSerializer


class MaterialsListAPIView(generics.ListAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()


class MaterialsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()


class MaterialsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()


class MaterialsDestroyAPIView(generics.DestroyAPIView):
    queryset = Materials.objects.all()

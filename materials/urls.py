from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import MaterialsCreateAPIView, MaterialsListAPIView, MaterialsRetrieveAPIView, \
    MaterialsUpdateAPIView, MaterialsDestroyAPIView

app_name = MaterialsConfig.name

urlpatterns = [
    path('materials/create/', MaterialsCreateAPIView.as_view(), name='materials_create'),
    path('materials/', MaterialsListAPIView.as_view(), name='materials_list'),
    path('materials/<int:pk>/', MaterialsRetrieveAPIView.as_view(), name='materials_pk'),
    path('materials/update/<int:pk>/', MaterialsUpdateAPIView.as_view(), name='materials_update'),
    path('materials/delete/<int:pk>/', MaterialsDestroyAPIView.as_view(), name='materials_delete'),

]

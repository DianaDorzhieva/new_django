from django.urls import path
from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet, SubscriptionView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(prefix=r'course', viewset=CourseViewSet, basename='courses')

urlpatterns = [
                  path('subscript/', SubscriptionView.as_view(),
                       name='subscript'),

              ] + router.urls

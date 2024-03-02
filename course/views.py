from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course, Subscriptions
from course.paginators import CoursePaginator
from course.serliazers import CourseSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated

from users.permission import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class SubscriptionView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscriptions.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        queryset = Course.objects.all()
        course_item = get_object_or_404(queryset, id=course_id)
        subs_item = Subscriptions.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка на курс удалена'
        else:
            Subscriptions.objects.create(user=user, course=course_item)
            message = 'Подписка на курс добавлена'

        return Response({"message": message})



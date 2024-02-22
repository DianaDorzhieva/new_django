from rest_framework import viewsets
from course.models import Course
from course.serliazers import CourseSerializer
from rest_framework.permissions import IsAuthenticated

from users.permission import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated|~IsModerator|IsOwner]
        elif self.action == 'list':
             self.permission_classes = [IsAuthenticated|IsModerator|IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated|IsModerator|IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated|IsModerator|IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated|IsModerator|IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated|~IsModerator|IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

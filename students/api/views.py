from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from students.api.serializers import SingleStudentSerializer, StudentSerializer, RatingsSerializer
from students.models import Student, Ratings
from students.api.pagination import StudentsRatingsPagination


class StudentsListAPIView(generics.ListAPIView):
    serializer_class = SingleStudentSerializer
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user).order_by("student_first_name")


class StudentsCreateAPIView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user).order_by("student_first_name")

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [ IsAuthenticated ]
    lookup_field = "slug"

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user).order_by("student_first_name")

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


# class StudenViewSet(viewsets.ModelViewSet):
    # serializer_class = StudentSerializer
    # permission_classes = [ IsAuthenticated ]

    # def get_queryset(self):
        # return Student.objects.filter(teacher=self.request.user).order_by("student_first_name")

    # def perform_create(self, serializer):
        # serializer.save(teacher=self.request.user)


# class RatingsCreateAPIView(generics.CreateAPIView):
    # queryset = Ratings.objects.all()
    # serializer_class = RatingsSerializer
    # permission_classes = [ IsAuthenticated ]

    # def perform_create(self, serializer):
        # kwarg_student = self.kwargs.get("student_id")
        # student = get_object_or_404(Student, id=kwarg_student)

        # serializer.save(student=student)


class RatingsListAPIView(generics.ListAPIView):
    serializer_class = RatingsSerializer
    permission_classes = [ IsAuthenticated ]
    pagination_class = StudentsRatingsPagination

    def get_queryset(self):
        return Ratings.objects.filter(student__teacher=self.request.user).order_by("student__student_first_name")


class RatingsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingsSerializer
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        return Ratings.objects.filter(student__teacher=self.request.user)

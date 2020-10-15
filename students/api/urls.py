from django.urls import include, path

from students.api import views as StudentAPIViews

urlpatterns = [
    # path("student/<int:student_id>/ratings/",
         # StudentAPIViews.RatingsCreateAPIView.as_view(),
         # name="create-student-ratings"),

    path("create/student/",
         StudentAPIViews.StudentsCreateAPIView.as_view(),
         name="create-student"),

    path("students/",
         StudentAPIViews.StudentsListAPIView.as_view(),
         name="list-students"),

    path("student/<slug:slug>/",
         StudentAPIViews.StudentRetrieveUpdateDestroyAPIView.as_view(),
         name="student-detail"),

    path("ratings/",
         StudentAPIViews.RatingsListAPIView.as_view(),
         name="list-student-ratings"),

    path("ratings/<int:pk>/",
         StudentAPIViews.RatingsRetrieveUpdateDestroyAPIView.as_view(),
         name="detail-student-ratings"),
]

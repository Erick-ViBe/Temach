from django.urls import path
from teachers import views

urlpatterns = [
    path(
        route='complete-teacher/',
        view=views.complete_profile,
        name='complete_teacher'
    ),
]

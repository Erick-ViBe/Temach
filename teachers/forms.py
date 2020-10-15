from django_registration.forms import RegistrationForm
from teachers.models import Teacher
from django import forms


class TeacherForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = Teacher



class CompleteTeacherForm(forms.Form):
    CHOICES_GRADE = [
        (0, "------"),
        (1, "PRIMERO"),
        (2, "SEGUNDO"),
        (3, "TERCERO"),
        (4, "CUARTO"),
        (5, "QUINTO"),
        (6, "SEXTO"),
    ]
    # grade = forms.IntegerField(choices=CHOICES_GRADE, required=True)
    grade = forms.ChoiceField(choices=CHOICES_GRADE)


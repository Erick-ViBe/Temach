from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from teachers.models import Teacher
from teachers.forms import CompleteTeacherForm


@login_required
def complete_profile(request):
    teacher = request.user

    if request.method == 'POST':
        form = CompleteTeacherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            teacher.grade = data['grade']

            teacher.save()

            url = "/"

            return redirect(url)
    else:
        form = CompleteTeacherForm()

    context = {
        'form': form
    }

    return render(request, 'complete_teacher.html', context)



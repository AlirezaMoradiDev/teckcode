from django.shortcuts import render, redirect
from .models import MyUser, InstructorProfile
from .forms import InstructorForm


def register_instructor(request):
    user = request.user
    instructor = MyUser.objects.get(id=user.id)
    if instructor.is_instructor:
        if request.method == "POST":
            form = InstructorForm(request.POST)
            if form.is_valid():
                pass
        else:
            form = InstructorForm()
    else:
        return redirect('account:not_access')
    return render(request, 'account/register_instructor.html', context={'form': form})


def error_not_access(request):
    return render(request, 'account/not_access.html', context={})
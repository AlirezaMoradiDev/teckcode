from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import MyUser, InstructorProfile
from .forms import InstructorForm



def register_instructor(request):
    user = request.user
    if user.is_authenticated:
        instructor = MyUser.objects.get(id=user.id)
        if InstructorProfile.objects.filter(name__username=request.user.username).exists():
            return redirect('account:profile', username=request.user.username)
        else:
            if instructor.is_instructor:
                if request.method == "POST":
                    form = InstructorForm(request.POST, user=request.user)
                    if form.is_valid():
                        instructor_main = form.save(commit=False)
                        instructor_main.name = request.user
                        instructor_main.save()
                        form.save_m2m()
                        return redirect('account:profile', username=request.user.username)
                else:
                    form = InstructorForm(user=request.user)
            else:
                return redirect('account:not_access')
    else:
        return redirect('account:not_access')
    return render(request, 'account/register_instructor.html', context={'form': form})


class ErrorNotAccessPage(TemplateView):
    template_name = 'account/not_access.html'



def profile_instructor(request, username):
    instructor = InstructorProfile.objects.get(name__username=username)
    return render(request, 'account/profile.html', context={'user': instructor})

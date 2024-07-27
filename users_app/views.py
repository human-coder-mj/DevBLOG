from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisteratonForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisteratonForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request , f"{username} ,Your account has been created for ! , now you can login")
            return redirect("login")
    else:
        form = UserRegisteratonForm()
    return render(request, 'html_templates/register.html' , {"form" : form})


def logout_view(request):
    logout(request)
    return render(request, 'html_templates/logout.html')


@login_required
def profile_view(request):
    return render(request , 'html_templates/profile.html')
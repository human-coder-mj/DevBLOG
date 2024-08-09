from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisteratonForm, UserUpdateForm ,ProfileUpdateForm
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
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request , "Your account has been updated!")
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request , 'html_templates/profile.html' , context)
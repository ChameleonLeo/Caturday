from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html',
                          {'new_user': new_user,
                           'profile': profile})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


@login_required
def get_profile(request):
    profile_detail = get_object_or_404(Profile, user=request.user)
    return render(request, 'accounts/profile.html', {'profile_detail': profile_detail})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return get_profile(request)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'accounts/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

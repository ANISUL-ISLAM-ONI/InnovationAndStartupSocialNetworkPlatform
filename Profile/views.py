
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .forms import EditProfileForm, ProfileForm


# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile.html')
    else:
        return redirect('/')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=request.user.profile)  # request.FILES is show the selected image or file

            if form.is_valid() and profile_form.is_valid():
                user_form = form.save()
                custom_form = profile_form.save(False)
                custom_form.user = user_form
                custom_form.save()
                return redirect('/profile')
        else:
            form = EditProfileForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            args = {}
            args.update(csrf(request))
            args['form'] = form
            args['profile_form'] = profile_form
            return render(request, 'profile/edit_profile.html', args)
    else:
        return redirect('/')
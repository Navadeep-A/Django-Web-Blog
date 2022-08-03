import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterationForm, UserUpdationForm, ProfileUpdationForm 


def register(request):
    if request.method =='POST':
        #   sending postdata to the form 
          form = UserRegisterationForm(request.POST)  
          if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'User {username} Was Successfully Created, You Can Log In Now..!!')
            return redirect('login')
    else:
       form = UserRegisterationForm()
    return render(request,'users/register.html',{'form':form})
  


@login_required
def profile(request):
    if request.method == 'POST':

      user_update = UserUpdationForm(request.POST, instance=request.user )
      profile_update = ProfileUpdationForm(request.POST, request.FILES,instance=request.user.profile)
      if user_update.is_valid() and profile_update.is_valid():
        user_update.save() 
        profile_update.save()
        messages.success(request,f'Your Profile has been updated')
        return redirect('profile')
    else:
      user_update = UserUpdationForm(instance=request.user)
      profile_update = ProfileUpdationForm(instance=request.user.profile)
      

      
    context ={
      'user_update' : user_update,
      'profile_update':profile_update
    }

    return render(request,'users/profile.html',context)





        


                                    





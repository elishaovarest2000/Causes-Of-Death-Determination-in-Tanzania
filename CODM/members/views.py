from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages



def Login_view(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # Redirect to a success page.
            messages.add_message(request, messages.SUCCESS, 'Login successful')
            return redirect(reverse('home'))
        else:
            # Return an 'invalid login' error message.
            messages.add_message(request, messages.ERROR, 'Login Fail')
            return redirect(reverse(''))
    else:
        return render(request, 'registration/login.html')    

# class logout_view(View):
#     def get(self,req,*args, **kwargs):
#         user= req.user

#         if isinstance(user, AnonymousUser):
#            return HttpResponse('You does not login')
#         else:
#             logout(req)
#             return  HttpResponse('You does not login')
       


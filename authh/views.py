from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout





def user_login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        user_password=request.POST['password']

        user=authenticate(username=user_name,password=user_password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message=True
            return render(request,'user_login.html',{'message':message})
        
    return render(request, 'user_login.html')

def user_register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
            return render(request,'user_register.html',{'message':username})

        except:

            user=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username)
            user.set_password(password)
            user.save()
            return redirect('user_login')


    return render(request, 'user_register.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')


def changepass(request):

    if request.method=='POST':
        newpass=request.POST['password']
        user=User.objects.get(username=request.user)
        user.set_password(newpass)
        user.save()
        return redirect('user_login')

    return render(request,'changepass.html')









# def login_(request):
#     if request.method=='POST':
#         username_data=request.POST['username']
#         password_data=request.POST['password']
#         print(username_data,password_data)
#         u=authenticate(username=username_data,password=password_data)
#         print(u)
#         if u is not None:
#             login(request,u)
#             return redirect('home')
#         else:
#             wc=True
#             return render(request,'login_.html',{'wc':wc})
 
    # return render(request,'login_.html')

# def register_(request):
#     if request.method == 'POST':
#         firstname=request.POST['firstname']
#         lastname=request.POST['lastname']
#         email=request.POST['email']
#         username=request.POST['username']
#         password=request.POST['password']
        
#         try:
#             u=User.objects.get(username=username)
#             return render(request,'register_.html',{'u':u})
        
#         except:

#             print(firstname,lastname,email,username,password)
#             u=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username)
#             u.set_password(password)
#             u.save()
#             return redirect('login_')
        
#     return render(request,'register_.html')


# def logout_(request):
#     logout(request)  # erase the session storage

#     return redirect('login_')


# @login_required(login_url='login_')
# def profile(request):

#     return render(request,'profile.html')


# def changepass(request):

#     if request.method=='POST':
#         np=request.POST['password']
#         user=User.objects.get(username=request.user)
#         user.set_password(np)
#         user.save()
#         return redirect('login_')

#     return render(request,'changepass.html')
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def login(request):
    return HttpResponse("User Login.")





# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate, get_user_model

# user = get_user_model()
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})

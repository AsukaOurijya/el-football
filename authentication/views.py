from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
    
    try:
        data = request.POST or json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return JsonResponse({
            "status": False,
            "message": "Username and password are required."
        }, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
    
    try:
        data = request.POST or json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not username or not password1 or not password2:
        return JsonResponse({
            "status": False,
            "message": "Username and both passwords are required."
        }, status=400)

    # Check if the passwords match
    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Passwords do not match."
        }, status=400)
    
    # Check if the username is already taken
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username already exists."
        }, status=400)
    
    # Create the new user
    user = User.objects.create_user(username=username, password=password1)
    user.save()
    
    return JsonResponse({
        "username": user.username,
        "status": True,
        "message": "User created successfully!"
    }, status=201)

@csrf_exempt
def logout(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "User is not logged in."
        }, status=401)

    auth_logout(request)
    return JsonResponse({
        "status": True,
        "message": "Logout successful."
    }, status=200)

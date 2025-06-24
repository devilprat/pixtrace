from django.shortcuts import render, redirect
from django.contrib import messages, auth

from app.helper.validation import validate_post_request
from app.request.LoginRequest import LoginRequest
from app.service import AuthService


@validate_post_request(LoginRequest, 'index.html')
def authentication(request, form=None):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        try:
            AuthService.login(request)
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'index.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')

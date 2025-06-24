from django.contrib import auth


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            raise Exception("Invalid user credentials")
    except Exception as e:
        raise Exception(str(e))

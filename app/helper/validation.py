from functools import wraps
from django.shortcuts import render


def validate_get_request(form_class, template_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'GET':
                form = form_class(request.GET)
                if not form.is_valid():
                    return render(request, template_name, {
                        'errors': form.errors,
                        'old': form.cleaned_data,
                    })
                return view_func(request, form, *args, **kwargs)
            return view_func(request, None, *args, **kwargs)

        return wrapper

    return decorator


def validate_post_request(form_class, template_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'POST':
                form = form_class(request.POST, request.FILES)
                if not form.is_valid():
                    return render(request, template_name, {
                        'errors': form.errors,
                        'old': form.cleaned_data,
                    })
                return view_func(request, form, *args, **kwargs)
            return view_func(request, None, *args, **kwargs)

        return wrapper

    return decorator

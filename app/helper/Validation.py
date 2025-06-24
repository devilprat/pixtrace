from functools import wraps
from django.shortcuts import render


def validate_get_request(form_class, template_name, services=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'GET':
                form = form_class(request.GET)
                if not form.is_valid():
                    context_data = {}
                    if services:
                        for service in services:
                            func = service.get('func')
                            name = service.get('name')
                            params = service.get('params', [])
                            resolved_params = [getattr(request, param) if param == 'user' else None for param in params]
                            context_data[name] = func(*resolved_params)
                    response = {
                        'errors': form.errors,
                        'old': form.cleaned_data,
                        **context_data,
                    }
                    return render(request, template_name, response)
                return view_func(request, form, *args, **kwargs)
            return view_func(request, None, *args, **kwargs)

        return wrapper

    return decorator


def validate_post_request(form_class, template_name, services=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'POST':
                form = form_class(request.POST, request.FILES)
                if not form.is_valid():
                    context_data = {}
                    if services:
                        for service in services:
                            func = service.get('func')
                            name = service.get('name')
                            params = service.get('params', [])
                            resolved_params = [getattr(request, param) if param == 'user' else None for param in params]
                            context_data[name] = func(*resolved_params)
                    response = {
                        'errors': form.errors,
                        'old': form.cleaned_data,
                        **context_data,
                    }
                    return render(request, template_name, response)
                return view_func(request, form, *args, **kwargs)
            return view_func(request, None, *args, **kwargs)

        return wrapper

    return decorator

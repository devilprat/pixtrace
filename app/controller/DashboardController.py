import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from app.helper.Validation import validate_post_request
from app.request import SearchRequest
from app.service import ProductService


@login_required(login_url='index')
@validate_post_request(SearchRequest, 'admin/dashboard.html', [{
    "name": "productList",
    "func": ProductService.getLatest,
    "params": ['user']
}])
def index(request, form=None):
    if request.method == 'POST':
        try:
            ProductService.save(request)
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('dashboard')
    productList = ProductService.getLatest(request.user)
    return render(request, 'admin/dashboard.html', {'productList': productList})

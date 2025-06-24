from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from app.helper.Validation import validate_post_request
from app.request import SearchRequest
from app.service import ProductService


@login_required(login_url='index')
def history(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        historyData = ProductService.getHistory(request.user, page)
        return render(request, 'admin/history.html',
                      historyData)
    return redirect('dashboard')

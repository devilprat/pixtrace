from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.helper.Validation import validate_get_request
from app.request import AnalysisRequest
from app.service import ProductService


@login_required(login_url='index')
def history(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        historyData = ProductService.getHistory(request.user, page)
        return render(request, 'admin/history.html',
                      historyData)
    return redirect('dashboard')


@login_required(login_url='index')
@validate_get_request(AnalysisRequest)
def analysis(request, form=None):
    if request.method == 'GET':
        productId = request.GET['product']
        historyData = ProductService.getById(productId, request.user)
        return render(request, 'admin/analysis.html',
                      historyData)
    return redirect('dashboard')

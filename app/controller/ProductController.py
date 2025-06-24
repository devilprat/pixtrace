import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
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
        current_year = datetime.now().year
        productId = request.GET['product']
        product = ProductService.getById(productId, request.user)
        marketHistory = [e for e in product.product_analysis.all() if int(e.year) <= current_year]
        marketPrediction = [e for e in product.product_analysis.all() if int(e.year) > current_year]
        chart = {
            "sales_history": {
                "labels": [e.year for e in marketHistory],
                "values": [e.sales.replace("$", "") for e in marketHistory],
            },
            "units_sales_history": {
                "labels": [e.year for e in marketHistory],
                "values": [e.units_sold for e in marketHistory],
            },
            "sales_prediction": {
                "labels": [e.year for e in marketPrediction],
                "values": [e.sales.replace("$", "") for e in marketPrediction],
            },
            "units_sales_prediction": {
                "labels": [e.year for e in marketPrediction],
                "values": [e.units_sold for e in marketPrediction],
            }
        }

        return render(request, 'admin/analysis.html',
                      {"product": product, "chart": chart})
    return redirect('dashboard')

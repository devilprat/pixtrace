from django.db import transaction
from app.models import Products, ProductAnalysis, ProductReview, CompetitorAnalysis
from app.service.ChatGptService import analyze


def save(request):
    try:
        with transaction.atomic():
            file = request.FILES['file']
            product = Products.objects.create(
                image=file,
                user=request.user,
            )
            analysis = analyze(product)
            product.name = analysis['name']
            product.category = analysis['category']
            product.save()
            for productAnalysis in analysis['product_analysis']:
                ProductAnalysis.objects.create(
                    year=productAnalysis['year'],
                    units_sold=productAnalysis['units_sold'],
                    average_rate=productAnalysis['average_rate'],
                    sales=productAnalysis['sales'],
                    growth_rate=productAnalysis['growth_rate'],
                    market_trend=productAnalysis['market_trend'],
                    market_position=productAnalysis['market_position'],
                    market_drivers=productAnalysis['market_drivers'],
                    market_challenges=productAnalysis['market_challenges'],
                    remarks=productAnalysis['remarks'],
                    product=product,
                )
            for productReview in analysis['product_review']:
                ProductReview.objects.create(
                    platform=productReview['platform'],
                    link=productReview['link'],
                    author=productReview['author'],
                    caption=productReview['caption'],
                    engagement=productReview['engagement'],
                    product=product
                )
            for competitorAnalysis in analysis['competitor_analysis']:
                CompetitorAnalysis.objects.create(
                    brand=competitorAnalysis['brand'],
                    model=competitorAnalysis['model'],
                    average_price=competitorAnalysis['average_price'],
                    target_audience=competitorAnalysis['target_audience'],
                    key_features=competitorAnalysis['key_features'],
                    strengths=competitorAnalysis['strengths'],
                    weaknesses=competitorAnalysis['weaknesses'],
                    market_share_estimate=competitorAnalysis['market_share_estimate'],
                    positioning=competitorAnalysis['positioning'],
                    product=product
                )
    except Exception as e:
        print(e)
        raise Exception("Failed to analyze the image.Please try again later")

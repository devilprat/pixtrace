from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Prefetch

from app.models import Products, ProductAnalysis, ProductReview, CompetitorAnalysis
from app.service.ChatGptService import analyze, detectImage
from app.service.YoutubeService import getYoutubeReview


def getLatest(user):
    try:
        return Products.objects.filter(user=user).order_by('-created_at')[:10].values()
    except Exception as e:
        print(e)
        return []


def getById(id, user):
    try:
        return (Products.objects.prefetch_related(
            'product_analysis',
            'product_review',
            'competitor_analysis'
        ).get(id=id, user=user))
    except Exception as e:
        print(e)
        print("aa")
        raise Exception(str(e))


def getHistory(user, page):
    try:
        productList = Products.objects.filter(user=user).order_by('-created_at')
        paginator = Paginator(productList, 20)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return {
            'productList': list(page_obj.object_list.values()),
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous()
        }
    except Exception as e:
        print(e)
        return {
            "productList": [],
            "total_pages": 0,
            "current_page": 1,
            "has_next": False,
            "has_previous": False
        }


def save(request):
    try:
        with transaction.atomic():
            file = request.FILES['file']
            product = Products.objects.create(
                image=file,
                user=request.user,
            )
            productDetect = detectImage(product)
            if productDetect is not None:
                product.name = productDetect['name']
                product.category = productDetect['category']
                product.save()
            analysis = analyze(product)
            if analysis is not None:
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
            youtubeReviews = getYoutubeReview(product.name)
            if youtubeReviews is not None:
                for productReview in youtubeReviews:
                    ProductReview.objects.create(
                        platform=productReview['platform'],
                        link=productReview['link'],
                        author=productReview['author'],
                        caption=productReview['caption'],
                        engagement=productReview['engagement'],
                        product=product
                    )
    except Exception as e:
        print(e)
        raise Exception("Failed to analyze the image.Please try again later")

import logging

from app.models import Products


def save(request):
    try:
        file = request.FILES['file']
        Products.objects.create(
            image=file,
            user=request.user,
        )
    except Exception as e:
        logging.error(str(e))
        raise Exception("Failed to analyze the image.Please try again later")

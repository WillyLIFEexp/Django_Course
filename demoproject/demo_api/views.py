from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Book
# Create your views here.

# disable CSRF
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse(
                {
                    'error': True,
                    'msg': 'Reuqired field missing.',
                },
                status = 400
            )
        return JsonResponse(model_to_dict(book), status=201)

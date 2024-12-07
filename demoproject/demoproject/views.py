from django.http import HttpResponse
# Create your views here.
def handler404(request, exception):
    return HttpResponse('404 not found')


from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World. This is the index view of DemoAPP')

def next_url(request):
    return HttpResponse('Hello World. This is the next_url view of DemoAPP')

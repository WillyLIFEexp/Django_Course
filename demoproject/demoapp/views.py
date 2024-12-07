from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World. This is the index view of DemoAPP')

def next_url(request):
    return HttpResponse('Hello World. This is the next_url view of DemoAPP')

def need_para_url(request, category='default_category'):
    """
    Way to write api documents
    ---
    parameters:
      - name: category
        description: The category to filter items by.
        default: default_category
        required: true
        type: string
    """
    return HttpResponse(f"Name: {category} From para method")

def qryview(request):
    """
    Getting parameter through query, which is the data after the ?
    Query Parameters:
        category (str): Filter items by category. Optional.
    Returns:
        HttpResponse: A JSON response containing the list of items.
    """
    cate = request.GET['category']
    return HttpResponse(f"Name: {cate} From query method")
from django.http import HttpResponse


def index(request):
    return HttpResponse("music.")
def music(request):
    return HttpResponse("chain")
def tupac(request):
    return HttpResponse("tupac")
def chain(request):
    return HttpResponse("chain.")
def joel(request):
    return HttpResponse("joel")
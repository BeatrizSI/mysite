from django.http import HttpResponse

def index(request):
    print('Minha primeira view!')
    return HttpResponse('Hello, world!')

def sobre(request):
    print('view - sobre')
    return HttpResponse("Dupla: Antony Raul e Maria Beatriz")
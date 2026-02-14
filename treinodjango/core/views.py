from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'username': 'Miguel William'}
    return render(request, 'core/index.html', context)
    # return HttpResponse('oi')
from django.shortcuts import render
from .models import place
from .models import member


# Create your views here.
def screen(request):
    content = place.objects.all()
    obj = member.objects.all()
    return render(request, 'index.html', {'key': content, 'mem': obj})

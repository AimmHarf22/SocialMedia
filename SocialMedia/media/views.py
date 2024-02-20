from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "media/register.html")


def register():
    return
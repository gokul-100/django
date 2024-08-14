from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseNotFound
from .models import author

authors=author.objects.all()
def index(request):
    auth=author.objects.all()
    # auth=list(auth)
    return render(request,'authors/index.html',{
        'author':auth
    })


def author_details(request , Author):
    try:
        auth=author.objects.get(id=Author)
        print(f'-------------------------------------------{Author}')
       
        responce_data=render(request,'authors/auth_details.html',{
            'authors':auth
        })
        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound("this is not mentioned")


# Create your views here.

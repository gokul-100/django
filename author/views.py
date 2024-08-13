from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseNotFound
from .models import author

authors=author.objects.all()
def index(request):
    auth=author.objects.all()
    # auth=list(auth)
    return render(request,'index.html',{
        'author':auth
    })
    
def author_details(Request,authors):
    try:
        month_text=authors
        # responce_data = render_to_string('month_details/month.html')
        responce_data=render(Request,'month_details/month.html',{
            "text": month_text,
            "title":month_text
        })
        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound("this is not mentioned")
# Create your views here.

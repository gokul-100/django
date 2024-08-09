from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

month_schdule={
    'january':'learning python',
    'Feb':'learning Dsa',
    'march':'learning django',
    'april':'learning git',
    
}
def month_details(Request,month):
    try:
        month_text=month_schdule[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound("this is not mentioned")
    
def month_details_by_number(request,month):
    
    months=list(month_schdule.keys())
    if month > len(months):
        return HttpResponseNotFound("this is not mentioned")

    redirect_month=months[month-1]
    redirect_path=reverse('details',args=[redirect_month])
    # return HttpResponseRedirect('/month/'+redirect_month)
    return HttpResponseRedirect(redirect_path)
# Create your views here.

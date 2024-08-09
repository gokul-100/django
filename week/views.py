from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
week_day={
    'monday':'learning frontend Technologies',
    'tuesday':'learning APi',
    'wednessday':'learning python',
    'thursday':'learning django',
    'friday':'learning sql',
}

def week_details(Request,week):
    try:
        week_text=week_day[week]
        return HttpResponse(week_text)
    except:
        return HttpResponseNotFound("invalid input...")
    
def week_details_number(request,week):
    weeks=list(week_day.keys())
    if week>len(weeks):
        return HttpResponseNotFound("this is invalid input")
    redirect_week=weeks[week-1]
    redirect_path= reverse('week-details',args=[redirect_week])
    return HttpResponseRedirect(redirect_path)
# Create your views here.


from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    
def image_today(request):
    date = dt.date.today()
    images=Image.todays_image()
    return render(request, 'all-image/today-image.html', {"date": date,"images":images})

def past_days_news(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_of_day)

    images = Image.days_image(date)
    return render(request, 'all-image/past-image.html', {"date": date,"images":images})
def search_results(request):
    
    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-image/search.html',{"message":message,"image": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-image/search.html',{"message":message})

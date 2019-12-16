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


def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)


def past_days_news(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    images = Image.days_image(date)
    return render(request, 'all-image/past-image.html', {"date": date,"images":images})
def search_results(request):
    
    if 'images' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-image/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-image/search.html',{"message":message})

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from mainapp.models import *
#def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    
    
#pages

def signup_page(request):
    pass
def login_page(request):
    pass
def search_page(request):
    pass


def dashboard(request):
    return  HttpResponse(request.GET['lol'])


def post_page(request):
    pass
def results_page(request):
    pass

#Actions
def signup_do(request):
    pass
def login_do(request):
    pass
def search_do(request):
    pass

def edit_post(request):
    pass
def cancel_post(request):
    pass

def post_new(request):
    if request.method == 'GET':
        return HttpResponse('invalid request')
    
    
    #New Post
    owner = request.POST['owner']
    car_number = request.POST['car_number']
    total_seats = int(request.POST['total_seats'])
    phone = request.POST['phone']
    fro = request.POST['fro']
    to = request.POST['to']
    
    #yy-mm-dd-hh-mm
    date_time = request.POST['date_time'].split("-")
    date_time = datetime.datetime(year=date_time[0], month=date_time[1], day=date_time[2], hour=date_time[3], minute=date_time[4], second=0, microsecond=0)
    
    
    ac = int(request.POST['ac'])
    men_women = int(request.POST['men_women'])
    available_to = int(request.POST['available_to'])
    
    entry = Post(owner=Rider.objects.get(username=owner), car_number=car_number, total_seats=total_seats, phone=phone, fro=fro, to=to, date_time=date_time, ac=ac,men_women=men_women,available_to=available_to)
    
    entry.save()


def reserve(request):
    pass
def accept(request):
    pass
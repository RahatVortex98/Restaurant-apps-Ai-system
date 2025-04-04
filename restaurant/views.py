from http import HTTPStatus
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .forms import UserLoginForm
from django.contrib.auth import authenticate, login,logout

from .models import Meal,OrderTransaction
from django.http import JsonResponse
from .models import Meal
from django.contrib.auth.decorators import login_required
# Create your views here.


# restaurant/views.py



def error_404_view(request, exception):
    return render(request, '404.html', status=404)




def index(request):
    meals = Meal.objects.all()

    context = {
        'meals':meals,
    }

    return render(request,'restaurant/index.html',context)




@login_required
def order(request, pk=None):
    if pk:
        got_meal = Meal.objects.filter(id=pk).first()  # Fetch the meal safely

        if got_meal and got_meal.stock > 0:
            OrderTransaction.objects.create(
                meal=got_meal, customer=request.user, amount=got_meal.price
            )
            got_meal.stock -= 1
            got_meal.save()

            return redirect('index')  # Redirect to index after successful order

    return HttpResponse(HTTPStatus.BAD_REQUEST) 

@login_required
def order_details(reqeust):
    transactions = OrderTransaction.objects.filter(customer = reqeust.user)

    context ={
        'transactions' : transactions
    }

    return render(reqeust,'restaurant/details.html',context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  
            else:
                form.add_error('username', 'Wrong Username or Password!')
                form.add_error('password', 'Wrong Username or Password!')
    else:
        form = UserLoginForm()  

    return render(request, "restaurant/login.html", {"form": form})


def user_logout(request):
    logout(request)

    return redirect('index')

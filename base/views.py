from django.shortcuts import render , redirect
from . models import Event , Youth
from . forms import YouthForm
import requests
from django.conf import settings
from django.contrib import messages

# Create your views here.


def home(request):
    events = Event.objects.all()


    context = {
        "events": events, 
    }

    return render(request, "base/home.html" , context)

def about(request):
    return render(request, "base/about.html")

def verify_flutterwave_payment(transaction_id):
    url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"
    headers = {
        "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY }",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result["status"] == "success" and result["data"]["status"] == "successful":
            return True
    return False



def register(request):
    if request.method == "POST":
        form = YouthForm(request.POST)
        if form.is_valid():
            transaction_id = request.POST.get("transaction_id")
            if transaction_id and verify_flutterwave_payment(transaction_id):
                form.save()
                messages.success(request, "Payment verified and registration complete!")
                return redirect("base:new_event")
            else:
                messages.error(request, "Payment verification failed. Please try again.")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = YouthForm()

    return render(request, 'base/register.html', {'form': form})
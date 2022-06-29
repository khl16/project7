
from time import gmtime,strftime
from django.shortcuts import render,HttpResponse ,redirect
import random
from datetime import datetime



def index(request):
    if "balance" not in request.session:
        request.session["balance"] = 0


    if "activities" not in request.session:
        request.session["activities"] = []
        
    return render(request, "index.html")

def process_money(request):
    if request.method == "POST":
       location = request.POST["location"]
       if location == "farm" or location == "cave" or location == "house":
            randomValue = random.randint(10,20)
       else:
            randomValue = random.randint(-50,50)
       request.session["activities"].append( {
        "activityName" : location,
        "earnedValue": randomValue,
        "date":strftime("%m %d %Y %H : %M %p",gmtime ())
       })     
       request.session["balance"] += randomValue
       return redirect("/")
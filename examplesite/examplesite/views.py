from django.shortcuts import render 


def index(request):
    return render(request, "index.html")

def submitted(request):
    name = request.POST["name"]
    msg = request.POST["msg"]

    params = {"name" : name, "msg" : msg}
    return render(request, "submitted.html", params)
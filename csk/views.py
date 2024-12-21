from django.shortcuts import render

# Create your views here.
def team(req):
    return render(req,'team.html')
def match(req):
    return render(req,'match.html')
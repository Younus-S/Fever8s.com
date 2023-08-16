from django.shortcuts import render
from django.http import HttpResponse

def friends(request):
    return HttpResponse("01: Friend1<br> 02: Friend2<br> 03: Friend3<br> 04: Friend4<br> 05: Friend5<br> 06: Friend6<br> 07: Friend7<br> 08: Friend8<br> 09: Friend 9<br> 10: Friend 10<br> ")
def friend1(request):
    return HttpResponse("Friend1")
def friend2(request):
    return HttpResponse("Friend2")
def friend3(request):
    return HttpResponse("Friend3")
def friend4(request):
    return HttpResponse("Friend4")
def friend5(request):
    return HttpResponse("Friend5")
def friend6(request):
    return HttpResponse("Friend6")
def friend7(request):
    return HttpResponse("Friend7")
def friend8(request):
    return HttpResponse("Friend8")
def friend9(request):
    return HttpResponse("Friend9")
def friend10(request):
    return HttpResponse("Friend10")

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'kurs/index.html')


def tests(request):
    return render(request, 'kurs/tests.html')


def tasks(request):
    return render(request, 'kurs/tasks.html')


def post_test(request):
    results = 0
    if request.POST.get("quest1") == "2":
        results += 1
    if request.POST.get("quest2") == "3":
        results += 1
    if request.POST.get("quest3") == "1":
        results += 1
    if request.POST.get("quest4") == "3":
        results += 1
    if request.POST.get("quest5") == "2":
        results += 1
    if request.POST.get("quest6") == "3":
        results += 1
    if request.POST.get("quest7") == "2":
        results += 1
    if request.POST.get("quest8") == "2":
        results += 1
    if request.POST.get("quest9") == "2":
        results += 1
    if request.POST.get("quest10") == "1":
        results += 1
    if request.POST.get("quest11") == "2":
        results += 1
    if request.POST.get("quest12") == "2":
        results += 1
    if request.POST.get("quest13") == "3":
        results += 1
    if request.POST.get("quest14") == "2":
        results += 1
    if request.POST.get("quest15") == "1":
        results += 1
    context = {'results': results}
    return render(request, 'kurs/tests.html', context)

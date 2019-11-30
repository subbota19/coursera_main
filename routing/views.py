from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm


def simple_route(request, string=None):
    if request.GET == {} and string is None:
        return HttpResponse(status=200)
    elif request.method != "GET":
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)


def slug_route(request, slug):
    return HttpResponse(slug)


def sum_route(request, number_1, number_2):
    return HttpResponse(number_1 + number_2)


def sum_get_method(request, string=None):
    if string is None:
        try:
            return HttpResponse(eval(request.GET["a"]) + eval(request.GET["b"]))
        except NameError:

            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


def sum_post_method(request):
    if request.method == "POST":
        try:
            return HttpResponse((eval(request.POST['number_1']) + eval(request.POST['number_2'])))
        except NameError:
            return HttpResponse(status=400)

    else:
        return render(request, 'response.html', {'form': NameForm()})

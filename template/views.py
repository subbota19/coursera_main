from django.shortcuts import render


def echo(request):
    if request.META['QUERY_STRING'] == '':
        return render(request, 'meta.html',
                      {'form': request.META['PATH_INFO'].split('/').pop(-1)})

    if request.method == "GET":
        return render(request, 'get.html',
                      {'form': list(request.GET.items())[0][0] + '=' + list(request.GET.items())[0][1]})
    if request.method == "POST":
        return render(request, 'post.html',
                      {'form': list(request.POST.items())[0][0] + '=' + list(request.POST.items())[0][1]})


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })

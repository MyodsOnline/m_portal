from django.shortcuts import render, HttpResponse


def main(request):
    context = {
        'title': 'Mediaportal'
    }
    return render(request, 'base.html', context)

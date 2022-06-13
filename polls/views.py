from django.shortcuts import render, HttpResponse


def main(request):
    context = {
        'title': 'Mediaportal',
        'greeting': 'Welcome %user_name!'
    }
    return render(request, 'index.html', context)

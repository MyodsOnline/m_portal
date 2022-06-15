from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import Content


class ContentView(ListView):
    model = Content
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Mediaportal'
        content['greeting'] = 'Welcome %user_name!'
        return content


def main(request):
    context = {
        'title': 'Mediaportal',
        'greeting': 'Welcome %user_name!'
    }
    return render(request, 'index.html', context)

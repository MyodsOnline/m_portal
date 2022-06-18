from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from pytils.translit import slugify

from .models import Content, Category, Tag
from .forms import ContentForm, ReviewForm


class ContentView(ListView):
    model = Content
    queryset = Content.objects.filter(active=True)
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, *args, object_list=None, **kwargs):
        content = super().get_context_data(*args, **kwargs)
        content['title'] = 'Mediaportal'
        content['greeting'] = 'Welcome %user_name!'
        return content


class CategoryContentView(ListView):
    template_name = 'index.html'
    context_object_name = 'content'
    allow_empty = False

    def get_queryset(self):
        return Content.objects.filter(category__slug=self.kwargs['slug'])


class TagContentView(ListView):
    template_name = 'index.html'
    context_object_name = 'content'
    allow_empty = False

    def get_queryset(self):
        return Content.objects.filter(tag__slug=self.kwargs['slug'])


class SingleContentView(DetailView):
    model = Content
    template_name = 'single.html'
    fields = '__all__'


class CreateContentView(CreateView):
    model = Content
    template_name = 'add.html'
    form_class = ContentForm
    success_url = reverse_lazy('polls')


class AddComment(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        content = Content.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.content = content
            form.save()
        return redirect(content.get_absolute_url())


def main(request):
    context = {
        'title': 'Mediaportal',
        'greeting': 'Welcome %user_name!'
    }
    return render(request, 'index.html', context)

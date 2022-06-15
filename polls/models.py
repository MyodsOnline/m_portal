from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    type = models.CharField(max_length=120, unique=True, verbose_name='Тип контента')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='slug')
    description = models.CharField(max_length=300, verbose_name='Описание типа')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('category_tag', kwargs={'slug': self.slug})


# class Portal_User(User):
#     portal_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь портала')
#     slug = models.SlugField(max_length=30, unique=True)
#
#     def __str__(self):
#         return self.portal_user


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True, verbose_name='Имя тэга')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('content_tag', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Автор контента')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_tag', kwargs={'slug': self.slug})


class Content(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Название')
    tagline = models.CharField(max_length=120, unique=True, verbose_name='Краткое описание')
    file = models.FileField(upload_to='media/%Y/data', verbose_name='Файл', blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')
    image = models.ImageField(upload_to='media/%Y/images', verbose_name='Изображения', blank=True)
    author = models.ForeignKey(Author,
                               on_delete=models.PROTECT,
                               blank=True,
                               related_name='content_author',
                               verbose_name='Автор')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='slug')
    link = models.URLField(blank=True, verbose_name='Ссылка на источник')
    text = models.TextField(verbose_name='Описание контента', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='messages', verbose_name='Тэги записи')
    active = models.BooleanField(default=True, verbose_name='Признак актуальности')

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('content', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

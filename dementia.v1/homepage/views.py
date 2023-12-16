from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse


def home(request, *args, **kwargs):
    return render(request, 'index.html', {})


def error404_view(request, *args, **kwargs):
    return render(request, '404.html', {})


def dementia_view(request, *args, **kwargs):
    return render(request, 'dementia.html', {})


def learning_view(request, *args, **kwargs):
    return render(request, 'learning.html', {})


def technologies_view(request, *args, **kwargs):
    return render(request, 'technologies.html', {})


def research_view(request, *args, **kwargs):
    return render(request, 'news.html', {})


def forum_view(request, *args, **kwargs):
    return render(request, 'forum.html', {})

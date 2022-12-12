from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


def index(request):
    template = loader.get_template('core/index.html')

    context = {
        'forum_title': settings.SITE_CONFIG['general']['ForumTitle'],
        'bg_path': settings.SITE_CONFIG['general']['BackgroundImage']
    }

    resp = HttpResponse(template.render(context, request))
    resp.headers['X-Sanskar-Debug'] = settings.SITE_CONFIG['general']['BackgroundImage']
    return resp

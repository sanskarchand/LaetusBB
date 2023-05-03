from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


def index(request):
    template = loader.get_template('core/index.html')
    # TODO: findout if template.render needed for empty context case
    resp = HttpResponse(template.render({}, request))
    resp.headers['X-Sanskar-Debug'] = settings.SITE_CONFIG['general']['BackgroundImage']
    return resp

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime

# login_requiredのインポート
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Item


# Create your views here.

@login_required
def edit(request, item_id):

    # itemの取得
    item = get_object_or_404(Item, id=item_id)


# ビュー
def hello(request):
    # テンプレートに渡す辞書
    context = {
        'message': 'メッセージ',
        'today': datetime.date.today(),
        'headers': {
            'scheme': request.scheme,
            'path': request.path,
            'method': request.method,
            'content_length': request.META['CONTENT_LENGTH'],
            'http_accept': request.META['HTTP_ACCEPT'],
            'http_accept_language': request.META['HTTP_ACCEPT_LANGUAGE'],
            'user_agent': request.META['HTTP_USER_AGENT'],
            'remote_addr': request.META['REMOTE_ADDR'],
        }
    }

    return TemplateResponse(request, 'item/message.html', context=context)


def extends(request):
    return TemplateResponse(request, 'item/index.html')


def post(request, post_id):
    return HttpResponse('post_idは = {}です'.format(post_id))


def news(request, slug):
    return HttpResponse('slugは = {}です'.format(slug))

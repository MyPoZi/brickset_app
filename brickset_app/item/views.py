from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import datetime

# login_requiredのインポート
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# from brickset_app.item.forms import ItemForm
from .models import Item, WishList


# Create your views here.

@login_required
def edit(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reversed('item_index'))
    else:
        form = ItemForm(instance=item)
        context = {'form': form, 'item': item}
        return TemplateResponse(request, 'item/edit.html', context=context)


@login_required
@require_POST
def delete(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    item.delete()

    return HttpResponseRedirect(reversed('item_index'))


@login_required
def index(request):
    # item一覧を取得し、辞書に格納
    context = {'items': Item.objects.all()}
    return TemplateResponse(request, 'item/list.html', context=context)


@login_required
@require_POST
def add_to_wish_list(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    # wishlistの取得(wishlistが存在しない場合は新規に作成)
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wishlistに該当するitemを追加
    wish_list.items.add(item)

    return HttpResponseRedirect(reversed('wish_list_index'))


@login_required
@require_POST
def delete_from_wish_list(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    # wishlistの取得(wishlistが存在しない場合は新規に作成)
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wishlistから該当するitemを削除
    wish_list.items.remove(item)

    return HttpResponseRedirect(reversed('wish_list_index'))


@login_required
def wish_list_index(request):
    # 欲しいものリストの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # 欲しいものに含まれる全てのitemを取得して、辞書に格納
    context = {'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)


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

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import datetime

# login_requiredのインポート
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import ItemForm
from .models import Item, WishList


# Create your views here.

@login_required
@permission_required('polls.can_vote', raise_exception=True)
def edit(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index'))
    else:
        form = ItemForm(instance=item)

    context = {'form': form, 'item': item}
    return TemplateResponse(request, 'item/edit.html', context=context)


@login_required
@require_POST
@permission_required('polls.can_vote', raise_exception=True)
def delete(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    item.delete()

    return HttpResponseRedirect(reverse('item_index'))


def _get_page(list_, page_no, count=20):
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)
    return page


@login_required
def index(request):
    # item一覧を取得し、辞書に格納
    page = _get_page(Item.objects.all(), request.GET.get('page'))
    context = {'items': page}
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

    return HttpResponseRedirect(reverse('wish_list_index'))


@login_required
@require_POST
def delete_from_wish_list(request, item_id):
    # itemの取得
    item = get_object_or_404(Item, id=item_id)

    # wishlistの取得(wishlistが存在しない場合は新規に作成)
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wishlistから該当するitemを削除
    wish_list.items.remove(item)

    return HttpResponseRedirect(reverse('wish_list_index'))


@login_required
def wish_list_index(request):
    # 欲しいものリストの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # 欲しいものに含まれる全てのitemを取得して、辞書に格納
    context = {'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)

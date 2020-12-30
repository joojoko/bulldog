from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from account.models import Account

from .models import Board
from .forms import BoardForm

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board, 'email': request.session.get('user')})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            account = Account.objects.get(email=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = account
            board.save()

            return redirect('/board_list')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form, 'email': request.session.get('user')})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 10)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards, 'email': request.session.get('user')})

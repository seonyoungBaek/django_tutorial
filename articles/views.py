from django.shortcuts import render, redirect
import random
from .models import Article
#같은 폴더(앱)의 models안의 Article 모델 가져오기

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner (request):
    menus = [{"name":'족발', "price":30000}, {"name":'햄버거', "price":5000}, {"name":'치킨', "price":20000}, {"name":'초밥', "price":15000}]
    #보통 이렇게 딕셔너리 안에 리스트로 담겨있는 경우가 많다.
    pick = random.choice(menus)
    #pick은 menus중에서 하나를 랜덤으로 골라주는 것. 고른 값이 pick 안에 들어감.
    articles = Article.objects.order_by('-pk')
    #Article모델을 pk(등록 아이디)의 역순으로 불러오기(장고 orm문법)
    context = {
        'pick':pick,
        'menus':menus,
        #menus안에 있는 것들을 for문으로 돌려주기 위해 contex안에 menus를 담아서 html에 넘겨준다. 
        'articles':articles,
    }
    #views.py에서 html로 데이터를 넘겨주기 위해 context라는 것을 사용함. 딕셔너리 형태로 만들고, 그 안에 키값:밸류값을 넣어준다.
    return render(request, 'dinner.html', context)
    #render에도 request, html, context를 실어줘야 한다.

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    #request로 받은 것 중 post메소드 일때, 그 데이터 안에서 content라는 이름만 받아오기. (html에 name=content인 데이터 있음)
    title = request.POST.get('title')
    article = Article(title = title, content = content)
    # article이란 인스턴스 안에 위에 임포트했던 Article모델의 content, title을 받아온다.
    article.save()
    # Article 모델에 대한 인스턴스이기 때문에 특별한 기능들이 제공된다. 그 중 하나가 save이며, 인스턴스의 내용을 db에 알아서 저장되도록 한다.

    return redirect('articles:detail', article.pk)
    #저장까지 모두 끝난 후, detail페이지로 옮겨가도록 한다.


def detail(request, pk):
#pk를 받아옴으로써 url에 입력된 숫자를 가져와 db에 저장된 아이디를 조회함.
    article = Article.objects.get(pk=pk)
    #article이란 변수 안에 Article모델의 pk를 가져옴.(request해온 pk와 일치하는)
    context = {
        'article' : article
    }
    return render (request, 'detail.html', context)
    #첫번째 인자 request, 두번째 template, 세번째 article이 담긴 context를 실어서 보내준다.

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    #detail과 동일하게 article db에서 불러오기

    if request.method == 'POST':
    #요청 방식이 post일 때만
        article.delete()
        #Article모델 안에 정의된 delete를 실행한다.
    return redirect('articles:dinner')
    #지우고 나면 리스트 페이지로 돌아가도록

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    #edit도 delete처럼 어느 한 글을 쏙 골라서 수정하는 것이기 때문에 게시글의 pk를 받아와야함.
    context = {
        'article' : article,
    }
    return render(request, 'edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    #(파이썬에서)article의 타이틀을, post요청된 edit.html에서의 name = title로 바꾼다.
    article.content = request.POST.get('content')
    article.save()
    #db에 수정된 정보를 저장한다.
    return redirect('articles:detail', article.pk)
    
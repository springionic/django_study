from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request, 'one.html')

def two(request):
    # 用来存放向模板中传输的数据
    ct = dict()
    ct['name'] = '王晓静'
    ct['name2'] = '李晓静'
    ct['name3'] = '张晓静'
    return render(request, 'two.html', context=ct)

def three(request):
    ct = dict()
    ct['score'] = [66, 77, 88, 86, 94, 55]
    return render(request, 'three.html', context=ct)

def four(request):
    ct = dict()
    ct['name'] = '王晓静'
    return render(request, 'four.html', context=ct)

def five(request):
    return render(request, 'five.html')

def five_post(request):
    print(request.POST)
    return render(request, 'one.html')

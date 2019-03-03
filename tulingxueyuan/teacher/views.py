from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

# 视图函数需要一个参数，类型应该是HTTPRequest
def do_normalmap(request):
    return HttpResponse('This is normalmap')

def withparam(request, year, month):
    return HttpResponse('This is with param {0}, {1}'.format(year, month))

def do_app(request):
    return HttpResponse('这是个子路由！')

def do_param2(request, pn):
    return HttpResponse('Page number is {0}!'.format(pn))

def extremParam(r, name):
    return HttpResponse('My nmae is {0}'.format(name))

def revParse(request):
    return HttpResponse('Your requested url is {0}'.format(reverse('askname')))

#coding:utf-8
#
import sqlite3
import binascii
import struct
import time
import datetime
import memcache
import json
import simplejson
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临!")

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def symconfig(request):
    if request.method == 'GET':
        return HttpResponse('hello')
        pass
    elif request.method == 'POST':
        req = json.loads(request.body.decode("utf-8"))
        rttime = str(datetime.datetime.fromtimestamp(int(time.time())))
        print(rttime, '||', len(req))
        print(list(req['rts'][0].keys()))
        zz = req['rts'][0]
        for key, value in zz.items():
            print("\"%s\":\"%s\"" % (key, value))
        fl = open('list.txt', 'w')
        fl.write(req['rts'][0])
        fl.write("\n")
        fl.close()

        return HttpResponse('200')
        pass
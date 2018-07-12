# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
import datetime
from dateutil import tz


def successResponse(message='Successed', data={}):
    result = {}
    result['message'] = message
    result['data'] = data
    return HttpResponse(json.dumps(result))

def datetime2Normal(nowtime):
    return nowtime.strftime("%Y-%m-%d %H:%M:%S")


def utcnow():
    """  A tz-aware now  """
    return datetime.datetime.utcnow().replace(tzinfo=tz.tzutc())

from __future__ import unicode_literals
from django.http import HttpResponse
from django.db import connection
import json
import datetime
import collections
from decimal import Decimal


def json_custom_parser(obj):
    """
        A custom json parser to handle json.dumps calls properly for Decimal and Datetime data types.
    """
    if isinstance(obj, Decimal):
        return str(obj)
    elif not isinstance(obj, str) and isinstance(obj, collections.Iterable):
        return list(obj)
    elif isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19  # 'YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM'.find('.')
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)


def jsonify(obj):
    return json.dumps(obj, default=json_custom_parser)


def json_response(data, status=200, headers={}):
    hr = HttpResponse(
        json.dumps(data, default=json_custom_parser),
        content_type='application/json',
        status=status)
    for k, v in headers.items():
        hr[k] = v

    return hr


def fetchall(query, params=None):
    "Returns all rows from a cursor"
    if params is None:
        params = ()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cursor.close()


def execute(query, params=None, conn=connection):
    "Executes a query"
    if params is None:
        params = ()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
    finally:
        cursor.close()


def dictfetchall(query, params=None, conn=connection):
    """Returns all rows from a cursor as a dict"""
    if params is None:
        params = ()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        keys = [col[0] for col in cursor.description]
        x = [
            dict(zip(keys, row))
            for row in cursor.fetchall()
        ]
        return x
    finally:
        cursor.close()

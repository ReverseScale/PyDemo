
import json
import django
def get_an_apple(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return django.http(json.dumps(resp), content_type="application/json")
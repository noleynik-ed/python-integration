import os

import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view

from integration.logging_config import logger


@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


@api_view(['POST'])
def post_payload(request):
    payload = request.data
    logger.info("Payload received:")
    logger.info(payload)
    outgoing_url = os.getenv('OUTGOING_URL')
    resp = requests.post(outgoing_url, data=payload)
    return HttpResponse("Payload posted. Response code: " + str(resp.status_code))

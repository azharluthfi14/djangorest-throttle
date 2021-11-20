from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .throttles import LimitThrottle, RateThrottle, VeryLimitedThrottle


class ExampleLimitedView(APIView):
    throttle_class = [LimitThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'Your request was permitted'
        }

        return Response(content)


class ExampleVeryLimitedView(APIView):
    throttle_class = [VeryLimitedThrottle]

    def get(self, request, *args, **kwargs):
        content = {
            'status': 'Hello world'
        }

        return Response(content)

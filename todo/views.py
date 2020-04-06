import os
import logging
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class FrontendAppView(View):
    indexFilePath = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')

    def get(self, request):
        try:
            with open(self.indexFilePath) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead after
                running `yarn start` on the frontend/ directory
                """,
                status=501,
            )

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
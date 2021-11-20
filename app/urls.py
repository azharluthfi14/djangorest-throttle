from django.urls import path
from .views import (
    ExampleLimitedView,
    ExampleVeryLimitedView
)

urlpatterns = [
    path('', ExampleLimitedView.as_view()),
    path('limited/', ExampleVeryLimitedView.as_view()),
]

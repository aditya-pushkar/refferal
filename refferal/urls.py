from django.contrib import admin
from django.urls import path
from .views import main_view, signup_view
from profile_app.views import my_recommendation_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main-view'),
    path('signip/', signup_view, name='signup-view'),
    path('my/recs/', my_recommendation_view, name='rec-view'),
    path('<str:ref_code>/', main_view, name='main-view'),
]

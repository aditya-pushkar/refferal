from django.shortcuts import render
from .models import Profile

# Create your views here.


def my_recommendation_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profiles()
    context = {
        'my_recs': my_recs
    }
    return render(request, 'profile/main.html', context)
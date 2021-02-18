from api.models import Profile
from django.utils import timezone


class LastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
            profile.last_request = timezone.now()
            profile.save()
        return response

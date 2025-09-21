from zoneinfo import ZoneInfo
from django.utils import timezone

class UserTimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = None
        
        if request.user.is_authenticated:
            if hasattr(request.user, "profile"):
                tzname = request.user.profile.timezone

        if not tzname:
            tzname = request.session.get("django_timezone")

        if tzname:
            try:
                timezone.activate(ZoneInfo(tzname))
            except Exception:
                timezone.deactivate()
        else:
            timezone.deactivate()

        return self.get_response(request)
from django.utils import timezone
from testing.models import Snippet

class SnippetService(Snippet):
    def latest_snippets(days, hour, minuts):
        diffDateTime = timezone.now() - timezone.timedelta(days=days)
        print(f"比較日時:{diffDateTime}")
        if days == 0:
            return None
        return Snippet.objects.filter(created_at__gt=diffDateTime).all()

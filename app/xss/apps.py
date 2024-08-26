from django.apps import AppConfig
from django.http import HttpResponse

class XssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xss'

_form_html = """<form method="get">
<input type="text" name="q" placeholder="search" value="">
<button type="submit">search</button>
</form>
"""

def xss_view(request):
    if 'q' in request.GET:
        return HttpResponse(f"searched: {escape(request.GET['q'])}")
    else:
        return HttpResponse(_form_html)

def escape(s, quote=True):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
        s = s.replace('\'', "&#x27;")
        
    return s

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from testing.form import SnippetForm

UserModel = get_user_model()

@login_required
def new_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return HttpResponse("created", status=201)
        else:
            return HttpResponse("bad request", status=400)
    else:
        form = SnippetForm()
    return render(request, "testing/new_snippet.html", {"form": form})

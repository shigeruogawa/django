from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from testing.models import Snippet
from django.contrib.auth.decorators import login_required
from snippets.forms import SnippetForm

# def top(request):
#     return render(request, "snippets/top.html")

def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html",context)

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html',
                  {'snippet': snippet})

@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail,snippet_id=snippet.pk)
    else:
        form = SnippetForm()
            
    return render(request, "snippets/snippet_new.html", {'form': form})

@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("他のユーザのスニペットは編集することができません。")
    
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html',{'form': form})
        

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import person
from .forms import personForm

def home(request):
    context = {'form': personForm(request.POST or None, request.FILES or None)}
    if context['form'].is_valid():
        context['form'].save()
        return HttpResponseRedirect(reverse('list'))
    return render(request, "index.html", context)

def list_view(request):
    query = request.GET.get("query", "")
    context = {}
    if query:
        dataset = person.objects.filter(firstname__icontains=query) | person.objects.filter(lastname__icontains=query)
        if dataset.exists():
            context['dataset'] = dataset
        else:
            # No results found, set 'no_results' flag to True
            context['no_results'] = True
    else:
        context['dataset'] = person.objects.all()
    return render(request, "list.html", context)


def detail_view(request, id):
    context = {'data': get_object_or_404(person, id=id)}
    return render(request, "detail.html", context)

def update_view(request, id):
    obj = get_object_or_404(person, id=id)
    form = personForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detail_view', args=(id,)))
    return render(request, "update.html", {'form': form})

def delete_view(request, id):
    obj = get_object_or_404(person, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('list'))
    return render(request, "delete.html", {'data': obj})




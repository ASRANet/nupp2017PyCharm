from django.shortcuts import render
from django.http import HttpResponse
from register.models import User
from register.forms import CategoryForm


def index(request):

    return render(request, 'register/index.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'register/add_category.html', {'form': form})

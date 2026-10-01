from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import LostAndFoundItem


def landing(request):
    return render(request, 'Inv_Items/landing.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def Home(request):
    items = LostAndFoundItem.objects.all()
    return render(request, 'home.html', {'items': items})


@login_required
def AddItem(request):
    if request.method == 'POST':
        LostAndFoundItem.objects.create(
            item_name=request.POST.get('item_name'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            location=request.POST.get('location'),
            status=request.POST.get('status'),
            contact_information=request.POST.get('contact_information'),
        )
        return redirect('home')

    return render(request, 'add_item.html')


@login_required
def EditItem(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Only Lost and Found staff can edit items.')
        return redirect('home')

    item = get_object_or_404(LostAndFoundItem, pk=pk)

    if request.method == 'POST':
        item.item_name = request.POST.get('item_name')
        item.description = request.POST.get('description')
        item.category = request.POST.get('category')
        item.location = request.POST.get('location')
        item.status = request.POST.get('status')
        item.contact_information = request.POST.get('contact_information')
        item.save()
        return redirect('home')

    return render(request, 'edit_item.html', {'item': item})


@login_required
def DeleteItem(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Only Lost and Found staff can delete items.')
        return redirect('home')

    item = get_object_or_404(LostAndFoundItem, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('home')
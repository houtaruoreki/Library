from django.shortcuts import render, redirect
from .models import Reader
from .forms import UserForm
from django.urls import reverse
from django.db import IntegrityError


def collect_user_info(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            try:
                Reader.objects.create(firstname=first_name, lastname=last_name, email=email)
                return redirect(reverse('Book:index'))
            except IntegrityError:
                error_message = "This email address is already registered."
                form.add_error('email', error_message)
    else:
        form = UserForm()
    return render(request, 'collect_user_info.html', {'form': form})

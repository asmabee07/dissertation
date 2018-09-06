from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, CompleteProfileForm
from .models import FoodItem, CompleteProfile


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


@login_required
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def complete_profile(request, pk=None):
    instance = get_object_or_404(CompleteProfile, pk=pk) if pk else None
    cyp = CompleteProfileForm(request.POST, instance=instance)
    if request.POST:
        if cyp.is_valid():
            complete_profile = cyp.save(commit=False)
            complete_profile.user = request.user
            complete_profile.save()
    return render(request, 'complete_profile.html', {'cyp': cyp})


'''
def bmi_measurement(request):
    bmi = BmiMeasurementForm(request.POST)
    if bmi.is_valid():
        bmi.save()
    return render(request, 'bmi.html', {'bmi': bmi})

'''


@login_required
def dietary_intake(request):
    food_items = FoodItem.objects.all()
    context = {
        'food_items': food_items,
    }
    return render(request, 'dietary_intake.html', context)


def sample_chart(request):
    food_nutrients = FoodItem.objects.filter(protein='9 g', total_Carbs='16 g', total_Fat='21 g', sugars='1 g')
    food_items = FoodItem.objects.filter(food_name='Mutter Paneer')
    context = {
        'food_nutrients': food_nutrients,
        'food_items': food_items,
    }
    return render(request, 'sample_chart.html', context)


def highcharts(request):

    return render(request, 'highcharts.html')


def highcharts_demo(request):
    return render(request, 'highcharts_demo.html')
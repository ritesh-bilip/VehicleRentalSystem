from django.shortcuts import render, redirect
from .models import Booking, Car, Bike, Truck, Customer, RentalRecord, Owner,User,Profile
from .serializers import Carserializer, Bikeserializer, Truckserializer, Customerserializer, rentalRecordserializer, OwnerSerializer
from rest_framework import viewsets
from .forms import SignUpForm, LoginForm, CarForm,ProfileForm,BikeForm,TruckForm,BookingForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# ------------------ API ViewSets ------------------
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = Carserializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = Bikeserializer

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = Truckserializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer

class rentalRecordViewSet(viewsets.ModelViewSet):
    queryset = RentalRecord.objects.all()
    serializer_class = rentalRecordserializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# ------------------ Pages ------------------
def home(request):
    return render(request, 'rentals/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ✅ use password1
            auth_user = authenticate(
                request,
                email=user.email,
                password=form.cleaned_data['password']
            )
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Account created successfully")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed")
    else:
        form = SignUpForm()
    return render(request, 'rentals/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successfully")
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'rentals/login.html', {'form': form})

@login_required
def addCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            rentals_car= authenticate
            messages.success(request, "Car added successfully")
            return redirect('vehicle_list')
    else:
        form = CarForm()
    cars = Car.objects.all()
    return render(request, 'rentals/carFrom.html', {'form': form, 'cars': cars})

def logout_user(request):
    logout(request)
    return redirect('home')
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'rentals/car_list.html', {'cars': cars})
@login_required
def add_owner_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= request.user
            profile.save()
            messages.success(request,"Profile created successfully")
            return redirect('dashboard')
    else:
        form=ProfileForm()
    return render(request,'rentals/add_profile.html',{'form':form})
@login_required
def dashboard(request):
    profile= Profile.objects.filter(user=request.user).first()
    return render(request,'rentals/owner_dasboard.html',{'profile':profile})
@login_required
def add_bike(request):
    if request.method=='POST':
        form=BikeForm(request.POST)
        if form.is_valid():
            form.save()
            rentals_bike= authenticate
            messages.success(request,"Bike added successfully")
            return redirect('vehicle_list')
    else:
        form=BikeForm()
    bikes=Bike.objects.all()
    return render(request,'rentals/bike_form.html',{'form':form,'bikes':bikes})

@login_required
def add_truck(request):
    if request.method=='POST':
        form=TruckForm(request.POST)
        if form.is_valid():
            form.save()
            rentals_truck= authenticate
            messages.success(request,"Truck added successfully")
            return redirect('vehicle_list')
    else:
        form=TruckForm()
    trucks=Truck.objects.all()
    return render(request,'rentals/truck_form.html',{'form':form,'trucks':trucks})
def vehicle_list(request):
    vehicle_type = request.GET.get('type', 'car')  # default to car
    cars = Car.objects.all()
    bikes = Bike.objects.all()
    trucks = Truck.objects.all()

    context = {
        'vehicle_type': vehicle_type,
        'cars': cars,
        'bikes': bikes,
        'trucks': trucks,
    }
    return render(request, 'rentals/vehicle_list.html', context)
def book_ride(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('user_dashboard')
    else:
        form = BookingForm()
    return render(request, 'rentals/book_ride.html', {'form': form})

def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'rentals/user_dashboard.html', {'bookings': bookings})
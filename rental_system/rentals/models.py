from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
# -------------------
# Rental System Models
# -------------------

class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rental_day = models.PositiveBigIntegerField()
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def calculate_rent(self):
        return self.rental_day * self.rent_per_day

class Car(Vehicle):
    owner_name = models.CharField(max_length=100, null=True, blank=True)# simple text field
    car_name = models.CharField(max_length=100)
    seating_capacity = models.PositiveIntegerField()
    car_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.car_name} - {self.car_number} (Owner: {self.owner_name})"

class Bike(Vehicle):
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    bike_name = models.CharField(max_length=100)
    bike_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.bike_name} - {self.bike_number}"


class Truck(Vehicle):
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    truck_name = models.CharField(max_length=100)
    load_capacity = models.PositiveIntegerField()
    truck_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.truck_name} - {self.truck_number}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()


class RentalRecord(models.Model):   # ✅ Capitalized class name
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    vehicle_id = models.PositiveIntegerField()
    renter_name = models.CharField(max_length=100)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    total_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        rental_days = (self.rent_end_date - self.rent_start_date).days
        if self.vehicle_type == 'Car':
            vehicle = Car.objects.get(id=self.vehicle_id)
        elif self.vehicle_type == 'Bike':
            vehicle = Bike.objects.get(id=self.vehicle_id)
        elif self.vehicle_type == 'Truck':
            vehicle = Truck.objects.get(id=self.vehicle_id)
        else:
            raise ValueError("Invalid vehicle type")

        self.total_rent = rental_days * vehicle.rent_per_day
        super().save(*args, **kwargs)


# -------------------
# Custom User Model
# -------------------

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError("Must enter email")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password):
        user = self.create_user(email, name, phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    
#!------- Owner peofile add------
class Profile(models.Model):
    name = models.CharField(max_length=100,null=True )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner_profile")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
   


    def __str__(self):
        return f"{self.user.username}'s Profile"
    
# -------------------
# user model view
# -------------------
class Booking(models.Model):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    preference = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.pickup_location} → {self.destination}"
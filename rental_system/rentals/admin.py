from django.contrib import admin
from .models import Owner, Car, Bike, Truck, Customer, RentalRecord, User

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Bike)
admin.site.register(Truck)
admin.site.register(Customer)
admin.site.register(RentalRecord)   # ✅ Capitalized
admin.site.register(User)
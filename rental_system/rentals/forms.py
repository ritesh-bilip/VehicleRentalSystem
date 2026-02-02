from django import forms
from django.contrib.auth import get_user_model
from .models import Car,Profile,Bike,Truck,Booking
User = get_user_model()

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','password']  # ✅ use 'fields'

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # ✅ use cleaned_data
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
class CarForm(forms.ModelForm):
    class Meta:
        model= Car
        fields='__all__'
class BikeForm(forms.ModelForm):
    class Meta:
        model= Bike
        fields='__all__'
class TruckForm(forms.ModelForm):
    class Meta:
        model= Truck
        fields='__all__'
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_location', 'destination', 'preference']
        widgets = {
            'pickup_location': forms.TextInput(attrs={'class':'form-control','id':'id_pickup_location'}),
            'destination': forms.TextInput(attrs={'class':'form-control','id':'id_destination'}),
            'preference': forms.Select(attrs={'class':'form-select','id':'id_preference'}),
        }
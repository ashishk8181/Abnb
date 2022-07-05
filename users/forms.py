from . import models
from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email Address", "class":"input w-full"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Your Password", "class":"input w-full"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Incorrect Password"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Your Password"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Your Password Again"}), label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User with this Email already exists")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data["password"]
        password1 = self.cleaned_data["password1"]

        if password != password1:
            raise forms.ValidationError("Passwords don't Match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()

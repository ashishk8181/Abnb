from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from . import forms, models, mixins
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        # next_arg = self.request.query_params.get('next',None)
        print(self.request.GET)
        # print(next_arg)
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    logout(request)
    messages.info(request, f"See you later")
    return redirect(reverse("core:home"))


class SignUpView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)






class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"

    
class UpdateProfileView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):
    
    model = models.User
    template_name = "users/update_profile.html"
    success_message = "Profile Updated"
    fields = {
        "first_name",
        "last_name",
        "gender",
        "bio",
        "birthdate",
        "language",
        "currency",
    }

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["first_name"].widget.attrs={"placeholder": "First Name"}
        form.fields["last_name"].widget.attrs={"placeholder": "Last Name"}
        form.fields["bio"].widget.attrs={"placeholder": "About You"}
        form.fields["gender"].widget.attrs={"placeholder": "Gender"}
        form.fields["birthdate"].widget.attrs={"placeholder": "Birth Date"}
        form.fields["language"].widget.attrs={"placeholder": "Language"}
        form.fields["currency"].widget.attrs={"placeholder": "Curency"}
        return form


class PasswordChangeView(mixins.LoggedInOnlyView, mixins.EmailLoginOnlyView, SuccessMessageMixin, PasswordChangeView):

    template_name = "users/update-password.html"
    success_message = "Password Updated"
 
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["old_password"].widget.attrs={"placeholder": "Current Password"}
        form.fields["new_password1"].widget.attrs={"placeholder": "New Password"}
        form.fields["new_password2"].widget.attrs={"placeholder": "Confirm New Password"}
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()


@login_required
def switch_hosting(request):
    try: 
        del request.session["is_hosting"]
    except KeyError:
        request.session["is_hosting"] = True
    return redirect(reverse("core:home"))

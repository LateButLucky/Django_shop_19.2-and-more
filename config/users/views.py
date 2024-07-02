from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        send_mail(
            'Verify your email',
            'Please verify your email by clicking this link.',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        login(self.request, user)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'


class CustomPasswordResetView(generic.FormView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = CustomUser.objects.get(email=email)
        new_password = CustomUser.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            'Your new password',
            f'Your new password is {new_password}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)

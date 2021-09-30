from django.contrib.auth.models import *
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class UserCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_superuser']


class UserUpdateForm(BSModalForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'is_superuser']


class ChangePasswordForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']





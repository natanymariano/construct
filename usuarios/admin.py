from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django #esse AS é para não confundir com o ADMIN uilizado na linha 1, pois ambos são diferentes.
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin) :
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import UserAdminCreationForm, UserAdminChangeForm
from accounts.models import User

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin')
    list_filter = ('admin','staff', 'student', 'cr', 'outsider', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','batch',)}),
        ('Permissions', {'fields': ('admin','staff', 'student', 'cr', 'outsider', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'batch', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

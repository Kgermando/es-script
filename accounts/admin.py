from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.site_header = 'CRM ADMIN'
admin.site.site_title = "Interface d'administration des comptes"

from accounts.models import Profile, Campagne

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_is_online', 'get_campagne', 'get_role',)
    list_select_related = ('profile', )

    def get_is_online(self, instance):
        return instance.profile.is_online
    get_is_online.short_description = 'is_online'

    def get_campagne(self, instance):
        return instance.profile.campagne
    get_campagne.short_description = 'Campagne'

    def get_role(self, instance):
        return instance.profile.role
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class CampagneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Campagne)

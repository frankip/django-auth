import django
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

admin.site.unregister(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'full_names','is_staff', 'is_active', 'date_joined')
    date_hierarchy = 'date_joined'
    
    list_filter =('date_joined',)
    # pass
    
    @admin.display(empty_value='unknown')
    def full_names(self, obj):
        return ("%s" %(obj.get_full_name()))

admin.site.register(User, UserAdmin)
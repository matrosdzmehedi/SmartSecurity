from django.contrib import admin
from .models import UserInfo

# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'flat_no', 'phone_no',
                    'profession', 'address', 'marig_status')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(UserInfo, UserInfoAdmin)

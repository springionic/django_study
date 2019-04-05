from django.contrib import admin
from .models import AddressInfo

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    fields = ['address', 'pid']


admin.site.register(AddressInfo, AddressAdmin)
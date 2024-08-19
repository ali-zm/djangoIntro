from django.contrib import admin
from .models import Employer
from application.models import Application

# Register your models here.


class ApplicationInline(admin.TabularInline):
    model = Application

class EmployerAdmin(admin.ModelAdmin):
    inlines=[ApplicationInline]
    model = Employer
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Employer, EmployerAdmin)
from django.contrib import admin
from .models import Organization, Event, OrganizationEvent 


class MembershipInline(admin.TabularInline):
    model = OrganizationEvent
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Organization, OrganizationAdmin)
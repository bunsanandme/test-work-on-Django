from django.contrib import admin
from .models import Organization, Event, OrganizationEvent
from django.utils.safestring import mark_safe


class MembershipInline(admin.TabularInline):
    model = OrganizationEvent
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ("title", "date")
    list_filter = ("date", "organizations")
    search_fields = ("title__startswith", )

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ("title", "address")
    list_filter = ("postcode", )
    search_fields = ("title__startswith", )

admin.site.register(Event, EventAdmin)
admin.site.register(Organization, OrganizationAdmin)
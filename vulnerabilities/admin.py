from django.contrib import admin
from .models import Vulnerability, FixedVulnerability


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('cve_id', 'description', 'severity')
    search_fields = ('cve_id', 'description')


class FixedVulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('vulnerability', 'fixed_at', 'fixed_by')
    search_fields = ('vulnerability__cve_id',)


admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(FixedVulnerability, FixedVulnerabilityAdmin)

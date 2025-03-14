from django.contrib.auth.models import User
from django.db import models


class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    severity = models.CharField(max_length=20)

    def __str__(self):
        return self.cve_id


class FixedVulnerability(models.Model):
    vulnerability = models.OneToOneField(Vulnerability, on_delete=models.CASCADE)
    fixed_at = models.DateTimeField(auto_now_add=True)
    fixed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Fixed: {self.vulnerability.cve_id}"

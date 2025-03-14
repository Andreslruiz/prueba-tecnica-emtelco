from django.core.management.base import BaseCommand
import requests
from vulnerabilities.models import Vulnerability


class Command(BaseCommand):
    help = 'Import vulnerabilities from NIST API'

    def handle(self, *args, **kwargs):
        nist_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
        response = requests.get(nist_url)

        if response.status_code == 200:
            vulnerabilities_data = response.json()

            for vuln in vulnerabilities_data['vulnerabilities']:
                cve_id = vuln['cve']['id']
                description = vuln['cve']['descriptions'][0]['value'] if 'descriptions' in vuln['cve'] else 'No description'

                severity = 'Unknown'
                if 'cvssMetricV2' in vuln['cve']['metrics']:
                    cvss_data = vuln['cve']['metrics']['cvssMetricV2'][0]
                    severity = cvss_data['baseSeverity']

                if not Vulnerability.objects.filter(cve_id=cve_id).exists():
                    Vulnerability.objects.create(
                        cve_id=cve_id,
                        description=description,
                        severity=severity
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Vulnerabilidad con CVE {cve_id} ya existe.")
                    )
        else:
            self.stdout.write(
                self.style.ERROR(f"Error al obtener datos: {response.status_code}")
            )

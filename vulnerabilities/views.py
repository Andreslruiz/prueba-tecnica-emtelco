import logging

from django.views import generic
from rest_framework import status
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import VulnerabilitySerializer, FixedVulnerabilitySerializer
from .models import Vulnerability, FixedVulnerability

logger = logging.getLogger('django.rest_framework')


class DeleteVulnerabilityView(APIView):
    def delete(self, request, cve_id):
        logger.info(f"DELETE /api/vulnerabilities/{cve_id} - Intentando eliminar vulnerabilidad")
        try:
            vulnerability = Vulnerability.objects.get(cve_id=cve_id)
            vulnerability.delete()
            logger.info(f"DELETE /api/vulnerabilities/{cve_id} - Eliminación exitosa")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vulnerability.DoesNotExist:
            logger.warning(f"DELETE /api/vulnerabilities/{cve_id} - Vulnerabilidad no encontrada")
            return Response({"error": "Vulnerabilidad no encontrada"}, status=status.HTTP_404_NOT_FOUND)


class VulnerabilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer

    def list(self, request, *args, **kwargs):
        logger.info("GET /api/vulnerabilities - Listando todas las vulnerabilidades")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        cve_id = kwargs.get('pk')
        logger.info(f"GET /api/vulnerabilities/{cve_id} - Obteniendo detalles de vulnerabilidad")
        return super().retrieve(request, *args, **kwargs)


class FixedVulnerabilityViewSet(viewsets.ModelViewSet):
    queryset = FixedVulnerability.objects.all()
    serializer_class = FixedVulnerabilitySerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"POST /api/fixed - Registrando vulnerabilidad fixeada con datos: {request.data}")
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(fixed_by=self.request.user)
        logger.info(f"POST /api/fixed - Vulnerabilidad fixeada guardada exitosamente por {self.request.user}")

    def destroy(self, request, *args, **kwargs):
        cve_id = kwargs.get('pk')
        logger.warning(f"DELETE /api/fixed/{cve_id} - Eliminando vulnerabilidad fixeada")
        return super().destroy(request, *args, **kwargs)


class UnfixedVulnerabilityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VulnerabilitySerializer

    def get_queryset(self):
        fixed_ids = FixedVulnerability.objects.values_list('vulnerability__id', flat=True)
        return Vulnerability.objects.exclude(id__in=fixed_ids)

    def list(self, request, *args, **kwargs):
        logger.info("GET /api/unfixed - Listando vulnerabilidades no fixeadas")
        queryset = self.get_queryset()
        if not queryset:
            logger.info("GET /api/unfixed - No hay vulnerabilidades sin resolver")
            return Response(
                {"message": "No hay vulnerabilidades sin resolver"},
                status=200
            )
        return super().list(request, *args, **kwargs)


class VulnerabilitySummaryViewSet(viewsets.ViewSet):
    def list(self, request):
        logger.info("GET /api/vulnerabilities-summary - Obteniendo resumen de vulnerabilidades por severidad")
        summary = list(Vulnerability.objects.values('severity').annotate(total=Count('severity')))
        if not summary:
            logger.info("GET /api/vulnerabilities-summary - No hay registros disponibles")
            return Response({"message": "No hay registros disponibles"}, status=200)
        return Response(summary)


class InitialView(generic.TemplateView):

    template_name = 'vulnerabilities/vulnerabilities_initial.html'
    permission_required = 'vulnerabilities.can_see_initial_view'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, QuestionViewSet, ResultByKnowledgeAreaView, ResultViewSet, KnowledgeAreaViewSet, survey_status, user_detail, calculate_domain_averages, calculate_oe_domain_averages, CalculateAllDomainAverages, calculate_all_domain_averages_percent, oe_status

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('employees', EmployeeViewSet, basename="employee")
router.register('questions', QuestionViewSet, basename="know")
router.register('knowladge-area', KnowledgeAreaViewSet)
router.register('results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('status/', view=survey_status),
    path('oe_status/', view=oe_status),
    path('user_detail/', view=user_detail),
    path('average/', calculate_domain_averages,
         name='calculate_domain_averages'),
    path('average_oe/', calculate_oe_domain_averages,
         name='calculate_domain_averages'),
    path('all/', CalculateAllDomainAverages.as_view(),
         name='calculate_all_domain_averages'),
    path('percent/', calculate_all_domain_averages_percent,
         name='calculate_all_domain_averages'),
    path('api/results/by-knowledge-area/',
         ResultByKnowledgeAreaView.as_view(), name='result_by_knowledge_area'),
]

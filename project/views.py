from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Company, Employee, Question, Result, KnowledgeArea
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    QuestionSerializer,
    ResultSerializer,
    CompanyCreateSerializer,
    KnowladgeSerializer, QuestionGetSerializer, CompanyNameSerializer, ResultGet, EmployeeGetSerializer, ResultsSerializer
)
from core.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from django.http import JsonResponse
from rest_framework import status

from django.db.models import Sum

from rest_framework.views import APIView
from collections import defaultdict
from django.db.models import Avg  # Add this import


class ResultByKnowledgeAreaView(APIView):
    def get(self, request):
        # Get query parameters
        company_id = request.query_params.get('company_id')
        employee_id = request.query_params.get('employee_id')
        domain = request.query_params.get('domain')
        stage = request.query_params.get('stage')
        oe = request.query_params.get('oe')
        process_group = request.query_params.get('process_group')
        excluded_stages = ['cultural', 'humanresources', 'structural', 'technological']
        included = ["standardize", "measure", "control", "improve"]
        pg= ["Initiating", "Planning", "Integration Management", "Executing", "Monitoring and Controlling", "Closing"]

        queryset = Result.objects.all()

        # Filter results by company_id, employee_id, and domain
        if domain:
            queryset = Result.objects.filter(
                company_id=company_id,
                employee_id=employee_id,
                domain=domain
            )

            if stage:
                queryset = queryset.filter(stage=stage)

        elif process_group:
            response_data = []
            for i in pg:
                queryset = Result.objects.filter(
                    company_id=company_id,
                    employee_id=employee_id,
                    process_group=i
                )
                stage_averages = (
                    queryset
                    .values('process_group')
                    .annotate(average=Avg('result'))
                )
                count_stage = queryset.filter(process_group=i).count()
                # Create list of dictionaries for response
                for stage_data in stage_averages:
                    stage_name = stage_data['process_group']
                    print(count_stage)
                    print(stage_data['average'] )
                    
                    if count_stage > 0:
                        avg = stage_data['average']
                    else:
                        avg = stage_data['average'] / 1
                    print(count_stage)
                    average_result = round(avg, 2)
                    response_data.append({'subject': stage_name, 'A': average_result})

            return Response(response_data)

        elif stage:
            queryset = Result.objects.filter(
                company_id=company_id,
                employee_id=employee_id,
                stage=stage
            )
            stage_averages = (
                queryset
                .values('stage')
                .annotate(average=Avg('result'))
            )
            count_stage = queryset.filter(stage=stage).count()
            # Create list of dictionaries for response
            response_data = []
            for stage_data in stage_averages:
                stage_name = stage_data['stage']
                avg = stage_data['average'] 
                print(count_stage)
                average_result = round(avg, 2)
                response_data.append({'subject': stage_name, 'A': average_result})

            return Response(response_data)
        
        elif oe:
            response_data = []
            for i in excluded_stages:
                queryset = Result.objects.filter(
                    company_id=company_id,
                    employee_id=employee_id,
                    stage=i
                )
                stage_averages = (
                    queryset
                    .values('stage')
                    .annotate(average=Avg('result'))
                )
                count_stage = queryset.filter(stage=i).count()
                # Create list of dictionaries for response
                for stage_data in stage_averages:
                    stage_name = stage_data['stage']
                    print(count_stage)
                    print(stage_data['average'] )
                    
                    if count_stage > 0:
                        avg = stage_data['average']
                    else:
                        avg = stage_data['average'] / 1
                    print(count_stage)
                    average_result = round(avg, 2)
                    response_data.append({'subject': stage_name, 'A': average_result})

            return Response(response_data)
        else:
            response_data = []
            for i in included:
                queryset = Result.objects.filter(
                    company_id=company_id,
                    employee_id=employee_id,
                    stage=i
                )
                stage_averages = (
                    queryset
                    .values('stage')
                    .annotate(average=Avg('result'))
                )
                count_stage = queryset.filter(stage=i).count()
                # Create list of dictionaries for response
                for stage_data in stage_averages:
                    stage_name = stage_data['stage']
                    if count_stage > 0:
                        avg = stage_data['average']
                    else:
                        avg = stage_data['average'] / 1
                    print(count_stage)
                    average_result = round(avg, 2)
                    response_data.append({'subject': stage_name, 'A': average_result})

            return Response(response_data)

        # Initialize a dictionary to store results and totals grouped by knowledge areas
        results_by_knowledge_area = defaultdict(lambda: {'total_result': 0, 'total_number': 0})

        # Iterate through each result in the queryset
        for result in queryset:
            # Check if the knowledge area is not None
            if result.knowledge_area:
                knowledge_area_name = result.knowledge_area.name

                # Accumulate the result and total number for the knowledge area
                results_by_knowledge_area[knowledge_area_name]['total_result'] += result.result
                results_by_knowledge_area[knowledge_area_name]['total_number'] += result.total_number

        # Calculate average result for each knowledge area
        for knowledge_area, values in results_by_knowledge_area.items():
            total_result = values['total_result']
            total_number = values['total_number']
            average_result = total_result / total_number if total_number != 0 else 0
            # Round the average result to two decimal points
            results_by_knowledge_area[knowledge_area]['average_result'] = round(average_result, 2)

        # Serialize the data
        serialized_data = []
        for knowledge_area, values in results_by_knowledge_area.items():
            data = {
                'subject': knowledge_area,
                'A': values['average_result']
            }
            serialized_data.append(data)

        return Response(serialized_data)



@api_view(['GET'])
def calculate_all_domain_averages_percent(request):
    company_id = request.GET.get('company_id')
    employee_id = request.GET.get('employee_id')

    if company_id and employee_id:
        results = (
            Result.objects
            .filter(company_id=company_id, employee_id=employee_id)
            .aggregate(total_number=Sum('total_number'), result=Sum('result'))
        )

        total_number = results.get('total_number', 0)
        result = results.get('result', 0)

        if total_number != 0:
            average = result / total_number
            average_percent = (result / total_number) * 100
        else:
            average = 0
            average_percent = 0

        data = {
            'average': average,
            'percent': average_percent/4
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Please provide company_id and employee_id parameters'})

class CalculateAllDomainAverages(APIView):
    def get(self, request):
        company_id = request.query_params.get('company_id')
        employee_id = request.query_params.get('employee_id')

        if company_id and employee_id:
            results = (
                Result.objects
                .filter(company_id=company_id, employee_id=employee_id)
                .values('domain')
                .annotate(total_number=Sum('total_number'), result=Sum('result'))
            )

            domain_averages = {}
            for domain_data in results:
                domain = domain_data['domain']
                total_number = domain_data.get('total_number', 0)
                result = domain_data.get('result', 0)
                if total_number != 0:
                    average = result / total_number
                else:
                    average = 0
                domain_averages[domain] = {'total_number': total_number, 'result': result, 'average': round(average, 2)}

            return Response(domain_averages)
        else:
            return Response({'error': 'Please provide company_id and employee_id parameters'})

@api_view(['POST'])
def user_detail(request):
    if request.method == 'POST':
        data = request.data
        user_id = data.get("id")
        try:
            user = User.objects.get(id=user_id)
            is_admin = user.is_staff
            if user.user_type == 'employee':
                try:
                    employee = Employee.objects.get(user=user)
                    company = employee.company
                    company_serializer = CompanyNameSerializer(company)
                    return Response({'company': company_serializer.data, "employee": employee.id, "is_admin": is_admin, "survey": user.survey}, status=status.HTTP_200_OK)
                except Employee.DoesNotExist:
                    # Return a 404 response if employee record not found
                    return Response({'error': 'Employee record not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    company = Company.objects.get(user=user)
                    company_serializer = CompanySerializer(company)  # Serialize the Company object
                    return Response({'company': company_serializer.data,  "is_admin": is_admin}, status=status.HTTP_200_OK)
                except Company.DoesNotExist:
                    return Response({'error': 'Company record not found'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def survey_status(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        survey = "taken"

        user = User.objects.get(id=id)
        user.survey = survey
        user.save()
        return Response({"message": "Submitted successfully!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def calculate_domain_averages(request):
    company_id = request.GET.get('company_id')
    employee_id = request.GET.get('employee_id')

    if company_id and employee_id:
        # Define process groups excluding "oe"
        process_groups = ['initiating', 'planning', 'executing', 'm&c', 'closing']

        results = (
            Result.objects
            .filter(company_id=company_id, employee_id=employee_id)
            .exclude(domain='oe')  # Exclude "oe" domain
            .exclude(process_group__isnull=True)  # Exclude null process groups
            .values('process_group')
            .annotate(total_number=Count('id'), result=Count('result'))
            .order_by('process_group')
        )

        domain_averages = {}
        for process_group_data in results:
            total_number = process_group_data.get('total_number', 0)
            if total_number != 0:
                average = process_group_data['result'] / total_number
                domain_averages[process_group_data['process_group']] = {
                    'process_group': process_group_data['process_group'],
                    'average': average
                }

        # Fill in missing process groups with zero averages
        for process_group in process_groups:
            if process_group not in domain_averages:
                domain_averages[process_group] = {'process_group': process_group, 'average': 0}

        return JsonResponse(domain_averages)
    else:
        return JsonResponse({'error': 'Please provide company_id and employee_id parameters'})


@api_view(['GET'])
def calculate_oe_domain_averages(request):
    company_id = request.GET.get('company_id')
    employee_id = request.GET.get('employee_id')

    if company_id and employee_id:
        # Define stages excluding "oe"
        stages = ["human-resources", "cultural", "technological", "structural"]

        results = (
            Result.objects
            .filter(company_id=company_id, employee_id=employee_id, domain='oe')
            .values('stage')
            .annotate(total_number=Count('id'), result=Count('result'))
            .order_by('stage')
        )

        domain_averages = {}
        for stage_data in results:
            total_number = stage_data.get('total_number', 0)
            if total_number != 0:
                average = stage_data['result'] / total_number
                domain_averages[stage_data['stage']] = {
                    'stage': stage_data['stage'],
                    'average': average
                }

        # Fill in missing stages with zero averages
        for stage in stages:
            if stage not in domain_averages:
                domain_averages[stage] = {'stage': stage, 'average': 0}

        return JsonResponse(domain_averages)
    else:
        return JsonResponse({'error': 'Please provide company_id and employee_id parameters'})


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CompanyCreateSerializer
        return CompanySerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

class EmployeeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Employee.objects.all()
        company_id = self.request.query_params.get('company_id')
        if company_id:
            queryset = queryset.filter(company_id=company_id, user__survey="taken")
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeSerializer
        return EmployeeGetSerializer

class KnowledgeAreaViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeArea.objects.all()
    serializer_class = KnowladgeSerializer

class QuestionViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionSerializer
        return QuestionGetSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        knowledge_area_id = self.request.query_params.get('knowledge_area_id')
        stage = self.request.query_params.get('stage')
        domain = self.request.query_params.get('domain')

        if knowledge_area_id and stage and domain:
            queryset = queryset.filter(
                knowledge_area__id=knowledge_area_id,
                stage=stage,
                domain=domain
            )
        elif stage:
            queryset = queryset.filter(stage=stage)
        elif domain:
            queryset = queryset.filter(domain=domain)

        return queryset


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.filter(domain="oe")
    serializer_class = ResultsSerializer  # Make sure this serializer matches the queryset fields

    def get_serializer_class(self):
        if self.action == 'create':
            return ResultSerializer
        return ResultsSerializer

    # def get_queryset(self):
    #     queryset = Result.objects.all()

    #     # Filtering based on query parameters
    #     company_id = self.request.query_params.get('company_id')
    #     employee_id = self.request.query_params.get('employee_id')
    #     stage = self.request.query_params.get('stage')
    #     domain = self.request.query_params.get('domain')
    #     knowledge_area = self.request.query_params.get('knowledge_area')

    #     if company_id:
    #         queryset = queryset.filter(company_id=company_id)
    #     if employee_id:
    #         queryset = queryset.filter(employee_id=employee_id)
    #     if domain:
    #         queryset = queryset.filter(domain=domain)
    #     if stage:
    #         queryset = queryset.filter(stage=stage)
    #     if knowledge_area and knowledge_area != "gs":
    #         queryset = queryset.filter(knowledge_area=knowledge_area)

    #     # Grouping by knowledge area and annotating total count
    #     queryset = queryset.values('company', 'knowledge_area').annotate(total=Count('id'))

    #     return queryset
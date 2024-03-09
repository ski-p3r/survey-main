from rest_framework import serializers
from .models import Company, Employee, Question, Result, KnowledgeArea
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Company
        fields = '__all__'

class CompanyNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = Company
        fields = ['id','name']

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeGetSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
class KnowladgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeArea
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionGetSerializer(serializers.ModelSerializer):
    knowledge_area = KnowladgeSerializer()
    class Meta:
        model = Question
        fields = '__all__'

from rest_framework import serializers
from .models import Result

class ResultsSerializer(serializers.ModelSerializer):
    average = serializers.SerializerMethodField()
    knowledge_area_name = serializers.CharField(source='knowledge_area.name', read_only=True)
    class Meta:
        model = Result
        fields = ['company', 'employee', 'process_group', 'knowledge_area_name', 'stage', 'average']

    def get_average(self, obj):
        if obj.total_number != 0:  # Avoid division by zero
            return obj.result / obj.total_number
        return None  # Handle the case where total_number is zero


class ResultSerializer(serializers.ModelSerializer):
    knowledge_area_name = serializers.CharField(source='knowledge_area.name', read_only=True)  # Access name directly
    ratio = serializers.SerializerMethodField()  # Define SerializerMethodField

    class Meta:
        model = Result
        fields = ['id', 'company', 'employee', 'domain', 'stage', 'knowledge_area', 'knowledge_area_name', 'result', 'total_number', 'process_group', 'ratio']

    def get_ratio(self, obj):
        if obj.total_number != 0:  # Avoid division by zero
            return obj.result / obj.total_number
        return None  # Handle the case where total_number is zero

class ResultGet(serializers.ModelSerializer):
    subject = serializers.CharField(source='knowledge_area.name', read_only=True)
    A = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = ['subject', 'A']

    def get_A(self, obj):
        if obj.total_number != 0:  # Avoid division by zero
            return obj.result / obj.total_number
        return None  # Handle the case where total_number is zero

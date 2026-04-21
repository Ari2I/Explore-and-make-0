from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    deadline_after = filters.DateFilter(field_name='deadline', lookup_expr='gte')
    deadline_before = filters.DateFilter(field_name='deadline', lookup_expr='lte')

    class Meta:
        model = Task
        fields = [
            'project',
            'status',
            'priority',
            'performer',
        ]
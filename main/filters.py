import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains")
    description = CharFilter(field_name='description', lookup_expr="icontains")
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = [ 'created_at',]
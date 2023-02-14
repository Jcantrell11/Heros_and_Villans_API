from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from rest_framework import status
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        super_type_type = request.query_params.get('super_type')
        print(super_type_type)
        queryset = Super.objects.all()
        
        if super_type_type:
            queryset = queryset.filter(super_type__type=super_type_type)
        
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


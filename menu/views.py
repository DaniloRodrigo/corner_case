from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.utils import timezone
import datetime
import logging
import sys

logger = logging.getLogger(__name__)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_restaurant(request, pk):
    try:
        obj = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        logger.error('Restaurant not found.')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(obj)
        logger.info('[GET] Restaurant %s selected.'% obj.title)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        logger.info('[DELETE] Restaurant %s deleted.' % obj.title)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[PUT] Restaurant %s updated.' % obj.title)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        logger.error('[PUT] Restaurant payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_restaurant(request):

    if request.method == 'GET':
        objs = Restaurant.objects.all()
        serializer = RestaurantSerializer(objs, many=True)
        logger.info('[GET] All restaurants selected')
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
        }
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[POST] Restaurant %s created.' % request.data.get('title'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('[POST] Restaurant payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_employee(request, pk):
    try:
        obj = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        logger.error('Employee not found.')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(obj)
        logger.info('[GET] Employee %s selected.' % obj.name)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        logger.info('[DELETE] Employee %s deleted.' % obj.name)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[PUT] Employee %s updated.' % obj.name)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        logger.error('[PUT] Employee payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_employee(request):

    if request.method == 'GET':
        objs = Employee.objects.all()
        serializer = EmployeeSerializer(objs, many=True)
        logger.info('[GET] All employees selected.')
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'username': request.data.get('username'),
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[POST] Employee %s created.' % request.data.get('name'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('[POST] Employee payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_menu(request, pk):
    try:
        obj = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        logger.error('Menu not found.')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(obj)
        logger.info('[GET] Menu %s selected.' % obj.id)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        logger.info('[DELETE] Menu %s deleted.' % obj.id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_menu(request):

    if request.method == 'GET':
        objs = Menu.objects.all()
        serializer = MenuSerializer(objs, many=True)
        logger.info('All menus selected.')
        return Response(serializer.data)


@api_view(['GET'])
def get_today_menu(request):
    objs = Vote.objects.filter(created_at=timezone.datetime.today())
    serializer = VoteSerializer(objs, many=True)
    logger.info('[GET] All menus today selected.')
    return Response(serializer.data)


@api_view(['POST'])
def get_menus_by_date(request):
    data = request.data
    date = datetime.date(data.get('year'), data.get('month'), data.get('day'))
    objs = Menu.objects.filter(created_at=date)
    serializer = MenuSerializer(objs, many=True)
    logger.info('[POST] All menus for %s selected.' % date.isoformat())
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_post_vote(request):

    if request.method == 'GET':
        objs = Vote.objects.all()
        serializer = VoteSerializer(objs, many=True)
        logger.info('All Votes selected.')
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[POST] Vote %s created.' % request.data.get('id'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('[POST] Vote payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_votes_by_date(request):
    data = request.data
    date = datetime.date(data.get('year'), data.get('month'), data.get('day'))
    objs = Vote.objects.filter(created_at=date)
    serializer = VoteSerializer(objs, many=True)
    logger.info('[POST] All votes for %s selected.' % date.isoformat())
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_vote(request, pk):
    try:
        obj = Vote.objects.get(pk=pk)
    except Vote.DoesNotExist:
        logger.error('Vote not found.')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoteSerializer(obj)
        logger.info('[GET] Vote %s selected.' % obj.id)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        obj.delete()
        logger.info('[DELETE] Vote %s deleted.' % obj.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = VoteSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('[PUT] Vote %s updated.' % request.data.get('id'))
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        logger.error('[PUT] Vote payload not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                obj = Menu.objects.get(pk=pk)
                serializer = MenuSerializer(obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info('[PUT] Menu %s updated.' % obj.title)
                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
                logger.error('[PUT] Menu payload not valid.')
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Menu.DoesNotExist:
                logger.error('Menu not found.')
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info('[POST] Menu %s created.' % request.data.get('title'))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error('[POST] Menu payload not valid.')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


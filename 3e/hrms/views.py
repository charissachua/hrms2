# Create your views here.
from django.http import HttpResponseRedirect, Http404
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection


from .serializers import *
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import *


class UserList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'


class BookCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = BookForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'examples/update_book.html'
    form_class = BookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'examples/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'examples/delete_book.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('index')


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all().select_related('user')
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all().select_related('user')
    serializer_class = EmployeeSerializer



class EmployeeDetailsView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_object(self, pk):
        try:
            return EmployeeDetails.objects.get(pk=pk)
        except EmployeeDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeDetailsSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeDetailsSerializer(employee, data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('add_new_employee', [serializer.data['username'],
                                                     serializer.data['password'],
                                                     serializer.data['first_name'],
                                                     serializer.data['last_name'],
                                                     serializer.data['email'],
                                                     serializer.data['date_joined'],
                                                     serializer.data['is_superuser']])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeFullDetailsView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_object(self, pk):
        try:
            return EmployeeFullDetails.objects.get(pk=pk)
        except EmployeeFullDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeFullDetailsSerializer(employee)
        return Response(serializer.data)


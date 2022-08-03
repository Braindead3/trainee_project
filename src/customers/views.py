from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .filters import CustomerViewSetFilter, OfferViewSetFilter, CustomerShowroomPurchaseViewSetFilter
from .models import Customer, Offer, CustomerShowroomPurchase
from .serializers import (CustomerSerializer, OfferSerializer, CustomerShowroomPurchaseSerializer, UserSerializer,
                          UserResetPasswordSerializer, UserUsernameSerializer, UserEmailSerializer)
from .utils import Email, get_user_by_token


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filterset_class = CustomerViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['name', 'address']
    ordering_fields = ['balance', 'name']


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    filterset_class = OfferViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['car__name', 'customer__name']
    ordering_fields = ['max_price']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False)
    def register_new_user(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = user.username

            token = RefreshToken.for_user(user).access_token
            user_email = user.email
            current_site = get_current_site(request)
            relative_link = reverse('email_verification')
            subject = 'Verify your email'
            abs_ulr = f'http://{current_site}{relative_link}?token={str(token)}'
            email_body = f'Hi {user.username}. Use link below to verify your email. \n {abs_ulr}'

            Email.send_email(user_email, subject, email_body)
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def verify_account(self, request, *args, **kwargs):
        token = request.GET.get('token')
        user = get_user_by_token(token)
        return Response(f'Verify use is :{user.username}')

    @action(methods=['get'], detail=False)
    def request_to_change_password(self, request):

        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token:
            token = request.META.get('HTTP_AUTHORIZATION', None).split()[-1]
            user = get_user_by_token(token)

            user_email = user.email
            current_site = get_current_site(request)
            relative_link = reverse('password_reset')
            subject = f'Reset password on {current_site}'
            abs_ulr = f'http://{current_site}{relative_link}?token={str(token)}'
            email_body = f'Hi {user.username}. Use link below to change your password. \n {abs_ulr}'

            Email.send_email(user_email, subject, email_body)

            return Response('Email sanded')
        return Response('Token not provided or invalid token')

    @action(methods=['post'], detail=False)
    def change_password(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = request.META.get('HTTP_AUTHORIZATION', None)
            if token:
                token = request.META.get('HTTP_AUTHORIZATION', None).split()[-1]
                user: User = get_user_by_token(token)
                user.set_password(serializer.validated_data['password1'])
                user.save()
                return Response('New password set')
        else:
            data = serializer.errors
        return Response(data)

    @action(methods=['post'], detail=False)
    def change_username(self, request):
        serializer = UserUsernameSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            token = request.META.get('HTTP_AUTHORIZATION', None)
            if token:
                token = request.META.get('HTTP_AUTHORIZATION', None).split()[-1]
                user: User = get_user_by_token(token)
                user.username = serializer.validated_data['username']
                user.save()
                return Response('New username set')
        else:
            data = serializer.errors
        return Response(data)

    @action(methods=['post'], detail=False)
    def change_email(self, request):
        serializer = UserEmailSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            token = request.META.get('HTTP_AUTHORIZATION', None)
            if token:
                token = request.META.get('HTTP_AUTHORIZATION', None).split()[-1]
                user: User = get_user_by_token(token)
                user.username = serializer.validated_data['username']
                user.save()
                return Response('New username set')
        else:
            data = serializer.errors
        return Response(data)


class CustomerShowroomPurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerShowroomPurchaseSerializer
    queryset = CustomerShowroomPurchase.objects.all()
    filterset_class = CustomerShowroomPurchaseViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['customer__name']
    ordering_fields = ['is_sale', 'sale_date', 'purchase_date', 'price']

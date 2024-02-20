from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from members.models import Member
from members.serializers import MemberSerializer

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CustmAuthToken(ObtainAuthToken):
  
  def post(self, request, *args, **kwargs):
    
    serializer = self.serializer_class(data = request.data, context = {'request':request})
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user = user)
    
    return Response({'token':token.key, 'user_id':user.pk, 'user_name':user.user_name})
#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.models import User
from .models import Bin
from .serializers import *

class SubmitTrash(GenericAPIView):
    serializer_class = defaultNull
    queryset = Bin.objects.all()

    def post(self, request, *args, **kwargs):
        bin = get_object_or_404(Bin, id=kwargs["pk"])
        user_id = request.data["user_id"]
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)
            # if not user.is_verified:
            #     return Response({"message": "This user is not verified, kindly verify your account"}, status=status.HTTP_404_NOT_FOUND)
            if user.account_type == "individual":
                user.reward_points += 1
                bin.waste_count += 1
                user.save()
                bin.save()
                return Response({"message": "Submission Successful!"}, status=status.HTTP_200_OK)
            return Response({"message": "Account type(Business) is illegeble. Kindly update account type in your user profile."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "This user does not exist, kindly enter a valid user id."}, status=status.HTTP_200_OK)
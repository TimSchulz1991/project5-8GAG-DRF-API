from .serializers import CustomTokenObtainPairSerializer, CurrentUserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated


# to provide a landing page
@api_view()
def root_route(request):
    return Response({"message": "Welcome to my django rest framework API!"})


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def current_user(request):
    return Response(CurrentUserSerializer(request.user).data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

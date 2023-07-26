from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

# 이렇게 API VIEW를 상속받으면 api 문서에 기본적으로 나타나게 됨.
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_date

        refresh = RefreshToken.for_user(user)
        response = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response)




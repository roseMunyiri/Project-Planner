from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import User, OneTimePassword
from .serializers import UserSerializer

from .utils import send_code_to_user
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer, PasswordResetRequestSerializer, PasswordResetTokenGenerator, SetNewPasswordSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def post(self, request):
        user_data = request.data
        seriallizer = self.serializer_class(data=user_data)
        if seriallizer.is_valid(raise_exception=True):
            seriallizer.save()
            user = seriallizer.data
            '''send email fn'''
            send_code_to_user(user['email'])
            return Response({
                'data': user,
                'message': f'Hello  thanks for signing up a passcode'
            }, status=status.HTTP_201_CREATED)
        return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)

'''class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        '''

class UserLoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserLogoutView(generics.DestroyAPIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)

class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserVerificationEmail(GenericAPIView):
    def post(self, request):
        otp_code = request.data.get('otp')

        try:
            user_code_obj = OneTimePassword.objects.get(code=otp_code)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message': 'Email account verified successfully'
                }, status=status.HTTP_200_OK)
            return Response({
                    'message': 'Invalid code, user already verified'
                }, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist:
            return Response({
                    'message': 'Passcode not provided' 
                }, status=status.HTTP_404_NOT_FOUND)


class TestAuthTokenView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'message': 'generated user-tokens works perfectly fine'
        }
        return Response(data, status=status.HTTP_200_OK)
    
class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'A link to reset your password has been sent to your email'})
        
class PasswordResetConfirm(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id =smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message': 'Token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success': True, 'message':'Valid Credentials', 'uidb64':uidb64, 'token': token}, status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError:
            return Response({'message': 'Token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        
class SetNewPassword(GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Password reset successful'}, 200)


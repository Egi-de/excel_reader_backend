from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, LoginView, ExcelDataUploadView, ExcelDataListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('excel/upload/', ExcelDataUploadView.as_view(), name='excel_upload'),
    path('excel/list/', ExcelDataListView.as_view(), name='excel_list'),
]

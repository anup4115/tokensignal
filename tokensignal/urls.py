from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api import views
router=DefaultRouter()

router.register('stu',views.StudentApi,basename='stud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('st/', include(router.urls)),
    path('gettoken/', obtain_auth_token),
]

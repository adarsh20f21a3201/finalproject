"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finalproject import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendexammails', views.sendexammails),
    path('', views.homepage),
    path('s/<para>', views.s),
    path('clubs/<para>', views.clubs),
    path('pythonclub', views.pythonclub),
    path('codeingclub', views.codeingclub),
    path('debateclubs', views.debateclubs),
    path('graphicclubs', views.graphicclubs),
    path('ideaclubs', views.ideaclubs),
    path('literacyclubs', views.literacyclubs),
    path('speakingclubs', views.speakingclubs),
    path('womenclubs', views.womenclubs),
    path('innerwheel', views.innerwheel),
    path('euphoria', views.euphoria),
    path('project', views.project),
    path('campusradio', views.campusradio),
    path('about', views.about),
    path('abouts/<para>', views.abouts),
    path('departments', views.departments),
    path('departmentss/<para>', views.departmentss,name='departmentss'),
    path('computerscienceandengineering', views.computerscienceandengineering),
    path('computerscienceandengineeringai', views.computerscienceandengineeringai),
    path('computerscienceandengineeringds', views.computerscienceandengineeringds),
    path('electricalandelectronicsengineering', views.electricalandelectronicsengineering),
    path('civilengineering', views.civilengineering),
    path('mechanicalengineering', views.mechanicalengineering),
    path('electronicsandcommunicationsengineering', views.electronicsandcommunicationsengineering),
    path('humanitiesandbasicsciences', views.humanitiesandbasicsciences),
    path('departmentofmanagementstudies', views.departmentofmanagementstudies),
    path('cybersecrity', views.cybersecrity),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),
    path('accounts/<para>', views.accounts,name="accounts"),
    path('account/<para>',views.account,name='account'),
    path('signup', views.signup,name="signup"),
    path('forget', views.forget,name="forget"),
    path('otpverify', views.otpverify,name="otpverify"),
    path('departandrolls/<para>', views.departandroll,name="departandroll"),
    path('image_upload_view/<para>', views.image_upload_view,name="image_upload_view"),

    

]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

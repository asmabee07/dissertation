from django.urls import include, path


from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.index, name='index'),
    path('registration/signup/', views.signup, name='signup'),
    path('registration/', include('django.contrib.auth.urls')),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('complete_profile/<int:pk>/', views.complete_profile, name='complete_profile_edit'),
    path('dietary_intake/', views.dietary_intake, name='dietary_intake'),
    path('sample_chart/', views.sample_chart, name='sample_chart'),
    path('highcharts/', views.highcharts, name='highcharts'),
    path('highcharts_demo/', views.highcharts_demo, name='highcharts_demo'),

]

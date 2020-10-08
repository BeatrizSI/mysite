from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>',views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),
    path('<int:question_id>/result/', views.ResultView.as_view(), name='result'),
    path('sobre', views.SobreView.as_view(), name='sobre'),
]
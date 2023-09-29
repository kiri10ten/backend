from django.urls import path

from . import views


urlpatterns = [
    path('', views.BrowseArchiveView.as_view()),
    path('subjects/', views.SubjectView.as_view()),
    path('myarchive/', views.MyArchiveView.as_view()),
    path('create/', views.CreateArchiveView.as_view()),
    path('newest/', views.NewestArchiveView.as_view()),
    path('<int:pk>/', views.ArchiveDetailView.as_view()),
    path('<int:pk>/delete/', views.CreateArchiveView.as_view()),
    path('<int:pk>/edit/', views.CreateArchiveView.as_view()),
]

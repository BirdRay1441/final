from django.urls import path
from my_app import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student'),
    path('admins/', views.admin, name='admins'),
    path('teacher/', views.teachers, name='teacher'),
    # path('lection/<TypeID>/', views.MaterialsListView.as_view(), name='type'),
    # path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    # path('<TypeID>/', views.PhotoListView.as_view(), name='photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
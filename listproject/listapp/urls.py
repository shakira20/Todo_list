from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    # path('detail',views.detail,name='detail')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbview/',views.Tasklistview.as_view(),name='cbview'),
    path('cbdetailview/<int:pk>/',views.Detailtaskview.as_view(),name='cbdetailview'),
    path('cbupdateview/<int:pk>/',views.Updatetask.as_view(),name='cbupdateview'),
    path('cbdeleteview/<int:pk>/',views.Deletetask.as_view(),name='cbdeleteview')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
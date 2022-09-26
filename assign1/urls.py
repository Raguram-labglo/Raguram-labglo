from django.urls import path
from . import views
urlpatterns = [path('', views.show, name = 'details'),
               path('students',views.add_form, name = 'add_student' ),
               path('marks',views.add_marks, name = 'add_marks' ),
               path('show_mark/<int:id>',views.show_mark, name = 'show_mark' ),
               path('update_stu/<int:id>',views.update_stu, name = 'upd_stu' ),
               path('update_mark/<int:id>',views.update_mark, name = 'upd_mar' ),
               path('del_stu/<int:id>',views.del_student, name = 'del_stu' ),
               path('delete_mark/<int:id>', views.del_mark, name = 'del_mark'),
               ]


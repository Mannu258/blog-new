from django.urls import path
from . views import home,logout_user,register,add_blog,blog_detail,see_blog,blog_delete,blog_update

urlpatterns = [
    path('', home,name='home'),
    path('logout', logout_user ,name='logoutapp'),
    path('registration',register,name='registration'),
    path('add-blog',add_blog,name='addblog'),
    path('blog-detail/<slug>',blog_detail,name='blog_detail'),
    path('see-blog',see_blog,name='see_blog'),
    path('delete-blog<id>',blog_delete,name='blog_delete'),
    path('blog-update/<slug>',blog_update,name='blog_update'),







]

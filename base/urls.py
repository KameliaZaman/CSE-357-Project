from django.urls import path
from . import views
from .views import blogView, blogDetailView, addBlogView,updateBlogView
from .import HodViews, StudentViews

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

	path('blog/', blogView.as_view(), name="blog"),
    path('blog/<int:pk>',blogDetailView.as_view(),name="blogDetail"),
    path('addBlog/',addBlogView.as_view(),name="addBlog"),
    path('blog/update/<int:pk>',updateBlogView.as_view(),name="updateBlog" ),
    path('student_fcm_token_save', StudentViews.student_fcm_token_save,name="studentFcmTokenSave"),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js")

]
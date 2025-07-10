from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import token_obtain_pair , token_refresh
from main.views import *


schema_view = get_schema_view(
   openapi.Info(
      title="Portfolio API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('token/', token_obtain_pair ),
    path('token/refresh/', token_refresh ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

urlpatterns += [
    path('user/', UserProfileView.as_view(), name='user-detail'),

    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('admin/skills/create/', SkillCreateView.as_view(), name='skill-create'),
    path('admin/skills/<int:pk>/', SkillRetrieveDeleteUpdateView.as_view(), name='skill-detail'),

    path('softskills/', SoftSkillListAPIView.as_view(), name='softskill-list'),
    path('admin/skills/<int:pk>/', SoftSkillRetrieveDeleteUpdateView.as_view(), name='softskill-detail'),


    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('admin-projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('admin-projects/<int:pk>/', ProjectRetrieveDeleteUpdateView.as_view(), name='project-detail'),

    path('blogs/', BlogPostListView.as_view(), name='blog-list'),
    path('admin-blogs/create/', BlogPostCreateView.as_view(), name='blog-create'),
    path('admin-blogs/<slug:slug>/', BlogPostRetrieveUpdateView.as_view(), name='blog-detail'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog'),

    path('admin-blog-cover-image/create/', BlogCoverImageCreateView.as_view(), name='blog-cover'),
    path('admin-blog-cover-image/<int:pk>/', BlogCoverImageRetrieveDeleteUpdateView.as_view(), name='blog-cover-detail'),

    path('admin-project-cover-image/create/', ProjectsCoverImageCreateView.as_view(), name='project-cover'),
    path('admin-project-cover-image/<int:pk>/', ProjectsCoverImageRetrieveDeleteUpdateView.as_view(), name='project-cover-detail'),

    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('admin-experience/create/', ExperienceCreateView.as_view(), name='experience-create'),
    path('admin-experience/<int:pk>/', ExperienceRetrieveDeleteUpdateView.as_view(), name='experience-detail'),


    path('educations/', EducationListView.as_view(), name='education-list'),
    path('admin-education/create/', EducationCreateView.as_view(), name='education-create'),
    path('admin-education/<int:pk>/', EducationRetrieveDeleteUpdateView.as_view(), name='education-detail'),

    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('admin-messages/<int:pk>/', MessageRetrieveDeleteUpdateView.as_view(), name='message-detail'),

    path('page-views/', PageViewLogListView.as_view(), name='pageview-log-list'),

    path('blogs/comments/<int:blog_id>/', CommentsListView.as_view(), name='message-list'),
    path('comments/last/', LastCommentsView.as_view(), name='last-two-comments'),

    path('comments/create/', CommentCreateView.as_view(), name='message-create'),

    path('tags/', TagListView.as_view(),)

]

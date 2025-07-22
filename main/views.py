from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from main.serializers import *
from .pagenations import CustomPageNumberPagination

class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class UserProfilUpdate(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

class SkillCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class SkillRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [AllowAny]

class ProjectRetrieveDeleteUpdateView(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerCreate
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class BlogPostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializerCreate
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]
    lookup_field = 'slug'

class BlogPostRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip = self.get_client_ip(request)

        PageViewLog.objects.get_or_create(
            project=instance,
            ip_address=ip,
        )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    lookup_field = 'slug'


class BlogPostUpdateView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'slug'


class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip = self.get_client_ip(request)

        PageViewLog.objects.get_or_create(
            project=instance,
            ip_address=ip,
        )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]

class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

class ExperienceRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationsSerializer
    permission_classes = [AllowAny]

class EducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationsSerializer
    permission_classes = [IsAuthenticated]

class EducationRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationsSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

class MessageRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

class PageViewLogListView(generics.ListAPIView):
    queryset = PageViewLog.objects.all()
    serializer_class = PageViewLogSerializer
    permission_classes = [IsAuthenticated]

class CommentsListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(BlogPost, id=blog_id)
        return Comment.objects.filter(blog=blog, is_published=True).order_by('-id')

class LastCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = None  # pagination yo'q

    def get_queryset(self):
        return Comment.objects.filter(is_published=True).order_by('-created_at')[:2]


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [AllowAny()]


class BlogCoverImageCreateView(generics.CreateAPIView):
    queryset = BlogCoverImage.objects.all()
    serializer_class = BlogCoverImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

class BlogCoverImageRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCoverImage.objects.all()
    serializer_class = BlogCoverImageSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

class ProjectsCoverImageCreateView(generics.CreateAPIView):
    queryset = ProjectCoverImage.objects.all()
    serializer_class = ProjectsCoverImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]


class ProjectsCoverImageRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCoverImage.objects.all()
    serializer_class = ProjectsCoverImageSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]


class SoftSkillListAPIView(generics.ListCreateAPIView):
    serializer_class = SoftSkillSerializer

    def get_queryset(self):
        return SoftSkill.objects.filter(is_active=True)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

class SoftSkillRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftSkill.objects.all()
    serializer_class = SkillSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]



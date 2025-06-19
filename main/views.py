from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from main.serializers import *

class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

class ProjectRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class BlogPostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
    parser_classes = [FormParser, MultiPartParser]

class BlogPostRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
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


class BlogContentListView(generics.ListAPIView):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer
    permission_classes = [AllowAny]

class BlogContentCreateView(generics.CreateAPIView):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer
    permission_classes = [IsAuthenticated]

class BlogContentRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class MessageRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class PageViewLogListView(generics.ListAPIView):
    queryset = PageViewLog.objects.all()
    serializer_class = PageViewLogSerializer
    permission_classes = [IsAuthenticated]


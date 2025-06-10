from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['slug']

    def get_view_count(self, obj):
        return obj.views.count()

class BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PageViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageViewLog
        fields = '__all__'



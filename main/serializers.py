from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'location', 'github', 'linkedin', 'website']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectsCoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCoverImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    cover_images = ProjectsCoverImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class BlogCoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCoverImage
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    view_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    cover_images = BlogCoverImageSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['slug']

    def get_view_count(self, obj):
        return obj.views.count()
    def get_comment_count(self, obj):
        return obj.comment_set.count()

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']



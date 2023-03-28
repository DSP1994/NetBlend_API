from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Article
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'created_on',
            'modified_on',
            'profile_id',
            'profile_image',
        ]

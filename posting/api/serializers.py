from rest_framework import serializers
from posting.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Converts to JSON
    Validations for data passed
    """
    class Meta:
        model = BlogPost
        fields = ['pk', 'title', 'user', 'content', 'timestamp']
        read_only_fields = ['pk', 'user']

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The title has already been used!")
        return value


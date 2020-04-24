from django.contrib import admin
from .models import BlogPost


class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'timestamp']
    list_display_links = ['title', 'user', 'timestamp']
    # list_editable = ['video_link']
    list_filter = ['user', 'timestamp']
    search_fields = ['title', 'user', 'timestamp']
    # export_order = ['user', 'phone_number', 'father_name', 'mother_name', 'address']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostModelAdmin)

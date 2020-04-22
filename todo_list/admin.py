from django.contrib import admin
from .models import Todo


class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at', 'update_at']
    list_display_links = ['title', 'is_completed', 'created_at', 'update_at']
    # list_editable = ['video_link']
    list_filter = ['is_completed', 'created_at', 'update_at']
    search_fields = ['title', 'created_at']
    # export_order = ['user', 'phone_number', 'father_name', 'mother_name', 'address']

    class Meta:
        model = Todo


admin.site.register(Todo, TodoModelAdmin)

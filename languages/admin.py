from django.contrib import admin
from .models import Language, Paradigm, Programmer


class ParadigmModelAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ['name']
    # list_editable = ['video_link']
    # list_filter = ['is_active', 'date_joined']
    search_fields = ['name', ]
    # export_order = ['user', 'phone_number', 'father_name', 'mother_name', 'address']

    class Meta:
        model = Paradigm


admin.site.register(Paradigm, ParadigmModelAdmin)


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'paradigm']
    list_display_links = ['name']
    # list_editable = ['video_link']
    # list_filter = ['is_active', 'date_joined']
    search_fields = ['name', 'paradigm']
    # export_order = ['user', 'phone_number', 'father_name', 'mother_name', 'address']

    class Meta:
        model = Language


admin.site.register(Language, LanguageModelAdmin)


class ProgrammerModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    # list_editable = ['video_link']
    # list_filter = ['is_active', 'date_joined']
    search_fields = ['name',]
    # export_order = ['user', 'phone_number', 'father_name', 'mother_name', 'address']

    class Meta:
        model = Programmer


admin.site.register(Programmer, ProgrammerModelAdmin)

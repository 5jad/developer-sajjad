from django.contrib import admin
from .models import (
    Skill, Language, Certification, Education,
    WorkExperience, WorkResponsibility, Project,
    ProjectTechnology, Interest, PersonalInfo, Quote
)


class WorkResponsibilityInline(admin.TabularInline):
    model = WorkResponsibility
    extra = 1


class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [WorkResponsibilityInline]
    list_display = ('title', 'company', 'start_date', 'is_current')
    list_filter = ('is_current',)
    ordering = ('-start_date',)


class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTechnologyInline]
    list_display = ('title', 'is_featured', 'order', 'url')
    list_editable = ('is_featured', 'order')  # تعديل مباشر من القائمة
    list_filter = ('is_featured',)
    ordering = ('order',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_obtained', 'order')
    list_editable = ('order',)
    ordering = ('order',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    ordering = ('-start_date',)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')


class QuoteAdmin(admin.ModelAdmin):          # ✅ جديد
    list_display = ('text', 'author', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(PersonalInfo)
admin.site.register(Quote, QuoteAdmin)       # ✅ جديد
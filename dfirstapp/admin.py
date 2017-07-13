from django.contrib import admin

# Register your models here.
from dfirstapp.models import *

class StudentInterestInline(admin.TabularInline):
    model = StudentInterest
    extra = 0

class StudentSkillInline(admin.TabularInline):
    model = StudentSkill
    extra = 0

class StudentLinkInline(admin.TabularInline):
    model = StudentLink
    extra = 0

class StudentProfileAdmin(admin.ModelAdmin):
    model = StudentProfile
    list_display = ['name', 'email']
    search_fields = ['name', 'email']
    inlines = [StudentInterestInline, StudentSkillInline, StudentLinkInline]

class TeamSkillInline(admin.TabularInline):
    model = TeamSkill
    extra = 0

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 0

class TeamProfileAdmin(admin.ModelAdmin):
    model = TeamProfile
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [TeamSkillInline, TeamMemberInline]

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeamProfile, TeamProfileAdmin)

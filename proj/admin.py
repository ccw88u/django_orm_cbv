from django.contrib import admin
from proj.models import Reguser, website, website_subject, company, member
# Register your models here.


class ReguserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
admin.site.register(Reguser, ReguserAdmin)


class admindispfmt1_website_subject(admin.ModelAdmin):
    list_display = ('subject_name', )
admin.site.register(website_subject, admindispfmt1_website_subject)


class admindispfmt1_website(admin.ModelAdmin):
    list_display = ('title', 'subject', 'uri')
admin.site.register(website, admindispfmt1_website)


class admindispfmt1_company(admin.ModelAdmin):
    list_display = ('name', 'tel')
admin.site.register(company, admindispfmt1_company)

class admindispfmt1_member(admin.ModelAdmin):
    list_display = ('name', 'age')
admin.site.register(member, admindispfmt1_member)
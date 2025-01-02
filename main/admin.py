from django.contrib import admin
from main.models import HomePage, Parquet, AboutUsCard, AboutUs, Projects, Reviews, OurGallery

admin.site.register(HomePage)

class AboutUsCardInline(admin.StackedInline):
    model = AboutUsCard
    extra = 3

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsCardInline, ]

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Parquet)
admin.site.register(Reviews)
admin.site.register(Projects)
admin.site.register(OurGallery)

from django.contrib import admin
from main.models import HomePage, Parquet, AboutUsCard, AboutUs, Projects, ParquetSanding, ParquetInstallation, \
    ParquetRefinishing, LocalRestoration, Reviews, OurGallery

admin.site.register(ParquetSanding)
admin.site.register(ParquetInstallation)
admin.site.register(ParquetRefinishing)
admin.site.register(LocalRestoration)

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

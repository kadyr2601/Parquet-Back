from django.db import models
from django.core.exceptions import ValidationError


class Parquet(models.Model):
    title_ru = models.CharField(max_length=128)
    title_en = models.CharField(max_length=128)
    description_ru = models.TextField()
    description_en = models.TextField()
    image_left = models.FileField(upload_to='Parquet/')
    image_right = models.FileField(upload_to='Parquet/')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Parquet Banners'
        verbose_name_plural = 'Parquet Banners'

class AboutUsCard(models.Model):
    first_paragraph_ru = models.CharField(max_length=50)
    first_paragraph_en = models.CharField(max_length=50)
    second_paragraph_ru = models.CharField(max_length=50)
    second_paragraph_en = models.CharField(max_length=50)
    third_paragraph_ru = models.CharField(max_length=50)
    third_paragraph_en = models.CharField(max_length=50)
    fourth_paragraph_ru = models.CharField(max_length=50)
    fourth_paragraph_en = models.CharField(max_length=50)
    about_us = models.ForeignKey('AboutUs', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'About Us Card'
        verbose_name_plural = 'About Us Card'


class AboutUs(models.Model):
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.FileField(upload_to='AboutUs/')

    class Meta:
        verbose_name = 'About Us Banner'
        verbose_name_plural = 'About Us Banner'

class Projects(models.Model):
    icon = models.ImageField(upload_to='Projects/')

    class Meta:
        verbose_name = 'Projects Banner'
        verbose_name_plural = 'Projects Banner'


class Reviews(models.Model):
    comment_ru = models.TextField()
    comment_en = models.TextField()
    fullname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Reviews/')

    class Meta:
        verbose_name = 'Reviews Banner'
        verbose_name_plural = 'Reviews Banner'


class OurGallery(models.Model):
    image = models.ImageField(upload_to='OurGallery/')

    class Meta:
        verbose_name = 'Our Gallery Banner'
        verbose_name_plural = 'Our Gallery Banner'

class HomePage(models.Model):
    main_banner = models.FileField(upload_to='main_banner/')
    section_image = models.ImageField(upload_to='section_image/')
    parquet_sanding = models.OneToOneField(Parquet, on_delete=models.CASCADE, related_name='home_page_sanding', null=True, blank=True)
    parquet_installation = models.OneToOneField(Parquet, on_delete=models.CASCADE, related_name='home_page_installation', null=True, blank=True)
    parquet_refinishing = models.OneToOneField(Parquet, on_delete=models.CASCADE, related_name='home_page_refinishing', null=True, blank=True)
    local_restoration = models.OneToOneField(Parquet, on_delete=models.CASCADE, related_name='home_page_restoration', null=True, blank=True)
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='home_page_about_us', null=True, blank=True)
    projects = models.ManyToManyField(Projects, blank=True)
    reviews = models.ManyToManyField(Reviews, blank=True)
    gallery = models.ManyToManyField(OurGallery, blank=True)

    def __str__(self):
        return "Home Page Instance"

    def clean(self):
        if HomePage.objects.exists() and not self.pk:
            raise ValidationError("Only one HomePage instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(HomePage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'


class ParquetSanding(models.Model):
    image_before = models.ImageField(upload_to='ParquetSanding/')
    image_after = models.ImageField(upload_to='ParquetSanding/')
    title_ru = models.TextField()
    title_en = models.TextField()
    price_ru = models.TextField()
    price_en = models.TextField()

    def __str__(self):
        return "Parquet Sanding Instance"

    class Meta:
        verbose_name = 'Parquet Sanding Details'
        verbose_name_plural = 'Parquet Sanding Details'


class ParquetInstallation(models.Model):
    title_ru = models.CharField(max_length=512)
    title_en = models.CharField(max_length=512)
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to='ParquetInstallation/')

    class Meta:
        verbose_name = 'Parquet Installation Details'
        verbose_name_plural = 'Parquet Installation Details'


class ParquetRefinishing(models.Model):
    title_ru = models.CharField(max_length=512)
    title_en = models.CharField(max_length=512)
    price_ru = models.CharField(max_length=512)
    price_en = models.CharField(max_length=512)
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to='ParquetRefinishing/')

    class Meta:
        verbose_name = 'Parquet Refinishing Details'
        verbose_name_plural = 'Parquet Refinishing Details'

    def __str__(self):
        return "Parquet Refinishing Instance"

    def clean(self):
        if ParquetRefinishing.objects.exists() and not self.pk:
            raise ValidationError("Only one Parquet Refinishing instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ParquetRefinishing, self).save(*args, **kwargs)


class LocalRestoration(models.Model):
    background_image = models.ImageField(upload_to='LocalRestoration/')
    description_ru = models.TextField()
    description_en = models.TextField()
    image1 = models.ImageField(upload_to='LocalRestoration/')
    image2 = models.ImageField(upload_to='LocalRestoration/')
    image3 = models.ImageField(upload_to='LocalRestoration/')

    class Meta:
        verbose_name = 'Local Restoration Details'
        verbose_name_plural = 'Local Restoration Details'

    def __str__(self):
        return "Local Restoration Instance"

    def clean(self):
        if LocalRestoration.objects.exists() and not self.pk:
            raise ValidationError("Only one Local Restoration instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(LocalRestoration, self).save(*args, **kwargs)


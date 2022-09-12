from django.db import models
from .producer import publish



# Create your models here.
class cdnProvider(models.Model):
    title = models.CharField(max_length=20, default=None)
    country = models.CharField(max_length=3, blank=True)

    def __str__(self):
        """return string representation"""
        return self.title


class Site(models.Model):
    """Database model for Websites Info."""
    def save(self, *args, **kwargs):
        super(Site, self).save(*args, **kwargs)
        publish(self.IP)

    title_En = models.CharField(max_length=20, default=None)
    title_Fa = models.CharField(max_length=20, default=None)
    URL = models.URLField()
    IP = models.CharField(max_length=30, default=None)
    subject = models.ManyToManyField('Subject', through="SubjectSite")
    location = models.CharField(max_length=3, default=None)
    cdn_provider = models.ForeignKey(cdnProvider, on_delete=models.CASCADE)


    def __str__(self):
        """return string representation"""
        return self.URL


class Subject(models.Model):
    subject = models.CharField(max_length=30, default=None)

    def __str__(self):
        """return string representation"""
        return self.subject


class SubjectSite(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        """return string representation"""
        return self.site.URL


class QualityOfService(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    jitter = models.DecimalField(max_digits=19, decimal_places=4)
    delay = models.DecimalField(max_digits=19, decimal_places=4)
    load_time = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        """return string representation"""
        return self.site.URL






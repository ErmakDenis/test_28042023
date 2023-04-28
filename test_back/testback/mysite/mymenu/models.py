
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    def save(self, *args, **kwargs):
        if self.parent:
            self.url_name = '{}-{}'.format(self.parent.url_name, self.slug)
        else:
            self.url_name = self.slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


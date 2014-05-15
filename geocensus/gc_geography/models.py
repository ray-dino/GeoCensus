from django.contrib.gis.db import models


class Baranggay(models.Model):
    name = models.CharField(max_length=2048, null=True, blank=True)
    polygon = models.MultiPolygonField()
    center = models.PointField()

    def save(self, *args, **kwargs):
        self.center = self.polygon.centroid
        super(Baranggay, self).save(*args, **kwargs)

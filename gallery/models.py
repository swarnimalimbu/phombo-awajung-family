from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="phombo_photos/")
    caption = models.CharField(max_length=255, blank=True)
    contributor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption or "Phombo Photo"


from django.db import models


class Text(models.Model):
    text = models.CharField(max_length=10000, default="No text was entered")
    title = models.CharField(max_length=64, default="No title was entered")

    def __str__(self):
        return f"The text is: {self.text}, and the title is: {self.title}"

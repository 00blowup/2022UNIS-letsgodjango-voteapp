from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title


class Option(models.Model):
    name = models.CharField(max_length=20, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Vote(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    DEPARTMENT_CHOICES = [
            ("1", "Management"),
            ("2", "Marketing & sales"),
            ("3", "Billing"),
            ("4", "Legal"),
            ("5", "Human Resourse"),
            ("6", "UX team"),
            ("7", "Backend team"),
            ("8", "DevOps team"),
            ("9", "IT"),
        ]
    STATUS_CHOICES = [
            ("1", "Open"),
            ("2", "Closed"),
        ]
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="1",)
    department = models.CharField(
        max_length=15,
        choices=DEPARTMENT_CHOICES,
        default="1",
        )

    def __str__(self):
        return self.title + "\n"+self.description+"\n"+self.creator.username

class FollowUp(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="followup", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.ticket.title, self.creator)


# Create your models here.

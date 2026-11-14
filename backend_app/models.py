from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()          # <-- Added ()
    subject = models.CharField(max_length=100)
    message = models.TextField()         # <-- Added ()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):                   # <-- Indented inside Contact
        return self.full_name

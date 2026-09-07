from django.db import models


class Chore(models.Model):
    name = models.CharField(max_length=200)
    interval_days = models.PositiveIntegerField(
        help_text="Expected number of days between completions."
    )

    def __str__(self):
        return self.name


class LogEntry(models.Model):
    chore = models.ForeignKey(
        Chore, on_delete=models.CASCADE, related_name="log_entries"
    )
    completed_at = models.DateTimeField()

    class Meta:
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.chore.name} @ {self.completed_at}"

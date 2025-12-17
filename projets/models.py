from django.db import models
from utilisateurs.models import Utilisateur
import uuid

class Project(models.Model):
    TYPE_CHOICES = [
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    author = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'projets_projet'  # keep old table
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Contributor(models.Model):
    ROLE_CHOICES = [
        ('AUTHOR', 'Author'),
        ('CONTRIBUTOR', 'Contributor'),
    ]

    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CONTRIBUTOR')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.title} ({self.role})"

    class Meta:
        db_table = 'projets_contributeur'
        unique_together = ('user', 'project')


class Issue(models.Model):
    TAG_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE','Feature'),
        ('TASK', 'Task'),  
    ]
  
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    STATUS_CHOICES = [
        ('TODO', 'To do'),
        ('IN_PROGRESS', 'In progress'),
        ('FINISHED', 'Finished'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='TODO')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    author = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='created_issues')
    assigned_to = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, related_name='assigned_issues')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.tag})"

    class Meta:
        db_table = 'projets_probleme'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.issue.title}"

    class Meta:
        db_table = 'projets_commentaire'
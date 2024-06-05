from django.db import models

# Create your models here.
class CodeExplainer(models.Model):
    _input = models.TextField()
    _method = _method = models.CharField(max_length=100, blank=True, null=True)
    _output = models.TextField()

    class Meta:
        db_table = "t_code_explainer"
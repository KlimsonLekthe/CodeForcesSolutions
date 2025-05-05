from django.db import models

class Questions(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    category = models.CharField(max_length = 1)
    unique_id = models.CharField(max_length = 10, unique = True)
    source = models.URLField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
    solution = models.TextField()
    language = models.CharField(default = 'Python')
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.question.title}, {self.solution}"


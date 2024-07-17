from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    is_lent = models.BooleanField(default=False)
    lent_to = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class LendRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    lend_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} lent to {self.user}"

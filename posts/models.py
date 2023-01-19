from django.db import models
from django.conf import settings

class Post(models.Model):
    JUSTICE = 'JUS'
    BUILDING = 'BUI'
    EDUCATION = 'EDU'
    ROUTINE_WORK = 'ROU'
    IT = 'IT'
    MEDICINE = "MED"
    AGROCULTURE = "AGR"
    BIZNES = "BS"
    TURIZM = "TUR"
    TRADE = "TR"


    TYPES_OF_CATEGORY = [
        (JUSTICE, "Юстиция"),
        (BUILDING, "Строителстьво"),
        (EDUCATION, "Образование"),
        (ROUTINE_WORK, "Бытовая работа"),
        (IT, "ИКТ"),
        (MEDICINE, "Медицина"),
        (AGROCULTURE, "Аграрное дело"),
        (BIZNES, "Бизнес"),
        (TURIZM, "Туризм"),
        (TRADE, "Торговля"),

]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    body = models.TextField()
    price = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=TYPES_OF_CATEGORY, default=JUSTICE)
    phone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
# Generated by Django 4.1.4 on 2023-01-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("JUS", "Юстиция"),
                    ("BUI", "Строителстьво"),
                    ("EDU", "Образование"),
                    ("ROU", "Бытовая работа"),
                    ("IT", "ИКТ"),
                    ("MED", "Медицина"),
                    ("AGR", "Аграрное дело"),
                    ("BS", "Бизнес"),
                    ("TUR", "Туризм"),
                    ("TR", "Торговля"),
                ],
                default="JUS",
                max_length=20,
            ),
        ),
    ]

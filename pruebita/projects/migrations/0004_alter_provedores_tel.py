# Generated by Django 4.1.2 on 2022-10-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_provedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedores',
            name='tel',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_articulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('razon_social', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=60)),
                ('tel', models.IntegerField()),
            ],
        ),
    ]

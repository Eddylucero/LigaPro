# Generated by Django 5.2 on 2025-06-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='anios_creacion',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

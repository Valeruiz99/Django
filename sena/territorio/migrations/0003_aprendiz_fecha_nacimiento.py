# Generated by Django 4.0.6 on 2022-07-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0002_monitorias_actividades'),
    ]

    operations = [
        migrations.AddField(
            model_name='aprendiz',
            name='fecha_nacimiento',
            field=models.DateField(default='1999-01-01'),
            preserve_default=False,
        ),
    ]
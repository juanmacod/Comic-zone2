# Generated by Django 4.2.4 on 2023-08-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]

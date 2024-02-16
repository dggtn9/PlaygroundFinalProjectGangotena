# Generated by Django 5.0.1 on 2024-02-16 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_comentarios_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='pais',
            field=models.CharField(max_length=20),
        ),
    ]

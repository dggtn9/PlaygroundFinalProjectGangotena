# Generated by Django 5.0.1 on 2024-03-03 15:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='participante_dos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participante_dos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='participante_uno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participante_uno', to=settings.AUTH_USER_MODEL),
        ),
    ]

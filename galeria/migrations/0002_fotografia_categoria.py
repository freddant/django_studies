# Generated by Django 5.2 on 2025-05-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÀXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=50),
        ),
    ]

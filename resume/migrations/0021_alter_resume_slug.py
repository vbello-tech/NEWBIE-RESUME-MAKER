# Generated by Django 3.2.15 on 2022-09-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_alter_resume_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='8te3be4t8jvki2if2eal'),
        ),
    ]
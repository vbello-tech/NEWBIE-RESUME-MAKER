# Generated by Django 3.2.15 on 2022-09-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0022_alter_resume_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='yymgdywrb4n8rk1nvwrg'),
        ),
    ]

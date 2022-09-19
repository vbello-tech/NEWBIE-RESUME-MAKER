# Generated by Django 3.2.15 on 2022-09-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0028_auto_20220918_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='wb5hz07i568i09kko88q'),
        ),
        migrations.RemoveField(
            model_name='resume',
            name='tech_skill',
        ),
        migrations.AddField(
            model_name='resume',
            name='tech_skill',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

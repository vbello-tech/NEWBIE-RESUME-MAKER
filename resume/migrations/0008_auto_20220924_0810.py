# Generated by Django 3.2.15 on 2022-09-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_resume_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='field',
            field=models.CharField(blank=True, choices=[('BSC SCIENCE', 'BSC SCIENCE'), ('BSC ENGINEERING', 'BSC ENGINEERING'), ('BSC FINANCE', 'BSC FINANCE'), ('BSC ECONOMICS AND BUSINESS', 'BSC ECONOMICS AND BUSINESS'), ('BSC APPLIED SCIENCES', 'BSC APPLIED SCIENCES'), ('BOOTCAMP', 'BOOTCAMP'), ('BSC LAW', 'BSC LAW')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='abipy3kq0hml24jo8lkr'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='type',
            field=models.CharField(blank=True, choices=[('LANGUAGE', 'LANGUAGE'), ('DATABASE', 'DATABASE'), ('FRAMEWORK', 'FRAMEWORK'), ('SOFTWARE', 'SOFTWARE'), ('CLOUD_PLATFORM', 'CLOUD_PLATFORM'), ('PARADIGM', 'PARADIGM')], max_length=200, null=True),
        ),
    ]

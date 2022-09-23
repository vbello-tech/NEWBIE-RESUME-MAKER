# Generated by Django 3.2.15 on 2022-09-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0031_auto_20220919_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Junior', 'Junior'), ('Mid-level', 'Mid'), ('Senior', 'Senior'), ('Principal', 'Principal'), ('C-level', 'CTO')], max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='x9qwslw7nf04k5uj38ou'),
        ),
        migrations.AddField(
            model_name='resume',
            name='tech',
            field=models.ManyToManyField(blank=True, null=True, to='resume.Level'),
        ),
    ]

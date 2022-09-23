# Generated by Django 3.2.15 on 2022-09-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0032_auto_20220919_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Junior', 'Junior'), ('Mid-level', 'Mid'), ('Senior', 'Senior'), ('Principal', 'Principal'), ('C-level', 'CTO')], max_length=50, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Level',
            new_name='Skills',
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='resume.Skills'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='e9geqiay4ezhm5715va7'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='tech',
            field=models.ManyToManyField(blank=True, null=True, to='resume.Tech'),
        ),
    ]

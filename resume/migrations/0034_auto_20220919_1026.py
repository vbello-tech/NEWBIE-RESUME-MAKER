# Generated by Django 3.2.15 on 2022-09-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0033_auto_20220919_1011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Frameworks_LIB_Software',
        ),
        migrations.RenameModel(
            old_name='Tech',
            new_name='Languages_DB_Paradim',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='tech',
        ),
        migrations.AddField(
            model_name='resume',
            name='fr_lb_sw',
            field=models.ManyToManyField(blank=True, to='resume.Frameworks_LIB_Software'),
        ),
        migrations.AddField(
            model_name='resume',
            name='la_db_pd',
            field=models.ManyToManyField(blank=True, to='resume.Languages_DB_Paradim'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='slug',
            field=models.SlugField(default='qov64yvf293cfeoydq6d'),
        ),
    ]

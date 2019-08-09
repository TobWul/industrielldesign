# Generated by Django 2.2.2 on 2019-08-09 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo', '0004_auto_20190728_1303'),
        ('authentication', '0009_remove_profile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_komite',
        ),
        migrations.AddField(
            model_name='profile',
            name='komite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leonardo.Komite'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='graduation_year',
            field=models.IntegerField(choices=[(2024, '1.klasse'), (2023, '2.klasse'), (2022, '3.klasse'), (2021, '4.klasse'), (2020, '5.klasse'), (5000, 'Alumni')], verbose_name='Klasse'),
        ),
    ]

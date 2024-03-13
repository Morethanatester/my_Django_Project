# Generated by Django 4.2.10 on 2024-03-13 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillsApp', '0004_rename_name_colleague_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleague',
            name='colleagueID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='colleague',
            name='jobfamily',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='colleague',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='colleague',
            name='tel',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='colleague',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skillsApp.colleague'),
        ),
    ]

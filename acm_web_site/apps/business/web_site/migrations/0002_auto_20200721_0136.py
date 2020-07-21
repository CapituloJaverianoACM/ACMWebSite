# Generated by Django 3.0.8 on 2020-07-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='activities', to='web_site.Gallery'),
        ),
        migrations.AlterField(
            model_name='project',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='projects', to='web_site.Gallery'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='tutorials', to='web_site.Gallery'),
        ),
    ]

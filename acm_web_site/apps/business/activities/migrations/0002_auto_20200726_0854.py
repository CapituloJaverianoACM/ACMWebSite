# Generated by Django 3.0.8 on 2020-07-26 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='members',
            field=models.ManyToManyField(related_name='activities', through='activities.ActivityMember', to='people.Member'),
        ),
        migrations.AlterField(
            model_name='activitymember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Member'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to='people.Member'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('picture', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('major', models.CharField(choices=[('IS', 'Ingeniería de Sistemas'), ('IE', 'Ingeniería Electrónica'), ('II', 'Ingeniería Industrial'), ('IC', 'Ingeniería Civil'), ('MT', 'Matemáticas'), ('OT', 'Otro')], max_length=50)),
                ('identification', models.CharField(max_length=50, null=True)),
                ('date_major', models.DateField(null=True)),
                ('date_chapter', models.DateField(null=True)),
                ('date_birth', models.DateField(null=True)),
                ('cellphone', models.CharField(max_length=20, null=True)),
                ('picture', models.CharField(max_length=200)),
                ('is_staff', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[('1PRE', 'Presidente'), ('2VIC', 'Vice-Presidente'), ('3SEC', 'Secretario'), ('4TES', 'Tesorero'), ('5CM', 'Comunity Manager'), ('6ME', 'Miembro')], max_length=5, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('reason', models.TextField(null=True)),
            ],
        ),
    ]

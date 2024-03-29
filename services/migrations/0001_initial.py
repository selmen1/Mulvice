# Generated by Django 2.0 on 2019-08-05 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=50)),
                ('discription', models.CharField(blank=True, max_length=250)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('lastname', models.CharField(blank=True, max_length=250, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('sexe', models.CharField(blank=True, max_length=50, null=True)),
                ('diplome', models.CharField(blank=True, max_length=250, null=True)),
                ('formation', models.CharField(blank=True, max_length=250, null=True)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('langtitude', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('service_name', models.CharField(blank=True, max_length=50)),
                ('discription', models.CharField(blank=True, max_length=250)),
                ('wilaya', models.CharField(blank=True, max_length=50, null=True)),
                ('comune', models.CharField(blank=True, max_length=50, null=True)),
                ('cover_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel', models.CharField(blank=True, max_length=12, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('categorie', models.ManyToManyField(blank=True, null=True, to='services.Categorie')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Profile')),
            ],
        ),
    ]

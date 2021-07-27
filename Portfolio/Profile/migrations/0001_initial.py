# Generated by Django 3.2.5 on 2021-07-27 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(default='static/user.png', upload_to='pics')),
                ('work_field', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=200)),
                ('birth', models.DateField()),
                ('desc', models.TextField(max_length=2000)),
                ('gender', models.CharField(max_length=50)),
                ('lang', models.CharField(max_length=100)),
                ('hobb', models.CharField(max_length=200)),
                ('add_skill', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_name', models.CharField(max_length=300)),
                ('cert_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_stdt', models.DateField()),
                ('edu_eddt', models.DateField()),
                ('edu_course', models.CharField(max_length=250)),
                ('edu_clg', models.CharField(max_length=150)),
                ('edu_mark', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_img', models.ImageField(default='static/user.png', upload_to='proj')),
                ('img_1', models.ImageField(default='static/user.png', upload_to='proj_img')),
                ('img_2', models.ImageField(default='static/user.png', upload_to='proj_img')),
                ('img_3', models.ImageField(default='static/user.png', upload_to='proj_img')),
                ('img_4', models.ImageField(default='static/user.png', upload_to='proj_img')),
                ('img_5', models.ImageField(default='static/user.png', upload_to='proj_img')),
                ('proj_stdt', models.DateField(null=True)),
                ('proj_eddt', models.DateField(null=True)),
                ('proj_title', models.CharField(max_length=300)),
                ('proj_desc', models.TextField(max_length=2000)),
                ('proj_url', models.URLField()),
                ('proj_sc', models.URLField(null=True)),
                ('front_e', models.CharField(max_length=200, null=True)),
                ('back_e', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=200)),
                ('perc', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git', models.URLField()),
                ('linked_in', models.URLField()),
                ('about', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.about')),
            ],
        ),
    ]

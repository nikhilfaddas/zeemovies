# Generated by Django 2.2.7 on 2019-11-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=50)),
                ('mRdate', models.DateField()),
                ('mLang', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=50)),
                ('uAge', models.IntegerField()),
                ('uGender', models.CharField(max_length=80)),
            ],
        ),
    ]
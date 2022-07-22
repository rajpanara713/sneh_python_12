# Generated by Django 4.0.4 on 2022-06-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

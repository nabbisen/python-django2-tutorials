# Generated by Django 2.0 on 2017-12-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=12)),
                ('form_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_id', models.CharField(max_length=6)),
            ],
        ),
    ]
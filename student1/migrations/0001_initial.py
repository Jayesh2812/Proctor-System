# Generated by Django 3.0.2 on 2020-01-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students_profile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
                ('std_name', models.CharField(max_length=30)),
                ('std_year', models.CharField(max_length=20)),
                ('std_branch', models.CharField(max_length=50)),
                ('std_phone_no', models.DecimalField(decimal_places=0, max_digits=10)),
                ('std_parent_phone_no', models.DecimalField(decimal_places=0, max_digits=10)),
                ('std_fathers_name', models.CharField(max_length=50)),
                ('std_mothers_name', models.CharField(max_length=50)),
                ('std_email', models.EmailField(max_length=250)),
                ('std_parent_email', models.EmailField(max_length=250)),
            ],
        ),
    ]
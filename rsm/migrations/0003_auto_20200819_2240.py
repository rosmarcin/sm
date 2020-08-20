# Generated by Django 3.1 on 2020-08-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsm', '0002_auto_20200819_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Busines Analyst'), (2, 'Data Scientist'), (3, 'Admin')], default=1, verbose_name='USER_PROFILE_TYPE'),
        ),
    ]

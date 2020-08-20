# Generated by Django 3.1 on 2020-08-19 12:30

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_login_date', models.DateTimeField(blank=True, null=True, verbose_name='first_login_date')),
                ('external_id_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='external_id_1')),
                ('external_id_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='external_id_2')),
                ('first_name', models.CharField(max_length=30, verbose_name='first_name')),
                ('middle_name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='middle_name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('maden_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='maden_name')),
                ('personal_email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='personal_email')),
                ('personal_email_confirmed', models.BooleanField(default=False, verbose_name='personal_email_confirmed')),
                ('secondary_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='secondary_email')),
                ('additional_information', models.TextField(blank=True, max_length=1000, null=True, verbose_name='additional_information')),
                ('user_profile_status', models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Not-Active'), (3, 'Prospect'), (4, 'Blocked')], default=1, verbose_name='user_profile_status')),
                ('pesel', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='pesel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_user', to=settings.AUTH_USER_MODEL, verbose_name='application_user')),
            ],
            options={
                'verbose_name': 'User_Profile',
                'verbose_name_plural': 'User_Profiles',
                'permissions': (('can_change_all_user_profile', 'Can change ALL User Profile'), ('can_view_all_user_profile', 'Can view ALL User Profile')),
            },
        ),
    ]

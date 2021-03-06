# Generated by Django 3.1 on 2020-08-20 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rsm', '0004_auto_20200820_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParametersGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.PositiveSmallIntegerField(choices=[('CH', 'CH - Swiss'), ('DE', 'DE - Germany'), ('IT', 'IT - Italia'), ('NL', 'NL - Netherlands'), ('PL', 'PL - Poland')], default=1, verbose_name='USER_PROFILE_TYPE')),
                ('version', models.CharField(max_length=20)),
                ('required', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('sales_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_model', to='rsm.salesmodel')),
            ],
            options={
                'verbose_name': 'Parameters Group',
                'verbose_name_plural': 'Parameters Groups',
            },
        ),
    ]

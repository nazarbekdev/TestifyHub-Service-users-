# Generated by Django 4.2.1 on 2025-01-11 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_botuser_invited_by_botuser_referral_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Fanlar',
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='OTM2025',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yonalish_kodi', models.IntegerField()),
                ('yonalish_nomi', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fan1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan1_kodi', to='service.fanlar')),
                ('fan2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan2_kodi', to='service.fanlar')),
            ],
            options={
                'verbose_name': 'OTM2025',
                'verbose_name_plural': 'OTM2025',
            },
        ),
    ]

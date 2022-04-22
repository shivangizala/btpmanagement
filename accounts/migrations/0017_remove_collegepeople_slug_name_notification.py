# Generated by Django 4.0.3 on 2022-04-13 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_collegepeople_slug_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegepeople',
            name='slug_name',
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(default='', max_length=100)),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
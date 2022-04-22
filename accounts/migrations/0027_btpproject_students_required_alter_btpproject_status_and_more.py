# Generated by Django 4.0.3 on 2022-04-20 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0026_alter_projectmember_accept_status_teamnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='btpproject',
            name='students_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btpproject',
            name='status',
            field=models.CharField(choices=[('closed', 'Closed'), ('open', 'Open')], default='open', max_length=100),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='accept_status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('requested', 'requested'), ('accepted', 'accepted')], default='rejected', max_length=100),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('agenda', models.TextField(blank=True, default='')),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
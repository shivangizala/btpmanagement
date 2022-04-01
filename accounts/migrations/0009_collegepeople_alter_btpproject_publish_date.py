# Generated by Django 4.0.3 on 2022-04-01 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_btpproject_content_alter_btpproject_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegePeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=100)),
                ('firstNAme', models.CharField(default='', max_length=100)),
                ('lastName', models.CharField(default='', max_length=100)),
                ('course', models.CharField(default='', max_length=100)),
                ('cpi', models.IntegerField(default=0)),
                ('is_student', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='btpproject',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

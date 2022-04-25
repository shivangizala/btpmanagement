# Generated by Django 4.0.3 on 2022-04-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_btpproject_projectid_alter_btpproject_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegepeople',
            name='student_status',
            field=models.CharField(choices=[('not taken', 'not taken'), ('taken', 'taken')], default='not taken', max_length=100),
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
    ]
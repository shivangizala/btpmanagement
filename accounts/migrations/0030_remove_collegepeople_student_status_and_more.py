# Generated by Django 4.0.3 on 2022-04-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_collegepeople_student_status_alter_btpproject_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegepeople',
            name='student_status',
        ),
        migrations.AddField(
            model_name='projectmember',
            name='student_status',
            field=models.CharField(choices=[('not taken', 'not taken'), ('taken', 'taken')], default='not taken', max_length=100),
        ),
        migrations.AlterField(
            model_name='btpproject',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=100),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='accept_status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('requested', 'requested'), ('rejected', 'rejected')], default='rejected', max_length=100),
        ),
    ]

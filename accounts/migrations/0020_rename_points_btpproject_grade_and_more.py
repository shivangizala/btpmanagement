# Generated by Django 4.0.3 on 2022-04-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_btpproject_points_alter_btpproject_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btpproject',
            old_name='points',
            new_name='grade',
        ),
        migrations.AlterField(
            model_name='btpproject',
            name='status',
            field=models.CharField(choices=[('closed', 'Closed'), ('open', 'Open')], default='open', max_length=100),
        ),
    ]

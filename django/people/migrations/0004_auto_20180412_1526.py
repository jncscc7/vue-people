# Generated by Django 2.0.4 on 2018-04-12 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180412_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='organisation',
            new_name='company',
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='github_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='hireable',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='person',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='github_login',
            field=models.CharField(max_length=32),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]

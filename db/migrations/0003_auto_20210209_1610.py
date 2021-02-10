# Generated by Django 3.1.5 on 2021-02-09 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20210209_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='my_tags',
        ),
        migrations.RemoveField(
            model_name='number',
            name='my_collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='tags',
            field=models.ManyToManyField(related_name='collections', to='db.Tag'),
        ),
        migrations.AddField(
            model_name='number',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='db.collection'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.7 on 2021-07-17 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1000)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('feed', models.CharField(max_length=10000)),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Feeds',
        ),
    ]

# Generated by Django 2.0.3 on 2019-05-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_remove_stateaction_next_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epsilon',
            fields=[
                ('data_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('eps', models.FloatField(default=1.0)),
            ],
        ),
    ]
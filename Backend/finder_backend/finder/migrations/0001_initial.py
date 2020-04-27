# Generated by Django 2.1.5 on 2019-02-06 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
                ('e2e_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='[a-f0-9]{12}')])),
                ('mfg_key', models.CharField(max_length=64)),
                ('is_lost', models.BooleanField()),
                ('contact', models.CharField(blank=True, max_length=64, null=True)),
                ('access_token', models.CharField(blank=True, max_length=64, null=True)),
                ('found_counter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='finding',
            name='tracker',
            field=models.ForeignKey(on_delete='CASCADE', to='finder.Tracker'),
        ),
        migrations.AlterUniqueTogether(
            name='finding',
            unique_together={('tracker', 'counter')},
        ),
    ]

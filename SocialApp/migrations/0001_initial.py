# Generated by Django 3.2.2 on 2021-05-06 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=256)),
                ('lastName', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialApp.user')),
            ],
        ),
    ]

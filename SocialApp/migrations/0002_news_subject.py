# Generated by Django 3.2.2 on 2021-05-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='subject',
            field=models.CharField(default='EmptySubject', max_length=256),
            preserve_default=False,
        ),
    ]

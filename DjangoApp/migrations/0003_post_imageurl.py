# Generated by Django 5.0.3 on 2024-03-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_post_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageURL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
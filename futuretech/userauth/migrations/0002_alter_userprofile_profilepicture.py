# Generated by Django 4.2.7 on 2023-12-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_alter_userprofile_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(default='images/logo.png', upload_to='images/'),
        ),
    ]
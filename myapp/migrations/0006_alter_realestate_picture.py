# Generated by Django 4.2.3 on 2023-07-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_realestate_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='picture',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-05 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_prict_realestate_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='picture',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
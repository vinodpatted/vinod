# Generated by Django 3.2 on 2021-05-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20210506_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'carmodel', 'verbose_name_plural': 'carmodel'},
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='submission_date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sujets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujet',
            name='id_sujet',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

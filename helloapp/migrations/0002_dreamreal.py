# Generated by Django 3.2.6 on 2021-09-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
    ]

# Generated by Django 3.2.14 on 2022-07-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]

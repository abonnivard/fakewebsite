# Generated by Django 4.2.5 on 2023-09-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Banque', models.CharField(max_length=30)),
            ],
        ),
    ]

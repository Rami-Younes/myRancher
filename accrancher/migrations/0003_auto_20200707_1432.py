# Generated by Django 2.2 on 2020-07-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accrancher', '0002_svaechkbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveChkbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stacknames', models.CharField(max_length=50)),
                ('usernames', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SvaeChkbox',
        ),
    ]

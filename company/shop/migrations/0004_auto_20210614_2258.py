# Generated by Django 3.2.4 on 2021-06-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='contct',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default=1)),
                ('email', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('check1', models.CharField(default='', max_length=5)),
                ('check2', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
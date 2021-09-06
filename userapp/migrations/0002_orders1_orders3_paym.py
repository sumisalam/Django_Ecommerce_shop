# Generated by Django 3.2.3 on 2021-07-07 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0017_auto_20210707_1455'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=100)),
                ('cardnumber', models.CharField(max_length=100)),
                ('subtotal', models.FloatField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
        migrations.CreateModel(
            name='orders3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='orders2')),
                ('product', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('pri', models.FloatField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
        migrations.CreateModel(
            name='orders1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='orders')),
                ('product', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('pri', models.FloatField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]
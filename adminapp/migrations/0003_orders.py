# Generated by Django 3.2.3 on 2021-06-19 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('adminapp', '0002_delete_carts'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('pri', models.FloatField()),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]

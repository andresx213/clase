# Generated by Django 3.0.8 on 2020-08-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricio', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='tienda',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.cliente'),
        ),
        migrations.AddField(
            model_name='tienda',
            name='cuotas',
            field=models.ManyToManyField(to='tienda.cuotas'),
        ),
    ]
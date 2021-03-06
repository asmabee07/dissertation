# Generated by Django 2.0.6 on 2018-08-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynutriguide', '0009_auto_20180804_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='BmiMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_in_g', models.FloatField()),
                ('height_in_meters', models.FloatField()),
                ('measured_at', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='completeprofile',
            name='bmi',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='completeprofile',
            name='height',
            field=models.FloatField(help_text='Required. Enter height in meter(m).'),
        ),
    ]

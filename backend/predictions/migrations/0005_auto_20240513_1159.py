# Generated by Django 3.2.25 on 2024-05-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0004_auto_20240511_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='Female',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Govt_job',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Male',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Not_married',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Private',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Rural',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Self_employed',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Unknown_smoke',
            field=models.FloatField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='predict',
            name='Urban',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='age',
            field=models.FloatField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='predict',
            name='avg_glucose_level',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='bmi',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='children',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='ever_married',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='formerly_smoked',
            field=models.FloatField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='predict',
            name='heart_disease',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='hypertension',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='never_smoked',
            field=models.FloatField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='predict',
            name='result',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='smokes',
            field=models.FloatField(blank=True, max_length=30),
        ),
    ]

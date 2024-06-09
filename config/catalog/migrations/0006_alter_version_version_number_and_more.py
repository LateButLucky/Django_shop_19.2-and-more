# Generated by Django 5.0.6 on 2024-06-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together={('product', 'version_number')},
        ),
    ]

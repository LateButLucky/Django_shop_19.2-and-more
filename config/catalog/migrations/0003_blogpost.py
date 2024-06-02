# Generated by Django 5.0.6 on 2024-06-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('preview_image', models.ImageField(upload_to='blog_previews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
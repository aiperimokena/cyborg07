# Generated by Django 5.1.6 on 2025-03-04 12:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='media/image_file', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Category')),
                ('images', models.ManyToManyField(to='main.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Product display',
                'verbose_name_plural': 'Products display',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('title', models.TextField(verbose_name='Text')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rate')),
                ('comment', models.TextField(max_length=200, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='RatingAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date change')),
                ('time_limit', models.DateTimeField(blank=True, null=True, verbose_name='Time limit')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rating', verbose_name='Rating reply')),
            ],
            options={
                'verbose_name': 'Reply to the comment',
                'verbose_name_plural': 'Replies to the comments',
            },
        ),
    ]

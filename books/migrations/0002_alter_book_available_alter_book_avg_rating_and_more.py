# Generated by Django 4.0.6 on 2022-07-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Availalbe'),
        ),
        migrations.AlterField(
            model_name='book',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Average Rating'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='images/', verbose_name='Book Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='ex. King of Scars', max_length=100, verbose_name='Book Title'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(help_text='eg. King of Scars', max_length=100, verbose_name='Book Title')),
                ('author', models.CharField(help_text='ex. Brandon Sanderson', max_length=50, verbose_name='Author Name')),
                ('genre', models.CharField(choices=[('General Fiction', 'General Fiction'), ('Historical Fiction', 'Historical Fiction'), ('Fantasy', 'Fantasy'), ('Science Fiction', 'Science Fiction'), ('Young Adult', 'Young Adult'), ('Memoir', 'Memoir'), ('History', 'History'), ('Biography', 'Biography')], max_length=30, verbose_name='Genre')),
                ('description', models.TextField()),
                ('avg_rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('brand', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Bag',
        ),
        migrations.DeleteModel(
            name='Belt',
        ),
        migrations.DeleteModel(
            name='Cap',
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
        migrations.DeleteModel(
            name='Watch',
        ),
    ]

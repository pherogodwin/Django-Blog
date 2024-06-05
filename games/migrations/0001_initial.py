# Generated by Django 5.0.1 on 2024-02-02 16:36

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
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('play_with_money', 'Play With Money'), ('play_for_free', 'Free Game')], default='play_with_money', max_length=100)),
                ('image', models.ImageField(upload_to='game_pics')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('review', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
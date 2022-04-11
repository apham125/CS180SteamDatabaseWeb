# Generated by Django 4.0.4 on 2022-04-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('dev', models.CharField(max_length=150, verbose_name='developer')),
                ('rel_date', models.DateField(auto_now=True, verbose_name='release_date')),
                ('publisher', models.CharField(max_length=150, verbose_name='publisher')),
                ('categories', models.CharField(max_length=255, verbose_name='categeories')),
                ('genre', models.CharField(max_length=150, verbose_name='genres')),
                ('pos_rate', models.BigIntegerField(verbose_name='positive_ratings')),
                ('neg_rate', models.BigIntegerField(verbose_name='negative_ratings')),
                ('avg_playtime', models.BigIntegerField(verbose_name='average_playtime')),
                ('median_playtime', models.BigIntegerField(verbose_name='median_playtime')),
                ('price', models.FloatField(verbose_name='price')),
            ],
        ),
    ]
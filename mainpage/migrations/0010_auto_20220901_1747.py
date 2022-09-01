# Generated by Django 3.2.14 on 2022-09-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_content_performance_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contact_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='contact_title',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='performance_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_title',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='content',
            name='team_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='team_title',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

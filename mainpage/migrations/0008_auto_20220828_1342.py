# Generated by Django 3.2.14 on 2022-08-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contact_subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='disclaimer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='performance_subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_card_content_3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='strategy_subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='team_subtitle',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customershowroompurchase',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customershowroompurchase',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customershowroompurchase',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

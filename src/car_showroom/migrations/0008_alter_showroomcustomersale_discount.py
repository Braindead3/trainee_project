# Generated by Django 4.0.7 on 2022-08-03 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0007_alter_dealershowroomsale_discount'),
        ('car_showroom', '0007_remove_carshowroom_unique_customers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroomcustomersale',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dealer.discount'),
        ),
    ]
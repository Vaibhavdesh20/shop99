# Generated by Django 4.2.5 on 2023-10-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='D7OJA46Q', max_length=20),
        ),
    ]

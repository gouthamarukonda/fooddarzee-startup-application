# Generated by Django 2.0.3 on 2018-04-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_startdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpgardePlanPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_days_initial', models.IntegerField()),
                ('num_days_extended_to', models.IntegerField()),
                ('price_diff', models.IntegerField()),
            ],
            options={
                'db_table': 'upgrade_plan_pricing',
                'managed': True,
            },
        ),
    ]

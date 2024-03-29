# Generated by Django 2.0.3 on 2018-04-17 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_auto_20180413_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referee_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='referee', to='management.UserProfile')),
                ('referer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='referer', to='management.UserProfile')),
            ],
            options={
                'managed': True,
                'db_table': 'referal',
            },
        ),
        migrations.AlterModelOptions(
            name='addon',
            options={'managed': False, 'verbose_name_plural': 'Add on products'},
        ),
        migrations.AlterField(
            model_name='activityfactor',
            name='activity',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

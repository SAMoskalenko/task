# Generated by Django 2.2.2 on 2019-07-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeRangeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(verbose_name='начало диапазона')),
                ('end_time', models.IntegerField(verbose_name='конец диапазона')),
            ],
        ),
        migrations.CreateModel(
            name='IntervalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField(verbose_name='интервал')),
            ],
        ),
        migrations.CreateModel(
            name='TimeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='время')),
                ('time_delta_minus', models.IntegerField(verbose_name='отрицательный допуск по времени')),
                ('time_delta_plus', models.IntegerField(verbose_name='положитьельный допуск по времени')),
            ],
        ),
        migrations.CreateModel(
            name='ValueData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='значение')),
                ('value_delta_minus', models.IntegerField(verbose_name='отрицательный допуск по значению')),
                ('value_delta_plus', models.IntegerField(verbose_name='положитьельный допуск по значению')),
            ],
        ),
        migrations.CreateModel(
            name='DotData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_after', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interval_after', to='dotsapp.IntervalData')),
                ('interval_before', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interval_before', to='dotsapp.IntervalData')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dotsapp.TimeData')),
                ('value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dotsapp.ValueData')),
            ],
        ),
        migrations.CreateModel(
            name='CommentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, verbose_name='комментарий')),
                ('dot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dotsapp.DotData')),
                ('free_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dotsapp.FreeRangeData')),
                ('interval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dotsapp.IntervalData')),
            ],
        ),
    ]

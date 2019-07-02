from django.db import models


class TimeData(models.Model):
    time = models.IntegerField(verbose_name='время')
    time_delta_minus = models.IntegerField(verbose_name='отрицательный допуск по времени')
    time_delta_plus = models.IntegerField(verbose_name='положитьельный допуск по времени')


class ValueData(models.Model):
    value = models.IntegerField(verbose_name='значение')
    value_delta_minus = models.IntegerField(verbose_name='отрицательный допуск по значению')
    value_delta_plus = models.IntegerField(verbose_name='положитьельный допуск по значению')


class IntervalData(models.Model):
    interval = models.IntegerField(verbose_name='интервал')


class FreeRangeData(models.Model):
    start_time = models.IntegerField(verbose_name='начало диапазона')
    end_time = models.IntegerField(verbose_name='конец диапазона')


class DotData(models.Model):
    time = models.ForeignKey(TimeData, on_delete=models.CASCADE, blank=True, null=True)
    value = models.ForeignKey(ValueData, on_delete=models.CASCADE, blank=True, null=True)
    interval_before = models.ForeignKey(IntervalData, related_name='interval_before', on_delete=models.CASCADE,
                                        blank=True, null=True)
    interval_after = models.ForeignKey(IntervalData, related_name='interval_after', on_delete=models.CASCADE,
                                       blank=True, null=True)


class CommentData(models.Model):
    comment = models.CharField(verbose_name='комментарий', max_length=500)
    interval = models.ForeignKey(IntervalData, on_delete=models.CASCADE, blank=True, null=True)
    dot = models.ForeignKey(DotData, on_delete=models.CASCADE, blank=True, null=True)
    free_range = models.ForeignKey(FreeRangeData, on_delete=models.CASCADE, blank=True, null=True)

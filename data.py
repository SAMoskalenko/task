import os
import sys
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('task/')
django.setup()

from dotsapp.models import *

with open("file.bin", "rb") as file:
    data = file.read(1000)

datastring = str(data)

print(datastring)
print(len(data))

time = []
value = []
interval = []
num = 1

for i in range(24, len(data) - 1):
    x = []
    int = []
    d = []
    if i % 2 == 0:
        x.append(data[i])
        x.append(data[20])
        x.append(data[21])
        time.append(x)
        if num == 1:
            int.append(0)
        else:
            int.append(data[i] - data[i - 2])
        interval.append(int)
        num += 1
    else:
        x.append(data[i])
        x.append(data[22])
        x.append(data[23])
        value.append(x)

time_data = ['time', 'time_delta_minus', 'time_delta_plus']
for el in time:
    TimeData.objects.create(**dict(zip(time_data, el)))

value_data = ['value', 'value_delta_minus', 'value_delta_plus']
for el in value:
    ValueData.objects.create(**dict(zip(value_data, el)))

interval_data = ['interval']
for el in interval:
    IntervalData.objects.create(**dict(zip(interval_data, el)))

for i in range(num - 2):
    time = TimeData.objects.all()[i]
    value = ValueData.objects.all()[i]
    interval_before = IntervalData.objects.all()[i]
    interval_after = IntervalData.objects.all()[i + 1]
    if i == num - 2:
        dot = DotData(time=time,
                      value=value,
                      interval_before=interval_before,
                      interval_after=None)
    else:
        dot = DotData(time=time,
                      value=value,
                      interval_before=interval_before,
                      interval_after=interval_after)
    dot.save()

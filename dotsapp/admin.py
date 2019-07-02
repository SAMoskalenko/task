from django.contrib import admin

from dotsapp.models import *

admin.site.register(TimeData)
admin.site.register(ValueData)
admin.site.register(IntervalData)
admin.site.register(DotData)
admin.site.register(FreeRangeData)
admin.site.register(CommentData)
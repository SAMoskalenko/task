from rest_framework import serializers

from dotsapp.models import *


class TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeData
        fields = ['id', 'time', 'time_delta_minus', 'time_delta_plus']
        read_only_fields = ('id',)


class ValueDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueData
        fields = ['id', 'value', 'value_delta_minus', 'value_delta_plus']
        read_only_fields = ('id',)


class IntervalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalData
        fields = ['id', 'interval']
        read_only_fields = ('id',)

class FreeRangeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeRangeData
        fields = ['id', 'start_time', 'end_time']
        read_only_fields = ('id',)

class CommentDataSerializer(serializers.ModelSerializer):
    free_range = FreeRangeDataSerializer()

    class Meta:
        model = CommentData
        fields = ['id', 'comment', 'interval', 'dot', 'free_range']
        read_only_fields = ('id',)

    def create(self, validated_data):
        f_r = validated_data.pop('free_range')
        start_time = f_r['start_time']
        end_time = f_r['end_time']
        comment = validated_data.pop('comment')
        free_range = FreeRangeData.objects.create(start_time=start_time, end_time=end_time)
        comment_item = CommentData(free_range=free_range, comment=comment)
        comment_item.save()
        return comment_item

class DotDataSerializer(serializers.ModelSerializer):
    time = TimeDataSerializer()
    value = ValueDataSerializer()
    interval_before = IntervalDataSerializer()
    interval_after = IntervalDataSerializer()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = DotData
        fields = ['id', 'time', 'value', 'interval_before', 'interval_after', 'comment']
        read_only_fields = ('id',)

    def get_comment(self, obj):
        com = list(CommentData.objects.all().values('dot__id'))
        co = []
        for n in com:
            co.append(n['dot__id'])
        i = obj.id
        if i in co:
            comment = CommentData.objects.get(dot__id=i)
            c = comment.comment
            if c:
                return c
        else:
            return None





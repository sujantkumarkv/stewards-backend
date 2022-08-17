from .models import Steward, WorkStream, Stats
from rest_framework import serializers


class LoginRequestSerializer(serializers.Serializer):
    address = serializers.CharField(
        max_length=200)  # TODO: replace with a real validator
    signed = serializers.CharField(
        max_length=200)  # TODO: replace with a real validator


class StewardSerializer(serializers.ModelSerializer):

    address = serializers.SerializerMethodField('get_address')
    workstream = serializers.SerializerMethodField('get_workstream')

    def get_workstream(self, steward):
        return steward.workstream.short_name

    def get_address(self, steward):
        return steward.user.username

    class Meta:
        model = Steward
        exclude = ('id', 'user')

        read_only_fields = [
            'id',
            'name',
            'steward_since',
            'gitcoin_username',
            'discourse_username',
            'username',
        ]


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        exclude = ('id', )
        files = ['gtc_balance']


class WorkStreamSerializer(serializers.ModelSerializer):
    stats = StatsSerializer(read_only=True)

    class Meta:
        model = WorkStream
        exclude = ('id', )

        read_only_fields = [
            'current_gtc_graph', 'current_gtc_num', 'current_stable_num',
            'current_stable_graph', 'all_time_contributors', 'stats'
        ]

    # TODO: Add Method Field to give leads

from models import BroadlinkDevice, BroadlinkCommand
from rest_framework import serializers


class BroadlinkDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BroadlinkDevice
        fields = ('ip', 'port', 'name', 'description', 'model', 'mac')


class BroadlinkCommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BroadlinkCommand
        fields = ('name', 'description', 'command')

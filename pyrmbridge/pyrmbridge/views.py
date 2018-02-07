from rest_framework import viewsets
from serializers import BroadlinkDeviceSerializer, BroadlinkCommandSerializer
from rest_framework.decorators import api_view
from models import BroadlinkDevice, BroadlinkCommand
from bridge_commands import available_commands


class BroadlinkDeviceViewSet(viewsets.ModelViewSet):
    queryset = BroadlinkDevice.objects.all().order_by('-id')
    serializer_class = BroadlinkDeviceSerializer


class BroadlinkCommandViewSet(viewsets.ModelViewSet):
    queryset = BroadlinkCommand.objects.all().order_by('-id')
    serializer_class = BroadlinkCommandSerializer


def string_to_broadlink_command(command):
    return bytearray([int(command.strip()[i:i+2], 16) for i in range(0, len(command.strip()), 2)])


@api_view(['POST'])
def view(request):
    return available_commands[unicode(request.data['command'])](request.data)

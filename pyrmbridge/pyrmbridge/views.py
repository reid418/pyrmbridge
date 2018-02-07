from rest_framework import viewsets
from serializers import BroadlinkDeviceSerializer, BroadlinkCommandSerializer
from models import BroadlinkDevice, BroadlinkCommand
import broadlink
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    target_device = BroadlinkDevice.objects.get(name=request.data.get('target_device_name'))
    device = broadlink.rm(host=(target_device.ip, target_device.port), mac=str(target_device.mac))
    print (target_device.ip, target_device.port)
    print target_device.mac
    device.auth()
    if request.data['command'] == u"send_code":
        print device.send_data(string_to_broadlink_command(request.data['data']))
    if request.data['command'] == u"send_command":
        print device.send_data(string_to_broadlink_command(BroadlinkCommand.objects.get(name=request.data['data']).command))
    else:
        raise Exception('unknown')
    return Response({"message": "Hello for today! See you tomorrow!"})
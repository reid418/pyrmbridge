import broadlink
from models import BroadlinkDevice, BroadlinkCommand
from rest_framework.response import Response

available_commands = {}


def register_command(command, supported_methods=None):
    print command
    print supported_methods

    def _(func):
        def __(*args, **kwargs):
            return func(*args, **kwargs)

        available_commands[command] = __
        return __
    return _


def string_to_broadlink_command(command):
    return bytearray([int(command.strip()[i:i+2], 16) for i in range(0, len(command.strip()), 2)])


@register_command("send_code", ['POST'])
def send_code(data):
    target_device = BroadlinkDevice.objects.get(name=data.get('target_device_name'))
    device = broadlink.rm(host=(target_device.ip, target_device.port), mac=str(target_device.mac))
    device.auth()
    device.send_data(string_to_broadlink_command(data['data']))


@register_command("send_command", ['POST'])
def send_command(data):
    target_device = BroadlinkDevice.objects.get(name=data.get('target_device_name'))
    device = broadlink.rm(host=(target_device.ip, target_device.port), mac=str(target_device.mac))
    device.auth()
    print device.send_data(string_to_broadlink_command(str(BroadlinkCommand.objects.get(name=data['data']).command)))
    return Response({"code": 0, "msg": "rm2 send data success"})


@register_command("send_commands", ['POST'])
def send_command(data):
    target_device = BroadlinkDevice.objects.get(name=data.get('target_device_name'))
    device = broadlink.rm(host=(target_device.ip, target_device.port), mac=str(target_device.mac))
    device.auth()
    for command in data['data']:
        print device.send_data(string_to_broadlink_command(str(BroadlinkCommand.objects.get(name=command).command)))
    return Response({"code": 0, "msg": "rm2 send data success"})

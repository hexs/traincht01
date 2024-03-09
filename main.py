import os


class Computer:
    def __init__(self, device_name, ipv4, gateway, subnet='255.255.255.0'):
        self.device_name = device_name
        self.ipv4 = ipv4
        self.subnet = subnet
        self.gateway = gateway
        self.path = fr'\\{device_name}\PythonProjects'

    def listdir(self):
        return os.listdir(self.path)


c1 = Computer('N-PCD236570', '192.168.125.163', '192.168.125.254')
print(c1.listdir())

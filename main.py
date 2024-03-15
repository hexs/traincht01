import os


class Computer:
    username = 'dx'
    password = 'io90-0==='

    def __init__(self, device_name, ipv4, gateway, subnet='255.255.255.0', network_device='wifi'):
        self.device_name = device_name
        self.ipv4 = ipv4
        self.subnet = subnet
        self.gateway = gateway
        self.network_device = network_device
        self.path = fr'\\{device_name}\PythonProjects'

    def listdir(self, p=''):
        return os.listdir(os.path.join(self.path, p))


c1 = Computer('N-PCD236570', '192.168.125.163', '192.168.125.254')
c2 = Computer('N-PCD236548', '192.168.125.112', '192.168.125.254')
c3 = Computer('N-PCD236547', '192.168.125.110', '192.168.125.254')

print(c3.listdir())
print(c3.listdir('PythonTutorial'))

from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'my_session.txt',
}   
nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'my_session2.txt',
}

net_connect = ConnectHandler(**nxos1)
print(net_connect.find_prompt())

print(net_connect.send_command('show version'))

#!usr/bin/env python
import subprocess
import optparse


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] your mac is successfully changed to "+new_mac)


def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="enter interface  name here")
    parser.add_option("-m", "--mac", dest="new_mac", help="enter new mac here")
    (value, args) = parser.parse_args()
    if not value.interface:
        parser.error("please specify the interface use --help to see the help")
    elif not value.new_mac:
        parser.error("please specify the mac use --help to see the help")
    return value


options = arguments()
change_mac(options.interface, options.new_mac)









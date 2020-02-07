#! /usr/bin/env python3

#program:mac address changer 
#@Author : 5hifaT
#github:www.github.com/mh-shifat
#Date:7 Feb, 2020
#distro : Debian

import subprocess as sp 
import optparse as op

def get_arguments():
    parser = op.OptionParser();
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="The new MAC address")
    
    (options,arguments) = parser.parse_args()

    if not options.interface :
        parser.error("[-] please specify an interface , use --help for more info")
    elif not options.new_mac :
        parser.error("[-] please specify a MAC address , use --help for more info")
    return options


def change_mac(interface,new_mac):
    ifconfig = "/sbin/ifconfig"
    interface_down = [ifconfig , interface , "down"]
    interface_up = [ifconfig , interface , "up"]
    mac_change = [ifconfig, interface ,"hw","ether", new_mac]

    print("[+] changing MAC address for "+ interface+ " ......\n")

    sp.call(interface_down) 
    sp.call(mac_change) 
    sp.call(interface_up)
    
    print("Mac address has changed to " + new_mac)
    

def error_check():
    ifconfig = "/sbin/ifconfig"
    ifconfig_not_found = "bash: /sbin/ifconfig: No such file or directory"
    
    try:
        sp.check_output(ifconfig)
    except OSError as error:
        print("Net-tools is not installed.\n\n")
        try:
            print("[+] installing net-tools ....\n\n")
            sp.check_output("sudo apt-get install net-tools",shell=True)
            print("net-tools installed successfully\n")
        except OSError as err:
            print("Try  to install net-tools manually for your operating system")
            exit

options = get_arguments()
error_check()
change_mac(options.interface,options.new_mac)


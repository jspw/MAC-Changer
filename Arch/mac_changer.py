#! /usr/bin/env python3

#program:mac address changer 
#@Author : 5hifaT
#github:https://github.com/mh-shifat/MAC-Changer
#Date:7 Feb, 2020
#distro : Debian

import subprocess as sp 
import optparse as op
import re

def show_interfaces():
    print("Displaying Available Network Interfaces :\n")
    avl_if = sp.check_output("ls /sys/class/net",shell=True,universal_newlines=True)
    print(avl_if)
    

def get_arguments():
    parser = op.OptionParser();
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="The new MAC address")
    parser.add_option("-s","--show_interfaces",dest="show_interfaces",help="Use '-s show' to see the available interfaces")
    
    (options,arguments) = parser.parse_args()

    if  options.show_interfaces == "show":
        show_interfaces();
        return False
        
    else :
        if not options.interface :
            parser.error("[-] please specify an interface\nor\nuse '-s show' to  see the available interfaces or use --help for more info")

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
    
    ifconfig_result = sp.check_output([ifconfig,interface],universal_newlines=True)
    mac_search = re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result)
    
    if mac_search.group(0) == new_mac :
        print("Mac address has changed to " + new_mac + " successfully")
    else :
        print("MAC address can't be chnaged, try again")
    

def error_check():
    ifconfig = "/sbin/ifconfig"
    ifconfig_not_found = "bash: /sbin/ifconfig: No such file or directory"
    
    try:
        sp.check_output(ifconfig)
    except OSError as error:
        print("Net-tools is not installed.\n\n")
        try:
            print("[+] installing net-tools ....\n\n")
            sp.check_output("sudo pacman -S net-tools",shell=True)
            print("net-tools installed successfully\n")
        except OSError as err:
            print("Try  to install net-tools manually for your operating system")
            exit
            
if(get_arguments()):
    options = get_arguments()
    error_check()
    change_mac(options.interface,options.new_mac)
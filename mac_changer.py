#! /usr/bin/env python3

#program:mac address changer 
#@Author : 5hifaT
#github:www.github.com/mh-shifat
#Date:7 Feb, 2020

import subprocess as sp 
import optparse as op

def get_arguments():
    parser = op.OptionParser();
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its mac address")
    parser.add_option("-m","--mac",dest="new_mac",help="The new mac address")
    
    (options,arguments) = parser.parse_args()

    if not options.interface :
        parser.error("[-] please specify an interface , use --help for more info")
    elif not options.new_mac :
        parser.error("[-] please specify an mac address , use --help for more info")
    return options



def change_mac(interface,new_mac):
    ifconfig = "/sbin/ifconfig"
    interface_down = [ifconfig , interface , "down"]
    interface_up = [ifconfig , interface , "up"]
    mac_change = [ifconfig, interface ,"hw","ether", new_mac]

    print("[+] changing mac address for "+ interface+ " ......\n")

    sp.call(interface_down) 
    sp.call(mac_change) 
    sp.call(interface_up)
    
    print("Mac address changed to " + new_mac)
    

options = get_arguments()
change_mac(options.interface,options.new_mac)

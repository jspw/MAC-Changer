# MAC-Changer
A simple script to change mac address using python

## Usage :
install python3 : `sudo apt-get install python3` <br>
run app :`sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55`<br>
to see more :`python3 mac_changer.py -h`


### Change MAC address menually in command line :<br>
**Check interface :** `/sbin/ifconfig` <br>
**eth0 down :** `/sbin/ifconfig eth0 down` <br>
**Change address :** `/sbin/ifconfig eth0 hw ether 00:11:22:33:44:55` <br>
**eth0 up :** `/sbin/ifconfig eth0 up` <br>

###### **for old distro use : `ifconfig` instade of `/sbin/ifconfig` <br>**

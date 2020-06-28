# MAC-Changer
A simple script written in python to change **MAC Address** for **Linux** based Operating Systems.

- [Debian](/Debian/mac_changer.py)
- [Arch](/Arch/mac_changer.py)
- [CentOS](/CentOS/mac_changer.py)
- [SUSE](/Suse/mac_changer.py)

## Usage :
- Show Network Interfaces :

        sudo python  mac_changer.py -s show

- Change MAC Address :

        sudo python mac_changer.py -i interface_name -m new_mac_address


- To see more :

        `python3 mac_changer.py -h`

    ![Help SS](/images/help.png)

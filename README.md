# Raspberry-Pi-DHCP-Finder


Add new file to Raspberry Pi SD Card (boot partition/folder)


file: wpa_supplicant.conf


Add the following lines:


      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
      update_config=1
      
      network={
            id_str="WIFIALIAS1"
            ssid="WIFINAME1"
            scan_ssid=1
            psk="WIFIPASS1"
            key_mgmt=WPA-PSK
      }
      
      network={
            id_str="WIFIALIAS2"
            ssid="WIFINAME2"
            scan_ssid=1
            psk="WIFIPASS2"
            key_mgmt=WPA-PSK
      }
      
      
Then, make the script run on boot:


$ sudo nano /etc/rc.local


Add before the "exit 0" line


python /home/pi/Downloads/rasp-dhcp-finder.py &


(Change the file path accordingly)


Boot your Pi and use the App to find its IP Address.


-- playstore app link placeholder --

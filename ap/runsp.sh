hostapd -B /etc/sink-ap/hostapd.conf

ip addr flush wlan0
ip addr add 192.168.1.1/24 broadcast 192.168.1.0 dev wlan0
ip link set wlan0 up

dhcpd -q -d -cf /etc/sink-ap/dhcpd.conf wlan0

start()
{
    hostapd -B /etc/sink/hostapd.conf
    ip addr add 192.168.1.1/24 broadcast 192.168.1.0 dev wlan0
    dhcpd -cf /etc/sink/dhcpd.conf wlan0
    /etc/sink/enviroment/bin/python /etc/sink/webservice/run.py
}

stop()
{
    kill $(pidof hostapd)
    kill $(pidof wpa_supplicant)
    kill $(pidof dhcpd)
    ip addr flush wlan0
}

case "$1" in
    init)
	stop
	start
	;;
    start)
	start
	;;
    stop)
	stop
	;;
    *)
	echo "Default"
	;;
esac



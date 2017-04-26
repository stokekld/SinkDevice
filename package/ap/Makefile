C=dpkg-deb --build
PROJECT=sink-ap
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)

all: $(PACKAGE)

$(PACKAGE):
	mkdir -p $(PACKAGE)/DEBIAN
	mkdir -p $(PACKAGE)/etc/$(PROJECT)
	mkdir -p $(PACKAGE)/etc/systemd/system/
	cp control $(PACKAGE)/DEBIAN
	cp -r ../../ap/dhcpd.conf $(PACKAGE)/etc/$(PROJECT)
	cp -r ../../ap/hostapd.conf $(PACKAGE)/etc/$(PROJECT)
	cp -r ../../ap/runsp.sh $(PACKAGE)/etc/$(PROJECT)
	cp -r ../../ap/sinkap.service $(PACKAGE)/etc/systemd/system/

	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)

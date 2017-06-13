C=dpkg-deb --build
PROJECT=sink
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)
DEBIAN_DIR=$(PACKAGE)/DEBIAN
PROJECT_DIR=$(PACKAGE)/etc/$(PROJECT)
WEBSERVICE_DIR=$(PACKAGE)/etc/$(PROJECT)/webservice


all: $(PACKAGE)

$(PACKAGE):
	mkdir -p $(DEBIAN_DIR)
	mkdir -p $(PROJECT_DIR)
	mkdir -p $(WEBSERVICE_DIR)
	cp control $(DEBIAN_DIR)
	cp ../../ap/dhcpd.conf $(PROJECT_DIR)
	cp ../../ap/hostapd.conf $(PROJECT_DIR)
	cp -rv ../../webservice/source/* $(WEBSERVICE_DIR)
	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)

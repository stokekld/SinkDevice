C=dpkg-deb --build
PROJECT=sink-webservice
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)

all: $(PACKAGE)

$(PACKAGE):
	mkdir -p $(PACKAGE)/DEBIAN
	cp control $(PACKAGE)/DEBIAN
	mkdir -p $(PACKAGE)/etc/$(PROJECT)
	cp -r ../../webservice/source/* $(PACKAGE)/etc/$(PROJECT)
	mkdir -p $(PACKAGE)/lib/systemd/system/
	cp ../../webservice/scripts/websink.service $(PACKAGE)/lib/systemd/system/
	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)

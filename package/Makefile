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
	cp -r ../webservice/* $(PACKAGE)/etc/$(PROJECT)
	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)

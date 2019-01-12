# Modified from https://github.com/pop-os/system76-power/

prefix ?= ~/.local
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin

.PHONY: install uninstall test

BIN=vitals

install:
	install -D -m 04755 "src/$(BIN).py" $(DESTDIR)$(bindir)/$(BIN)

uninstall:
	rm -f $(DESTDIR)$(bindir)/$(BIN)

test:
	python3 src/test_vitals.py

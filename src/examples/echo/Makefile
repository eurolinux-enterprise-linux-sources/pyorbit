ORBIT2_CFLAGS=`pkg-config --cflags ORBit-2.0`
ORBIT2_LIBS=`pkg-config --libs ORBit-2.0`

all: echo_module.la

%.lo: %.c
	libtool --mode=compile gcc $(ORBIT2_CFLAGS) -c $<

echo_module.la: echo-imodule.lo
	libtool --mode=link  gcc $(ORBIT2_LIBS) -o $@ $< -rpath `pwd`\
		-export-dynamic -module -avoid-version

idlgen = echo-imodule.c echo-common.c echo.h

echo-imodule.c: echo.idl
	orbit-idl-2 --add-imodule --noskels --nostubs $<

clean:
	-libtool --mode=clean rm -rf *.lo *.la $(idlgen)

install: echo_module.la
	libtool --mode=install install echo_module.la\
		`pkg-config --variable=libdir ORBit-2.0`/orbit-2.0

## Makefile.am for cert file meta info plugin

# set the include path for X, qt and KDE
INCLUDES         = $(all_includes)

# these are the headers for your project
noinst_HEADERS   = kfile_cert.h

kde_module_LTLIBRARIES = kfile_cert.la

kfile_cert_la_SOURCES = kfile_cert.cpp
kfile_cert_la_LDFLAGS = $(all_libraries) -module $(KDE_PLUGIN)
kfile_cert_la_LIBADD = $(LIB_KSYCOCA)

# let automoc handle all of the meta source files (moc)
METASOURCES = AUTO

messages: rc.cpp
	$(XGETTEXT) kfile_cert.cpp -o $(podir)/kfile_cert.pot

services_DATA = kfile_cert.desktop
servicesdir = $(kde_servicesdir)

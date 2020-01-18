# -*- mode: rpm-spec -*-
%define python python2

Summary: Python bindings for ORBit2.
Name: pyorbit
Version: 2.24.0
Release: 1
Copyright: LGPL
Group: Development/Languages
Source: pyorbit-%{version}.tar.gz
BuildRoot: /var/tmp/pyorbit-root
Requires: ORBit2 >= 2.12
Requires: %{python} >= 2.2
Obsoletes: orbit-python = 1.99.0
Buildrequires: %{python}-devel >= 2.2
Buildrequires: ORBit2-devel >= 2.12

%description
pyorbit is an extension module for python that provides a Python
language mapping for the ORBit2 CORBA ORB.

%package devel
Summary: Files needed to build wrappers for pyorbit addon libraries.
Group: Development/Languages
Requires: ORBit2-devel >= 2.12

%description devel
This package contains files required to build extensions that
interoperate with pyorbit.

%changelog
* Tue Nov 12 2002  James Henstridge  <james@daa.com.au>
- initial spec file based on orbit-python's one.

%prep
%setup -q
./configure --prefix=%{_prefix}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(755, root, root, 755)
%{_prefix}/lib/python?.?/site-packages/*.so
%{_prefix}/lib/python?.?/site-packages/*.py*

%doc AUTHORS NEWS README TODO ChangeLog
#%doc tests

%files devel
%defattr(755, root, root, 755)
%{_includedir}/pyorbit-2/*.h
%{_prefix}/lib/pkgconfig/pyorbit-2.pc

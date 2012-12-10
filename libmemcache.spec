%define	major 0
%define libname %mklibname memcache %{major}
%define develname %mklibname memcache -d

Summary:	A high performance C API for memcached
Name:		libmemcache
Version:	1.4.0
Release:	0.rc2.8
Group:		System/Libraries
License:	BSD-like
URL:		http://people.freebsd.org/~seanc/libmemcache/
Source0:	http://people.freebsd.org/~seanc/libmemcache/%{name}-%{version}.rc2.tar.bz2
Patch0:		libmemcache-1.4.0.rc2_gnusource.patch
Patch1:		libmemcache-1.4.0.rc2_gcc43_inline.patch
Patch2:		libmemcache-1.4.0.rc2_preserve_cflags.patch
BuildRequires:	libtool
BuildRequires:	autoconf2.5

%description
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system. 

%package -n	%{libname}
Summary:	A high performance C API library for memcached
Group:          System/Libraries

%description -n	%{libname}
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system. 

%package -n	%{develname}
Summary:	Static library and header files for the libmemcache library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Provides:	memcache-devel = %{EVRD}
Obsoletes:	memcache-devel
Obsoletes:	%{mklibname memcache 0 -d}
Obsoletes:	%{mklibname memcache 1 -d}

%description -n	%{develname}
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system. 

This package contains the static libmemcache library and its
header files.

%prep

%setup -q -n %{name}-%{version}.rc2
%patch0
%patch1
%patch2

%build
touch NEWS README AUTHORS
autoreconf -fis
export STRIP="/bin/true"

%configure2_5x

%make

# this needs some freebsd stuff to work (cough...)
#make test

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING ChangeLog INSTALL
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc2.7mdv2011.0
+ Revision: 620151
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0-0.rc2.6mdv2010.0
+ Revision: 429809
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc2.5mdv2009.0
+ Revision: 229677
- added 3 patches from opensuse to make it compile

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-0.rc2.4mdv2008.0
+ Revision: 89839
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc2.3mdv2008.0
+ Revision: 83525
- new devel naming


* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc2.2mdv2007.0
+ Revision: 75442
- fix deps
- Import libmemcache

* Thu Apr 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc2.1mdk
- 1.4.0.rc2
- fix deps

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0-0.b9.1mdk
- 1.4.0.b9

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3

* Sun Jan 23 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.2-1mdk
- initial Mandrakelinux package


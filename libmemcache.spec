%define	major 0
%define libname %mklibname memcache %{major}
%define develname %mklibname memcache -d

Summary:	A high performance C API for memcached
Name:		libmemcache
Version:	1.4.0
Release:	1.rc2.8
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


%define	major 0
%define libname %mklibname memcache %{major}
%define develname %mklibname memcache -d

Summary:	A high performance C API for memcached
Name:		libmemcache
Version:	1.4.0
Release:	%mkrel 0.rc2.4
Group:		System/Libraries
License:	BSD-like
URL:		http://people.freebsd.org/~seanc/libmemcache/
Source0:	http://people.freebsd.org/~seanc/libmemcache/%{name}-%{version}.rc2.tar.bz2
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Provides:	%{name}-devel = %{version}-%{release}
Provides:	memcache-devel = %{version}-%{release}
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

%build

%configure2_5x

%make

# this needs some freebsd stuff to work (cough...)
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog INSTALL
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

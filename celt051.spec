Name:           celt051
Version:        0.5.1.3
Release:        0%{?dist}
Summary:        An audio codec for use in low-delay speech and audio communication

Group:          System Environment/Libraries
License:        BSD
# Files without license header are confirmed to be BSD. Will be fixed in later release
# http://lists.xiph.org/pipermail/celt-dev/2009-February/000063.html
URL:            http://www.celt-codec.org/
Source0:        http://downloads.us.xiph.org/releases/celt/celt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libogg-devel

%description
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio 
codec designed for realtime transmission of high quality speech and audio. 
This is meant to close the gap between traditional speech codecs 
(such as Speex) and traditional audio codecs (such as Vorbis). 

%package devel
Summary: Development package for celt
Group: Development/Libraries
Requires: libogg-devel
Requires: celt051 = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with celt.

%prep
%setup -q -n celt-%{version}

%build
%configure
# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libcelt051.a
rm $RPM_BUILD_ROOT%{_libdir}/libcelt051.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%{_bindir}/celtenc051
%{_bindir}/celtdec051
%{_libdir}/libcelt051.so.0
%{_libdir}/libcelt051.so.0.0.0

%files devel
%defattr(-,root,root,-)
%doc COPYING README
%{_includedir}/celt051
%{_libdir}/pkgconfig/celt051.pc
%{_libdir}/libcelt051.so

%changelog
* Tue May 12 2009 Monty <cmontgom@redhat.com> 0.5.1.3-0
- Rebase from upstream to pull in crash bugfixes
- Resolves: bz#488571  -  Add celt051 package

* Fri Apr 24 2009 Monty <cmontgom@redhat.com> 0.5.1.2-0
- Rebase from upstream to pull in versioning changes and .pc.in fix
- Bring inline with REVH package
- Resolves: bz#488571  -  Add celt051 package

* Wed Apr 22 2009 Monty <cmontgom@redhat.com> 0.5.1-5
- Update to reversioned upstream package

* Thu Feb 12 2009 Monty <cmontgom@redhat.com> 0.5.1-3
- Bump release for move from EPEL to RHEL

* Mon Feb 2 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.1-2
- Updates for package review

* Mon Jan 5 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.1-1
- Initial package

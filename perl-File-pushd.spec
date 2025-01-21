#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-File-pushd
Version  : 1.016
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-1.016.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-1.016.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-pushd-perl/libfile-pushd-perl_1.016-1.debian.tar.xz
Summary  : 'change directory temporarily for a limited scope'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-File-pushd-license = %{version}-%{release}
Requires: perl-File-pushd-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
File::pushd - change directory temporarily for a limited scope
VERSION
version 1.016

%package dev
Summary: dev components for the perl-File-pushd package.
Group: Development
Provides: perl-File-pushd-devel = %{version}-%{release}
Requires: perl-File-pushd = %{version}-%{release}

%description dev
dev components for the perl-File-pushd package.


%package license
Summary: license components for the perl-File-pushd package.
Group: Default

%description license
license components for the perl-File-pushd package.


%package perl
Summary: perl components for the perl-File-pushd package.
Group: Default
Requires: perl-File-pushd = %{version}-%{release}

%description perl
perl components for the perl-File-pushd package.


%prep
%setup -q -n File-pushd-1.016
cd %{_builddir}
tar xf %{_sourcedir}/libfile-pushd-perl_1.016-1.debian.tar.xz
cd %{_builddir}/File-pushd-1.016
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-pushd-1.016/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-pushd
cp %{_builddir}/File-pushd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-pushd/ac60cc1d2dd9088405a5dcfa94b5ac608e5bc096 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-pushd/ff7be4ca9dfdd6f07fa60fa70513682311ed8542 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::pushd.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-pushd/ac60cc1d2dd9088405a5dcfa94b5ac608e5bc096
/usr/share/package-licenses/perl-File-pushd/ff7be4ca9dfdd6f07fa60fa70513682311ed8542

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

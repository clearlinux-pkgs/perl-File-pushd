#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-pushd
Version  : 1.016
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-1.016.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-1.016.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-pushd-perl/libfile-pushd-perl_1.016-1.debian.tar.xz
Summary  : Change directory temporarily for a limited scope
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-File-pushd-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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


%prep
%setup -q -n File-pushd-1.016
cd ..
%setup -q -T -D -n File-pushd-1.016 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-pushd-1.016/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-pushd
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-pushd/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-pushd/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/File/pushd.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::pushd.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-pushd/LICENSE
/usr/share/package-licenses/perl-File-pushd/deblicense_copyright

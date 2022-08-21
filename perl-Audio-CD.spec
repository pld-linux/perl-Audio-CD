%define		pdir	Audio
%define		pnam	CD
Summary:	Perl interface to libcdaudio
Summary(pl.UTF-8):	Interfejs Perla do libcdaudio
Name:		perl-Audio-CD
Version:	0.04
Release:	21
Epoch:		1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# newer version distribution is restricted
#Source0:	http://homepages.cwi.nl/~jvhemert/files/Audio-CD-0.05.tar.gz
# Source0-md5:	5b3051fd01a36c557a54e83ac0bde567
URL:		http://search.cpan.org/dist/Audio-CD/
BuildRequires:	libcdaudio-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to libcdaudio.

%description -l pl.UTF-8
Interfejs Perla do libcdaudio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Audio/CD.pm
%dir %{perl_vendorarch}/auto/Audio/CD
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/CD/CD.so

%{_mandir}/man3/*

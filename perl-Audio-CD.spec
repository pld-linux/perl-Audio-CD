%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	CD
Summary:	Perl interface to libcdaudio
Summary(pl):	Interfejs perla do libcdaudio
Name:		perl-Audio-CD
Version:	0.04
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libcdaudio-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to libcdaudio.

%description -l pl
Interfejs perla do libcdaudio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Audio/CD.pm
%dir %{perl_vendorarch}/auto/Audio/CD
%{perl_vendorarch}/auto/Audio/CD/CD.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/CD/CD.so

%{_mandir}/man3/*

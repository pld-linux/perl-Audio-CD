%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to libcdaudio
Summary(pl):	Interfejs perla do libcdaudio
Name:		perl-Audio-CD
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Audio/Audio-CD-0.04.tar.gz
BuildRequires:	libcdaudio-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to libcdaudio.

%description -l pl
Interfejs perla do libcdaudio.

%prep
%setup -q -n Audio-CD-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

%dir %{perl_sitearch}/Audio
%{perl_sitearch}/Audio/CD.pm

%dir %{perl_sitearch}/auto/Audio
%dir %{perl_sitearch}/auto/Audio/CD
%{perl_sitearch}/auto/Audio/CD/CD.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/CD/CD.so

%{_mandir}/man3/*

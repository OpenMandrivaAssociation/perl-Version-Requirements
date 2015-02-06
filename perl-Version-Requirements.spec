%define upstream_name    Version-Requirements
%define upstream_version 0.101020

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A set of version requirements for a CPAN dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Version/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
A Version::Requirements object models a set of version constraints like
those specified in the _META.yml_ or _META.json_ files in CPAN
distributions. It can be built up by adding more and more constraints, and
it will reduce them to the simplest representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.101.20-2mdv2011.0
+ Revision: 654342
- rebuild for updated spec-helper

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.20-1mdv2011.0
+ Revision: 536215
- update to 0.101020

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.660-1mdv2010.1
+ Revision: 515667
- update to 0.100660

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.630-1mdv2010.1
+ Revision: 514402
- update to 0.100630

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.530-1mdv2010.1
+ Revision: 510098
- import perl-Version-Requirements


* Tue Feb 23 2010 cpan2dist 0.100530-1mdv
- initial mdv release, generated with cpan2dist

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Units
Summary:	Convert::Units::* - objects for performing unit conversions
Summary(pl):	Convert::Units::* - obiekty do przeliczania jednostek
Name:		perl-Convert-Units
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fa0ccd591bac873b8d0f32771699b3d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Units package is a collection of modules for parsing strings with
unit measurements (such as "12pt" or "3 meters") and converting them
to some other unit (such as "picas" or "inches").

It uses a base package (Units::Base) which does the dirty work. Other
modules define what units they handle and how they are related.

%description -l pl
Pakiet Units to zbiór modu³ów do przetwarzania ³añcuchów zawieraj±cych
jednostki miar (takich jak "12pt" czy "3 meters") i konwertuj±cych je
do innych jednostek (takich jak "picas" czy "inches").

Pakiet u¿ywa podstawowego modu³u (Units::Base), który wykonuje
w³a¶ciw± robotê. Inne modu³y definiuj± które jednostki mog± obs³u¿yæ i
jak s± miêdzy sob± powi±zane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Convert/Units
%{_mandir}/man3/*

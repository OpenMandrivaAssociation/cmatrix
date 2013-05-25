######################################################
# SpecFile: cmatrix.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
# Build for Stella-6.4
#####################################################
#empty debug
%define debug_package	%{nil}
%define name    cmatrix
%define version     1.2a
%define release 1
Summary:	CMatrix simulates the display from "The Matrix"
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Applications/Terminal
License:	GNU General Public License (GPL)
URL:		http://www.asty.org/cmatrix/
Source0:	http://www.asty.org/cmatrix/dist/cmatrix-%{version}.tar.gz
Patch0:         cmatrix-%{version}-makefile.patch
Patch1:         cmatrix-no-TIME-DATE.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  kbd
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


	
%description
CMatrix is based on the screensaver from The Matrix website. It works
with terminal settings up to 132x300 and can scroll lines all at the same
rate or asynchronously and at a user-defined speed.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
aclocal
autoconf
automake -a
%configure
make

%install
mkdir -p $RPM_BUILD_ROOT%{fontdir}
mkdir -p $RPM_BUILD_ROOT/lib/kbd/consolefonts
make DESTDIR=$RPM_BUILD_ROOT install
install -m644 mtx.pcf $RPM_BUILD_ROOT%{fontdir}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_mandir}/man1/*
%{_bindir}/*
%{fontdir}/*
/lib/kbd/consolefonts/*

%changelog
* Sat May 25 2013  Falticska Florin <symbianflo@mandrivausers.ro> 1.2a-1
- Push in rels2013
- MRB-Mandriva Users.Ro

* Sun Feb 13 2011 Nux nux@xxxnux.ro
- Import from symbianflo's build
- Build for Stella-6.2
	
* Mon Feb 07 2011 Falticska Florin <symbianflo@mandrivausers.ro> 1.2a-69mrb2010.2
- imported from source 	
- MRB-Mandriva Users.Ro





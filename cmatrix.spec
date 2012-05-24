######################################################
# SpecFile: cmatrix.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
#####################################################
%define debug_package	%{nil}
%define name    cmatrix
%define version     1.2a
%define release 1
Summary:	CMatrix simulates the display from "The Matrix"
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Terminals
License:	GPL
URL:		http://www.asty.org/cmatrix/
Source0:	http://www.asty.org/cmatrix/dist/cmatrix-%{version}.tar.gz
BuildRequires: xfont1-devel libncurses-devel
Requires:	ncurses

	
%description
CMatrix is based on the screensaver from The Matrix website. It works
with terminal settings up to 132x300 and can scroll lines all at the same
rate or asynchronously and at a user-defined speed.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} 
%make

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}/usr/lib/kbd/consolefonts
install -d -m 755 %{buildroot}/usr/X11R6/lib/X11/fonts/misc
install -d -m 755 %{buildroot}/usr/X11R6/lib/X11/fonts/misc
install -d -m 755 %{buildroot}%{_mandir}

install -m 755 cmatrix %{buildroot}%{_bindir}/
install -m 644 matrix.fnt $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts
install -m 644 matrix.psf.gz $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts
install -m 644 mtx.pcf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
install -m 644 mtx.pcf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/mtx.pcf

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog AUTHORS INSTALL NEWS TODO
%{_bindir}/cmatrix
/usr/lib/kbd/consolefonts/matrix.psf.gz
/usr/lib/kbd/consolefonts/matrix.fnt
/usr/X11R6/lib/X11/fonts/misc/mtx.pcf


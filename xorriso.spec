# !!! NOTE: PLD supplies xorriso from libisoburn.spec (using libjte+libisofs+libburn)
#
# Conditional build:
%bcond_without	tests		# don't perform "make test"
#
Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Summary(pl.UTF-8):	Program do operacji na systemach plików ISO 9660 Rock Ridge
Name:		xorriso
Version:	1.5.0
Release:	0.1
License:	GPL v3+
Group:		Applications
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
# Source0-md5:	e5fbae9ada52730fbe248ab9a88e7127
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/xorriso/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xorriso copies file objects from POSIX compliant filesystems into Rock
Ridge enhanced ISO 9660 filesystems and allows session-wise
manipulation of such filesystems. It can load the management
information of existing ISO images and it writes the session results
to optical media or to filesystem objects.

Vice versa xorriso is able to copy file objects out of ISO 9660
filesystems.

%description -l pl.UTF-8
xorriso kopiuje obiekty plików z systemów plików zgodnych z POSIX na
systemy plików ISO 9660 z rozszerzeniem Rock Ridge oraz pozwala na
operacje na tych systemach plików w ramach sesji. Potrafi wczytywać
informacje zarządzające z istniejących obrazów ISO i zapisuje wyniki
sesji na nośnik optyczny lub do obiektów systemu plików.

W drugą stronę xorriso potrafi kopiować obiekty plików z systemów
plików ISO 9660.

%package gui
Summary:	Tcl/Tk based frontend to the ISO 9660 Rock Ridge Filesystem Manipulator
Summary(pl.UTF-8):	Oparty na Tcl/Tk interfejs do obsługi xorriso w formie okien dialogowych
Group:		X11/Applications
Requires:	tk-BWidget
Requires:	%{name} = %{version}-%{release}
Obsoletes:	xorriso-tcltk

%description gui
Tcl/Tk based frontend that operates xorriso in dialog mode.

%description gui -l pl.UTF-8
Oparty na Tcl/Tk interfejs do obsługi xorriso w formie okien
dialogowych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS COPYRIGHT ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/osirrox
%attr(755,root,root) %{_bindir}/xorrecord
%attr(755,root,root) %{_bindir}/xorriso
%attr(755,root,root) %{_bindir}/xorrisofs
%{_mandir}/man1/xorrecord.1*
%{_mandir}/man1/xorriso.1*
%{_mandir}/man1/xorrisofs.1*
%{_infodir}/xorrecord.info*
%{_infodir}/xorriso.info*
%{_infodir}/xorrisofs.info*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xorriso-tcltk
%{_mandir}/man1/xorriso-tcltk.1*
%{_infodir}/xorriso-tcltk.info*

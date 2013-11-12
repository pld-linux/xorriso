#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Name:		xorriso
Version:	1.3.2
Release:	0.1
License:	GPL v3+
Group:		Applications
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
# Source0-md5:	40865f3ca320a08f24235c7c80dc1c19
URL:		http://www.gnu.org/software/xorriso/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	readline-devel
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

%package tcltk
Summary:	Frontend to the ISO 9660 Rock Ridge Filesystem Manipulator
Group:		X11/Applications
Requires:	tk-BWidget
Requires:	%{name} = %{version}-%{release}

%description tcltk
Frontend to xorriso, the ISO 9660 Rock Ridge Filesystem Manipulator.

%prep
%setup -q

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
%doc AUTHORS CONTRIBUTORS COPYRIGHT ChangeLog README
%doc doc/*
%attr(755,root,root) %{_bindir}/osirrox
%attr(755,root,root) %{_bindir}/xorrecord
%attr(755,root,root) %{_bindir}/xorriso
%attr(755,root,root) %{_bindir}/xorrisofs
%{_mandir}/man1/xorrecord.1*
%{_mandir}/man1/xorriso.1*
%{_mandir}/man1/xorrisofs.1*
%{_infodir}/xorr*.info*

%files tcltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xorriso-tcltk


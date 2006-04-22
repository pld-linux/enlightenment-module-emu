#
# TODO:
# - add meaningful descriptions
# - add pl
# - confirm BR and Rs
# - consider breaking the bin file into subpackage
# - checkout
# - rel 1
#
%define		_module_name	emu
%define		_snap	20060420
Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl):	Modu³ Enlightenmenta DR17: %{_module_name}
# - confirm BR and Rs
Name:		enlightenment-module-%{_module_name}
Version:	0.0.9
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e_modules/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	e14627bf404bb1503781bc374affe3ef
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	ewl-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment DR17 module: %{_module_name}.

%description -l pl
Modu³ Enlightenmenta DR17: %{_module_name}.

%prep
%setup -q -n %{_module_name}
sed 's/ 16\.999/ 0.16.999/' -i configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/enlightenment/modules/%{_module_name}
%dir %{_libdir}/enlightenment/modules/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/%{_module_name}/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/%{_module_name}/module_icon.png
%{_libdir}/enlightenment/modules/%{_module_name}/*.edc
%{_libdir}/enlightenment/modules/%{_module_name}/module_edje.edj
%{_datadir}/locale/*/LC_MESSAGES/%{_module_name}.mo

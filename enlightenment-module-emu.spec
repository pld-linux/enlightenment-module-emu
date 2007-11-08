#
%define		_module_name	emu
%define		_snap	20060610
Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: %{_module_name}
Name:		enlightenment-module-%{_module_name}
Version:	2006.01.27
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers/Tools
Source0:	http://sparky.homelinux.org/snaps/enli/e_modules/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	3cdd01c6f874fbfd879c0be7e5b7e67e
URL:		http://edevelop.org/emu
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenment
BuildRequires:	enlightenment-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenment
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment DR17 module: %{_module_name}.

%description -l pl.UTF-8
Moduł Enlightenmenta DR17: %{_module_name}.

%prep
%setup -q -n %{_module_name}
sed -e '/^filesdir/s#= .*#= $(e_modules)/$(MODULE)#' \
	-e '/^pkgdir/s#= .*#= $(e_modules)/$(MODULE)/$(MODULE_ARCH)#' \
	-i src/modules/emu/Makefile.am

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

%find_lang emu

%clean
rm -rf $RPM_BUILD_ROOT

%files -f emu.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/emu_client
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules_extra/%{_module_name}/module.eap

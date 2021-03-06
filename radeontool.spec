Summary:	Utility to control some functions of ATI Radeon chips
Summary(pl.UTF-8):	Narzędzie do sterowania niektórymi funkcjami kart ATI Radeon
Name:		radeontool
Version:	1.6.3
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://people.freedesktop.org/~airlied/radeontool/%{name}-%{version}.tar.bz2
# Source0-md5:	355d0e659dfeae14707f54284674dd07
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10.0
Requires:	xorg-lib-libpciaccess >= 0.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to control some functions of ATI Radeon chips:
- Turning on/off external DAC
- Turning on/off lcd panel backlight
- Turn on/off LCD scaling for resolution mismatch
- Dumping registers

%description -l pl.UTF-8
Narzędzie do sterowania niektórymi funkcjami kart opartych o chipset
ATI Radeon:
- Włączanie/wyłączanie zewnętrznego DAC
- Włączanie/wyłączanie podświetlania panelu LCD
- Włączanie/wyłączanie skalowania LCD przy niepasujących
  rozdzielczościach
- Zrzucanie rejestrów

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avivotool
%attr(755,root,root) %{_bindir}/radeonreg
%attr(755,root,root) %{_bindir}/radeontool

# TODO: use gtk4-update-icon-cache
Summary:	Showtime - watch without distraction
Summary(pl.UTF-8):	Showtime - oglądanie bez rozpraszania
Name:		showtime
Version:	48.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/showtime/48/%{name}-%{version}.tar.xz
# Source0-md5:	28d0f1086a5cec6d57ac32a799ce29d1
URL:		https://apps.gnome.org/Showtime/
BuildRequires:	AppStream
BuildRequires:	gettext-tools
BuildRequires:	gtk4-devel >= 4.15.0
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	meson >= 0.62.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.26.0
Requires:	gtk4 >= 4.15.0
Requires:	libadwaita >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Showtime - watch without distraction.

%description -l pl.UTF-8
Showtime - oglądanie bez rozpraszania.

%prep
%setup -q

%build
%meson

# parallel build is broken (some missing dependency in data)
%meson_build -j1

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/showtime
%{_datadir}/glib-2.0/schemas/org.gnome.Showtime.gschema.xml
%{_datadir}/metainfo/org.gnome.Showtime.metainfo.xml
%{_datadir}/showtime
%{py3_sitescriptdir}/showtime
%{_desktopdir}/org.gnome.Showtime.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Showtime.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Showtime-symbolic.svg

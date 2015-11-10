# TODO: dax-0.2 ???
Summary:	Pinpoint - a tool for making hackers do excellent presentations
Summary(pl.UTF-8):	Pinpoint - narzędzie pozwalającym hackerom robić świetne prezentacje
Name:		pinpoint
Version:	0.1.8
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pinpoint/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	4352f204d5b81bac467578d6a375e2e3
URL:		https://wiki.gnome.org/Apps/Pinpoint
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.9.12
BuildRequires:	clutter-devel >= 1.23.7
BuildRequires:	clutter-gst-devel >= 3.0.0
BuildRequires:	clutter-gtk-devel >= 1.6
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	librsvg-devel >= 2.0
#BuildRequires:	mx-devel >= 1.0 # with dax
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(cairo-pdf) >= 1.9.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pinpoint is a simple presentation tool that hopes to avoid audience
death by bullet point and instead encourage presentations containing
beautiful images and small amounts of concise text in slides.

%description -l pl.UTF-8
Pinpoint to proste narzędzie do prezentacji dające nadzieję, że
odbiorcy nie zanudzą się wypunktowaniami, a zamiast tego będą
zadowoleni z prezentacji zawierających na slajdach ładne obrazki i
niewielkie ilości zwięzłego tekstu.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/pinpoint
%{_datadir}/pinpoint

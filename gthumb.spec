Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl�darka obrazk�w dla GNOME
Name:		gthumb
Version:	2.5.0
Release:	1
License:	GPL
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gthumb/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	de178ab74d848221ef87f8f182f61f18
Patch0:		%{name}-locale_names.patch
URL:		http://gthumb.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libgphoto2-devel >= 2.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	libbonobo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%description -l pl
gThumb pozwala na przegl�danie twardego dysku z pokazywaniem
miniaturek plik�w z obrazkami. Pozwala tak�e ogl�da� pojedyncze pliki
(w tym animacje GIF), dodawa� komentarze do obrazk�w, uk�ada� obrazki
w katalogi, drukowa� obrazki, ogl�da� slajdy, ustawia� t�o biurka itd.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po
sed -i -e 's/^Categories=Application;/Categories=GTK;GNOME;/' \
	data/gthumb.desktop.in

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.{a,la}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}-image-viewer
%attr(755,root,root) %{_libdir}/%{name}-catalog-view
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_mandir}/man1/%{name}.1*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop

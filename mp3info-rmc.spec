Summary:	Utility for MP3 information and tag modification
Summary(pl.UTF-8):	Program do manipulowania znacznikami ID3 plików w formacie MP3
Summary(tr.UTF-8):	MP3 ses dosyası bilgileri düzenleme aracı
Name:		mp3info-rmc
Version:	0.8.5a
Release:	4
License:	GPL v2+
Group:		Applications/Sound
Source0:	ftp://ftp.ibiblio.org/pub/linux/apps/sound/mp3-utils/mp3info/mp3info-%{version}.tgz
# Source0-md5:	cb7b619a10a40aaac2113b87bb2b2ea2
URL:		http://www.ibiblio.org/mp3info/ 
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.

%description -l pl.UTF-8
mp3info jest programem do manipulowania znacznikami ID3 plików w
formacie MP3. Umożliwia dowolne skonfigurowanie wyświetlanych przez to
narzędzie informacji.

%description -l tr.UTF-8
mp3info, MP3 ses dosyalarından TAG (ID3) bilgilerini okumanızı ve
değiştirmenizi sağlayan bir komut satırı aracıdır. Çeşitli şekillerde
çıktılar verebilir.

%package gtk
Summary:	GTK+ version of utility for MP3 information and tag modification
Summary(pl.UTF-8):	Wersja GTK+ programu do manipulowania znacznikami ID3 plików w formacie MP3
Group:		X11/Applications/Sound
Conflicts:	mp3info-rmc < 0.8.5a

%description gtk
GTK+ version of utility for MP3 information and tag modification.

%description gtk -l pl.UTF-8
Wersja GTK+ programu do manipulowania znacznikami ID3 plików w
formacie MP3.

%prep
%setup -q -n mp3info-%{version}

%build
%{__make} mp3info gmp3info \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	STRIP=/bin/true

# conflict with another mp3info
mv -f $RPM_BUILD_ROOT%{_bindir}/mp3info{,-rmc}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/mp3info{,-rmc}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/mp3info-rmc
%{_mandir}/man1/mp3info-rmc.1*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmp3info

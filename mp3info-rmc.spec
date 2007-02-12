# TODO:
# - gtk subpackage
# - gtk bcond
Summary:	Utility for MP3 information and tag modification
Summary(pl.UTF-8):   Program do manipulowania znacznikami ID3 plików w formacie MP3
Summary(tr.UTF-8):   MP3 ses dosyası bilgileri düzenleme aracı
Name:		mp3info-rmc
Version:	0.8.4
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.ibiblio.org/pub/linux/apps/sound/mp3-utils/mp3info/mp3info-%{version}.tgz
# Source0-md5:	879d0ced8ede5ec9fbaff4813851ea3f
Patch0:		%{name}-multiline-strings.patch 
URL:		http://www.ibiblio.org/mp3info/ 
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	ncurses-devel
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

%prep
%setup -q -n mp3info-%{version}
%patch0 -p1

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

mv -f $RPM_BUILD_ROOT%{_bindir}/mp3info{,-rmc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/mp3info-rmc
%attr(755,root,root) %{_bindir}/gmp3info
%{_mandir}/*/*

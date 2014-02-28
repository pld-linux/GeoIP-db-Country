Summary:	GeoLite Country - Country database for GeoIP
Summary(pl.UTF-8):	GeoLite Country - baza danych krajów dla GeoIP
Name:		GeoIP-db-Country
# Updated every month:
Version:	2014.02.05
Release:	2
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz?/GeoIP-%{version}.dat.gz
# Source0-md5:	a551a8f2044c3e6e364c1aa82fe183b3
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoIPv6.dat.gz?/GeoIPv6-%{version}.dat.gz
# Source1-md5:	c635ff5a0ec3afb83b7c291b17323174
URL:		http://dev.maxmind.com/geoip/legacy/geolite/
Requires:	GeoIP-libs >= 1.4.5-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoLite Country is similar to the GeoIP Country database, but is not
as accurate. Should you require greater accuracy, GeoIP Country is a
drop-in replacement for GeoLite Country.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
GeoLite Country jest podobna do bazy danych GeoIP Country, ale nie
jest tak dokładna. Jeśli wymagana jest większa dokładność, GeoIP
Country jest zamiennikiem GeoLite Country.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxWind, dostępne z <http://www.maxwind.com/>.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

gunzip GeoIP-%{version}.dat.gz
gunzip GeoIPv6-%{version}.dat.gz

ver=$(TZ=GMT stat -c '%y' GeoIP-%{version}.dat | awk '{print $1}' | tr - .)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -p GeoIP-%{version}.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoIP.dat
cp -p GeoIPv6-%{version}.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoIPv6.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/GeoIP/*.dat

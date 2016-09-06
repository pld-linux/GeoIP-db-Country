Summary:	GeoLite Country - Country database for GeoIP
Summary(pl.UTF-8):	GeoLite Country - baza danych krajów dla GeoIP
Name:		GeoIP-db-Country
# Updated every month:
Version:	2016.09.06
Release:	1
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz?/GeoIP-%{version}.dat.gz
# Source0-md5:	2e3c2c78f3e753768f3f8dfd32b157c0
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoIPv6.dat.gz?/GeoIPv6-%{version}.dat.gz
# Source1-md5:	643aa0dfedc54a276f87f7f0d3b9c500
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
przez MaxMind, dostępne z <http://www.maxmind.com/>.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

gzip -d GeoIP-%{version}.dat.gz GeoIPv6-%{version}.dat.gz
dt4=$(TZ=GMT stat -c '%y' GeoIP-%{version}.dat | awk '{print $1}' | tr - .)
dt5=$(TZ=GMT stat -c '%y' GeoIP-%{version}.dat | awk '{print $1}' | tr - .)
if [ "$(echo $dt4 | tr -d .)" -gt "$(echo $dt6 | tr -d .)" ]; then
	ver=$dt4
else
	ver=$dt6
fi
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

Summary:	GeoLite Country - Country database for GeoIP
Summary(pl.UTF-8):	GeoLite Country - baza danych krajów dla GeoIP
Name:		GeoIP-db-Country
# Updated every month:
Version:	2010.10.01
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
# Source0-md5:	cf002e4d23b078970b14ef82df589c07
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	a1381bd1aa0a0c91dc31b3f1e847cf4a
URL:		http://www.maxmind.com/app/geolitecountry
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.

GeoLite Country is similar to the GeoIP Country database, but is not
as accurate. Should you require greater accuracy, GeoIP Country is a
drop-in replacement for GeoLite Country.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
GeoIP jest biblioteką napisaną w C umożliwiającą użytkownikowi
odnalezienie państwa, z którego pochodzi dany adres IP lub domena.
Używa do tego zapisanej w pliku bazy danych (z marca 2003). W bazie
tej adresy IP są kluczami, a państwa wartościami. Powinna ona być
dokładniejsza niż sprawdzanie odwrotnego DNS.

GeoLite Country jest podobna do bazy danych GeoIP Country, ale nie
jest tak dokładna. Jeśli wymagana jest większa dokładność, GeoIP
Country jest zamiennikiem GeoLite Country.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxWind, dostępne z <http://www.maxwind.com/>.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

gunzip GeoIP.dat.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP

install GeoIP.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat

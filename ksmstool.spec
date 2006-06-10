Summary:	KSMS-Tool - tool to send SMS via mobile phone
Summary(pl):	KSMS-Tool - narz�dzie do wysy�ania SMS-�w przez telefon kom�rkowy
Name:		ksmstool
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}-0.tar.gz
# Source0-md5:	36df76b1136bf5efa1109bfdec80b5b7
URL:		http://www.kde-apps.org/content/show.php?content=40298
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for sending SMS via your mobile phone. In principle,
every modern mobile phone should be supported; for a list of tested
mobile phones, please visit the KSMS-Tool homepage.

%description -l pl
Jest to narz�dzie do wysy�ania SMS-�w przez telefon kom�rkowy. W
zasadzie ka�dy wsp�czesny telefon powinien by� obs�ugiwany; list�
przetestowanych telefon�w mo�na zobaczy� na stronie domowej projektu.

%prep
%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ksmstool $RPM_BUILD_ROOT%{_bindir}/ksmstool

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmstool

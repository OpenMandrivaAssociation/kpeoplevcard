%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		kpeoplevcard
Version:	0.1
Release:	4
Source0: http://download.kde.org/%{stable}/kpeoplevcard/%{version}/%{name}-%{version}.tar.xz
Summary: VCard reading support for KPeople
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5People)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)

%description
VCard reading support for KPeople

%package devel
Summary: Development files for KPeopleVCard
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
Development files for KPeopleVCard

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/kpeople/datasource/KPeopleVCard.so

%files devel
%{_libdir}/cmake/KF5PeopleVCard

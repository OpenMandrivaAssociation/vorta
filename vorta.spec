Name:           vorta
Version:        0.11.1
Release:        1
Summary:        A GUI for Borg Backup
License:        GPL-3.0-only AND BSD-2-Clause AND OFL-1.1
# src/vorta/qt_single_application.py if BSD-2-Clause
# src/vorta/assets/icons are OFL-1.1
URL:            https://vorta.borgbase.com/
Source0:        https://github.com/borgbase/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:      noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(build)
BuildRequires:  python%{pyver}dist(installer)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

BuildRequires:  desktop-file-utils
Requires:       borgbackup
Requires:       hicolor-icon-theme
Requires:       python-packaging
Requires:       python-peewee
Requires:       python-platformdirs
Requires:       python-psutil
Requires:       python-qt6
Requires:       python-qt6-devel
Requires:       python-secretstorage
Requires:       python-setuptools
Requires:       %{_lib}Qt6Svg

%description
Vorta is a backup client for macOS and Linux desktops.
It integrates the mighty BorgBackup with your desktop environment
to protect your data from disk failure, ransomware and theft

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

install -D -p -m 644 src/vorta/assets/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.borgbase.Vorta.svg
install -D -p -m 644 package/icon-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.borgbase.Vorta-symbolic.svg
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.desktop -t %{buildroot}%{_datadir}/applications/
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.appdata.xml -t %{buildroot}/%{_metainfodir}/

desktop-file-validate %{buildroot}/%{_datadir}/applications/com.borgbase.Vorta.desktop


%files
%doc README.md CONTRIBUTORS.md
%license LICENSE.txt
%{_bindir}/vorta
%{_datadir}/applications/com.borgbase.Vorta.desktop
%{_metainfodir}/com.borgbase.Vorta.appdata.xml
%{_datadir}/icons/hicolor/*/apps/com.borgbase.Vorta*.svg
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.*-info/

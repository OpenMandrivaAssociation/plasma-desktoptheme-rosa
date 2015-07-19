Name: 		plasma-desktoptheme-rosa
Version:	1.2.5
Release:	11
Summary: 	Plasma Desktop theme from ROSA
Group: 		Graphical desktop/KDE
License:        GPLv2
URL:            http://rosalinux.com
BuildRequires:  kde4-macros
Requires:       kdebase4-workspace
BuildArch:	noarch
Source:		%{name}-%{version}.tar.bz2

%description
Original theme for the Plasma Desktop from ROSA.
This theme is used by default in ROSA Desktop since 2011.

%files
%{_kde_appsdir}/desktoptheme/ROSA

%prep
%setup -q -n ROSA

%install
mkdir -p %{buildroot}/%{_kde_appsdir}/desktoptheme/ROSA
mv * %{buildroot}/%{_kde_appsdir}/desktoptheme/ROSA

# Removing KDE Cache. This is not very good idea to use 'rm', 
# I know, but it seems we have no more accurate methods for this.
# Why also %postun script? Because it will work for update 
# and uninstall operations.

%post
rm -rf /var/tmp/kdecache-*/plasma_theme_ROSA.kcache

%postun
rm -rf /var/tmp/kdecache-*/plasma_theme_ROSA.kcache

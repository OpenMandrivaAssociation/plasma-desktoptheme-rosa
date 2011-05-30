Name: 		plasma-desktoptheme-rosa
Version:	1.0.0
Release:	4
Summary: 	Plasma desktoptheme from ROSA Laboratory
Group: 		Graphical desktop/KDE
License:        GPL
URL:            http://rosalab.ru/
BuildRequires:  kde4-macros
Requires:       kdebase4-workspace
BuildArch:	noarch
Source:		%{name}-%{version}.tar.bz2

%description
Original theme for the plasma-desktop from ROSA Laboratory. This theme is used by default 
in Mandriva and ROSA Desktop distibutives since 2011.

%files
%_kde_appsdir/desktoptheme/ROSA

#--------------------------------------------------------------------

%prep
%setup -q -n ROSA

%install
mkdir -p %buildroot/%_kde_appsdir/desktoptheme/ROSA
mv * %buildroot/%_kde_appsdir/desktoptheme/ROSA


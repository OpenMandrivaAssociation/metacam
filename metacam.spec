%define name metacam
%define version 1.2
%define release %mkrel 3

Summary:	Command line tool to read the EXIF extensions in JPEG files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics

Source:		ftp://ftp.cheeseplant.org/pub/metacam-1.2.tar.bz2

Url:		http://www.cheeseplant.org/~daniel/pages/metacam.html
BuildRoot:	%_tmppath/%name-%version-%release-root

%description

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. This tool can
extract information from these tags.

The speciality of this program is that it knows many manufacturer-
specific entries for Nikon, Canon, and Olympus cameras.

%prep
%setup -q

%build
%make
chmod a+rX *

%install
install -d %buildroot%_bindir
install -m 755 metacam %buildroot%_bindir

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README* LICENSE* BUGS THANKS
%_bindir/*


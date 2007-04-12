Summary:	Command line tool to read the EXIF extensions in JPEG files
Name:		metacam
Version:	1.2
Release:	2mdk
License:	GPL
Group:		Graphics

Source:		ftp://ftp.cheeseplant.org/pub/metacam-1.2.tar.bz2

Url:		http://www.cheeseplant.org/~daniel/pages/metacam.html
BuildRoot:	%_tmppath/%name-%version-%release-root

%description

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image.

In contrary to the tools "exif" and "gexif" (and all other
libexif-based tools as "gphoto2") this tool gives a much easier
readable summary of camera settings. But the speciality of this
program is that it knows many manufacturer-specific entries for Nikon,
Canon, and Olympus cameras.

The tool is very compact, the executable has only a size of around 87
kb.

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


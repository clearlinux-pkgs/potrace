#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : potrace
Version  : 1.15
Release  : 1
URL      : http://potrace.sourceforge.net/download/1.15/potrace-1.15.tar.gz
Source0  : http://potrace.sourceforge.net/download/1.15/potrace-1.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: potrace-bin = %{version}-%{release}
Requires: potrace-license = %{version}-%{release}
Requires: potrace-man = %{version}-%{release}
BuildRequires : pkgconfig(zlib)

%description
POTRACE - transform bitmaps into vector graphics

* * *

DESCRIPTION
Potrace is a tool for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.  The input is a bitmap (PBM,
PGM, PPM, or BMP), and the output is one of several vector file
formats.  A typical use is to create SVG or PDF files from scanned
data, such as company or university logos, handwritten notes, etc.
The resulting image is not "jaggy" like a bitmap, but smooth. It can
then be rendered at any resolution.

%package bin
Summary: bin components for the potrace package.
Group: Binaries
Requires: potrace-license = %{version}-%{release}
Requires: potrace-man = %{version}-%{release}

%description bin
bin components for the potrace package.


%package doc
Summary: doc components for the potrace package.
Group: Documentation
Requires: potrace-man = %{version}-%{release}

%description doc
doc components for the potrace package.


%package license
Summary: license components for the potrace package.
Group: Default

%description license
license components for the potrace package.


%package man
Summary: man components for the potrace package.
Group: Default

%description man
man components for the potrace package.


%prep
%setup -q -n potrace-1.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543754054
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1543754054
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/potrace
cp COPYING %{buildroot}/usr/share/package-licenses/potrace/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkbitmap
/usr/bin/potrace

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/potrace/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/potrace/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mkbitmap.1
/usr/share/man/man1/potrace.1

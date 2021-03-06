#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zlib
Version  : 1.2.11.1.jtkv6.3
Release  : 62
URL      : https://github.com/jtkukunas/zlib/archive/v1.2.11.1_jtkv6.3.tar.gz
Source0  : https://github.com/jtkukunas/zlib/archive/v1.2.11.1_jtkv6.3.tar.gz
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 Zlib
Requires: zlib-lib = %{version}-%{release}
Requires: zlib-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
Patch1: configure.patch
Patch2: lto.patch

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.2.11.1 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

%package dev
Summary: dev components for the zlib package.
Group: Development
Requires: zlib-lib = %{version}-%{release}
Provides: zlib-devel = %{version}-%{release}
Requires: zlib = %{version}-%{release}

%description dev
dev components for the zlib package.


%package dev32
Summary: dev32 components for the zlib package.
Group: Default
Requires: zlib-lib32 = %{version}-%{release}
Requires: zlib-dev = %{version}-%{release}

%description dev32
dev32 components for the zlib package.


%package lib
Summary: lib components for the zlib package.
Group: Libraries
Requires: zlib-license = %{version}-%{release}

%description lib
lib components for the zlib package.


%package lib32
Summary: lib32 components for the zlib package.
Group: Default
Requires: zlib-license = %{version}-%{release}

%description lib32
lib32 components for the zlib package.


%package license
Summary: license components for the zlib package.
Group: Default

%description license
license components for the zlib package.


%package staticdev
Summary: staticdev components for the zlib package.
Group: Default
Requires: zlib-dev = %{version}-%{release}

%description staticdev
staticdev components for the zlib package.


%package staticdev32
Summary: staticdev32 components for the zlib package.
Group: Default
Requires: zlib-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the zlib package.


%prep
%setup -q -n zlib-1.2.11.1_jtkv6.3
cd %{_builddir}/zlib-1.2.11.1_jtkv6.3
%patch1 -p1
%patch2 -p1
pushd ..
cp -a zlib-1.2.11.1_jtkv6.3 build32
popd
pushd ..
cp -a zlib-1.2.11.1_jtkv6.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605555447
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %configure  --static --shared
make  %{?_smp_mflags}

cat *.c | ./minigzip -6 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -4 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -9 | ./minigzip -d > /dev/null
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %configure  --static --shared
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure  --static --shared   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure  --static --shared
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1605555447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zlib
cp %{_builddir}/zlib-1.2.11.1_jtkv6.3/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/zlib/892b34f7865d90a6f949f50d95e49625a10bc7f0
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/lib64/haswell/libz.a
rm -f %{buildroot}/usr/lib64/haswell/pkgconfig/zlib.pc

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib64/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32zlib.pc
/usr/lib32/pkgconfig/zlib.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libz.so
/usr/lib64/haswell/libz.so.1
/usr/lib64/haswell/libz.so.1.2.11.1-motley
/usr/lib64/libz.so
/usr/lib64/libz.so.1
/usr/lib64/libz.so.1.2.11.1-motley

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libz.so
/usr/lib32/libz.so.1
/usr/lib32/libz.so.1.2.11.1-motley

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zlib/892b34f7865d90a6f949f50d95e49625a10bc7f0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libz.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libz.a

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
%define keepstatic 1
Name     : zlib
Version  : 1.2.13
Release  : 100
URL      : https://github.com/jtkukunas/zlib/archive/v1.2.13/zlib-1.2.13.tar.gz
Source0  : https://github.com/jtkukunas/zlib/archive/v1.2.13/zlib-1.2.13.tar.gz
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 Zlib
Requires: zlib-lib = %{version}-%{release}
Requires: zlib-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: configure.patch
Patch2: lto.patch
Patch3: nomemlevel.patch
Patch4: backport-CVE-2023-45853.patch

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.2.13 is a general purpose data compression library.  All the code is
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
%setup -q -n zlib-1.2.13
cd %{_builddir}/zlib-1.2.13
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
pushd ..
cp -a zlib-1.2.13 build32
popd
pushd ..
cp -a zlib-1.2.13 buildavx2
popd
pushd ..
cp -a zlib-1.2.13 buildapx
popd

%build
## build_prepend content
export CFLAGS="$CFLAGS  -DUNALIGNED_OK -D_REENTRANT -D_LARGEFILE64_SOURCE=1 "
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740106802
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %configure  --static --shared
make  %{?_smp_mflags}

cat *.c | ./minigzip -6 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -4 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -9 | ./minigzip -d > /dev/null
cat minigzip | ./minigzip -6 | ./minigzip -d > /dev/null
cat minigzip | ./minigzip -4 | ./minigzip -d > /dev/null
cat minigzip | ./minigzip -9 | ./minigzip -d > /dev/null
make clean
export GOAMD64=v2
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %configure  --static --shared
make  %{?_smp_mflags}

pushd ../build32/
## build_prepend content
export CFLAGS="$CFLAGS  -DUNALIGNED_OK -D_REENTRANT -D_LARGEFILE64_SOURCE=1 "
## build_prepend end
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure  --static --shared   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
export CFLAGS="$CFLAGS  -DUNALIGNED_OK -D_REENTRANT -D_LARGEFILE64_SOURCE=1 "
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure  --static --shared
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildapx/
## build_prepend content
export CFLAGS="$CFLAGS  -DUNALIGNED_OK -D_REENTRANT -D_LARGEFILE64_SOURCE=1 "
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --host=x86_64-clr-linux-gnu  --static --shared
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
cd ../buildapx;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1740106802
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zlib
cp %{_builddir}/zlib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zlib/233f44af3fb55dcc7fddfef8e77ac627b0008756 || :
cp %{_builddir}/zlib-%{version}/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/zlib/892b34f7865d90a6f949f50d95e49625a10bc7f0 || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v3
pushd ../buildapx/
%make_install_va
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libz.so.1.2.13
/VA/usr/lib64/libz.so.1.2.13
/usr/lib64/libz.so
/usr/lib64/libz.so.1
/usr/lib64/libz.so.1.2.13

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libz.so
/usr/lib32/libz.so.1
/usr/lib32/libz.so.1.2.13

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zlib/233f44af3fb55dcc7fddfef8e77ac627b0008756
/usr/share/package-licenses/zlib/892b34f7865d90a6f949f50d95e49625a10bc7f0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libz.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libz.a

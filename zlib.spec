#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zlib
Version  : 1.2.8.jtkv4
Release  : 40
URL      : https://github.com/jtkukunas/zlib/archive/v1.2.8_jtkv4.tar.gz
Source0  : https://github.com/jtkukunas/zlib/archive/v1.2.8_jtkv4.tar.gz
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 Zlib
Requires: zlib-lib
Requires: zlib-doc
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
Patch1: configure.patch
Patch2: lto.patch
Patch3: disable-level1.patch
Patch4: 0001-fix-fizzle-check.patch
Patch5: 0001-temporarily-workaround-JIRA-801.patch

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.2.8 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

%package dev
Summary: dev components for the zlib package.
Group: Development
Requires: zlib-lib
Provides: zlib-devel

%description dev
dev components for the zlib package.


%package dev32
Summary: dev32 components for the zlib package.
Group: Default
Requires: zlib-lib32
Requires: zlib-dev

%description dev32
dev32 components for the zlib package.


%package doc
Summary: doc components for the zlib package.
Group: Documentation

%description doc
doc components for the zlib package.


%package lib
Summary: lib components for the zlib package.
Group: Libraries

%description lib
lib components for the zlib package.


%package lib32
Summary: lib32 components for the zlib package.
Group: Default

%description lib32
lib32 components for the zlib package.


%prep
%setup -q -n zlib-1.2.8_jtkv4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a zlib-1.2.8_jtkv4 build32
popd
pushd ..
cp -a zlib-1.2.8_jtkv4 build-avx2
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486485200
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %configure  --static --shared
make V=1  %{?_smp_mflags}

cat *.c | ./minigzip -6 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -4 | ./minigzip -d > /dev/null
cat *.c | ./minigzip -9 | ./minigzip -d > /dev/null
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %configure  --static --shared
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure  --static --shared   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

pushd ../build-avx2/
export LDFLAGS="$LDFLAGS -m64"
if [ ! -z "`cat /proc/cpuinfo  | grep bmi2`" ]
then
	CFLAGS="${CFLAGS_GENERATE} -march=haswell" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %configure  --static --shared --libdir=/usr/lib64/haswell
	make V=1  %{?_smp_mflags}
	cat *.c | ./minigzip -6 | ./minigzip -d > /dev/null
	cat *.c | ./minigzip -4 | ./minigzip -d > /dev/null
	cat *.c | ./minigzip -9 | ./minigzip -d > /dev/null
	make clean
fi
CFLAGS="${CFLAGS_USE} -march=haswell" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %configure  --static --shared --libdir=/usr/lib64/haswell
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1486485200
rm -rf %{buildroot}

pushd ../build-avx2/
%make_install
popd
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib32/libz.a

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.a
/usr/lib64/libz.so
/usr/lib64/pkgconfig/zlib.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libz.so
/usr/lib32/pkgconfig/32zlib.pc
/usr/lib32/pkgconfig/zlib.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libz.so.1
/usr/lib64/libz.so.1.2.8
/usr/lib64/haswell/libz.so.1
/usr/lib64/haswell/libz.so.1.2.8
%exclude /usr/lib64/haswell/libz.a
%exclude /usr/lib64/haswell/libz.so
%exclude /usr/lib64/haswell/pkgconfig/zlib.pc


%files lib32
%defattr(-,root,root,-)
/usr/lib32/libz.so.1
/usr/lib32/libz.so.1.2.8

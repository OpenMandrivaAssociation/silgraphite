%define	major	3
%define	libname	%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d

Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		silgraphite
Version:	2.3.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+ or CPL
URL:		http://sourceforge.net/projects/silgraphite/
Source0:	http://downloads.sourceforge.net/silgraphite/silgraphite-%{version}.tar.gz

%description
Graphite is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create “smart fonts” capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by %{name}.

%package -n %{develname}
Summary:	Files for developing with silgraphite
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Includes and definitions for developing with silgraphite.

%prep
%setup -q
sed -i -e '/build_flags -O3/s/-O3//' engine/configure

%build
cd engine
autoreconf -fi
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std -C engine

%check
make -C engine/test/RegressionTest check

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/graphite
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global src_name scciclient
%global pkg_name python-scciclient
%global sum Python ServerView Common Command Interface (SCCI) Client Library

%global common_desc \
Python ServerView Common Command Interface (SCCI) Client Library

Name:        %{pkg_name}
Version:     0.8.1
Release:     1%{?dist}
Summary:     %{sum}
License:     ASL 2.0
URL:         https://pypi.python.org/pypi/%{pkg_name}
Source0:     https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz
BuildArch:   noarch

%description
%{common_desc}

%package -n python%{pyver}-%{src_name}
Summary: %{sum}
%{?python_provide:%python_provide python%{pyver}-%{src_name}}

BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-pbr
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-oslo-utils
BuildRequires: python%{pyver}-oslo-sphinx
BuildRequires: python%{pyver}-testscenarios
BuildRequires: python%{pyver}-stestr
BuildRequires: python%{pyver}-mock
BuildRequires: python%{pyver}-pyghmi
BuildRequires: python%{pyver}-pysnmp
BuildRequires: python%{pyver}-oslo-serialization
BuildRequires: git

# Handle python2 exception
%if %{pyver} == 2
BuildRequires: python-requests-mock
%else
BuildRequires: python%{pyver}-requests-mock
%endif

Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-babel >= 2.3.4
Requires: python%{pyver}-requests >= 2.14.2
Requires: python%{pyver}-six >= 1.10
Requires: python%{pyver}-oslo-utils >= 3.33.0
Requires: python%{pyver}-oslo-serialization >= 2.18.0
Requires: python%{pyver}-pyghmi
Requires: python%{pyver}-pysnmp
Requires: python%{pyver}-defusedxml >= 0.5.0

%description -n python%{pyver}-%{src_name}
%{common_desc}

%prep
%autosetup -n %{pkg_name}-%{upstream_version} -S git

%build
%{pyver_build}

%install
%{pyver_install}

%check
PYTHON=%{pyver_bin} stestr-%{pyver} run

%files -n python%{pyver}-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{pyver_sitelib}/%{src_name}
%{pyver_sitelib}/*.egg-info

%changelog
* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 0.8.1-1
- Update to 0.8.1


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global src_name scciclient
%global pkg_name python-scciclient
%global sum Python ServerView Common Command Interface (SCCI) Client Library

%global common_desc \
Python ServerView Common Command Interface (SCCI) Client Library

Name:        %{pkg_name}
Version:     XXX
Release:     XXX
Summary:     %{sum}
License:     ASL 2.0
URL:         https://pypi.python.org/pypi/%{pkg_name}
Source0:     https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz
BuildArch:   noarch

%description
%{common_desc}


%package -n python3-%{src_name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{src_name}}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-sphinx
BuildRequires: python3-testscenarios
BuildRequires: python3-stestr
BuildRequires: python3-mock
BuildRequires: python3-pyghmi
BuildRequires: python3-pysnmp
BuildRequires: python3-oslo-serialization
BuildRequires: git

BuildRequires: python3-requests-mock

Requires: python3-pbr >= 2.0.0
Requires: python3-babel >= 2.3.4
Requires: python3-requests >= 2.14.2
Requires: python3-six >= 1.10.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-pyghmi
Requires: python3-pysnmp

%description -n python3-%{src_name}
%{common_desc}

%prep
%autosetup -n %{pkg_name}-%{upstream_version} -S git

%build
%{py3_build}

%install
%{py3_install}

%check
PYTHON=%{__python3} stestr run

%files -n python3-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/*.egg-info

%changelog
# REMOVEME: error caused by commit https://opendev.org/openstack/python-scciclient/commit/8e527de430cc6dc2a743e39af478cb84f71a3af9

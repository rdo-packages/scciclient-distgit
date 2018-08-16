%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global src_name scciclient
%global pkg_name python-scciclient
%global sum Python ServerView Common Command Interface (SCCI) Client Library

%global common_desc \
Python ServerView Common Command Interface (SCCI) Client Library

Name:        %{pkg_name}
Version:     0.7.3
Release:     1%{?dist}
Summary:     %{sum}
License:     ASL 2.0
URL:         https://pypi.python.org/pypi/%{pkg_name}
Source0:     https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz
BuildArch:   noarch

%description
%{common_desc}


%package -n python2-%{src_name}
Summary: %{sum}
%{?python_provide:%python_provide python2-%{src_name}}

BuildRequires: python2-devel
BuildRequires: python2-pbr
BuildRequires: python2-setuptools
BuildRequires: python2-oslo-utils
BuildRequires: python2-oslo-sphinx
BuildRequires: python-requests-mock
BuildRequires: python2-testscenarios
BuildRequires: python2-stestr
BuildRequires: python2-mock
BuildRequires: python2-pyghmi
BuildRequires: python2-pysnmp
BuildRequires: python2-oslo-serialization
BuildRequires: git

Requires: python2-pbr >= 2.0.0
Requires: python2-babel >= 2.3.4
Requires: python2-requests >= 2.14.2
Requires: python2-six >= 1.10
Requires: python2-oslo-utils >= 3.33.0
Requires: python2-oslo-serialization >= 2.18.0
Requires: python2-pyghmi
Requires: python2-pysnmp

%description -n python2-%{src_name}
%{common_desc}


%if 0%{?with_python3}
%package -n python3-%{src_name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{src_name}}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-sphinx
BuildRequires: python3-requests-mock
BuildRequires: python3-stestr
BuildRequires: python3-testrepository
BuildRequires: python3-mock
BuildRequires: python3-pysnmp
# FIXME(ykarel): python3-pyghmi doesn't exist yet as pyghmi is not compatible
# with python 3: https://bugs.launchpad.net/pyghmi/+bug/1578613
#BuildRequires: python3-pyghmi
BuildRequires: python3-oslo-serialization
BuildRequires: git

Requires: python3-pbr >= 2.0.0
Requires: python3-babel >= 2.3.4
Requires: python3-requests >= 2.14.2
Requires: python3-six >= 1.10
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-pysnmp
# FIXME(ykarel): python3-pyghmi doesn't exist yet as pyghmi is not compatible
# with python 3: https://bugs.launchpad.net/pyghmi/+bug/1578613
#Requires: python3-pyghmi

%description -n python3-%{src_name}
%{common_desc}
%endif


%prep
%autosetup -n %{pkg_name}-%{upstream_version} -S git

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?with_python3}
stestr-3 run
%endif
stestr run

%files -n python2-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{python2_sitelib}/%{src_name}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/*.egg-info
%endif

%changelog
* Thu Aug 16 2018 RDO <dev@lists.rdoproject.org> 0.7.3-1
- Update to 0.7.3

* Wed Apr 19 2017 Koki Sanagi <sanagi.koki@jp.fujitsu.com> - 0.4.0-1
- Initial package

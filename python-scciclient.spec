%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x815AFEC729392386480E076DCC0DFE2D21C023C9
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx openstackdocstheme
%global src_name scciclient
%global pkg_name python-scciclient
%global sum Python ServerView Common Command Interface (SCCI) Client Library

%global common_desc \
Python ServerView Common Command Interface (SCCI) Client Library

Name:        %{pkg_name}
Version:     0.15.0
Release:     1%{?dist}
Summary:     %{sum}
License:     Apache-2.0
URL:         https://pypi.python.org/pypi/%{pkg_name}
Source0:     https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:   noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}


%package -n python3-%{src_name}
Summary: %{sum}

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: git-core

%description -n python3-%{src_name}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pkg_name}-%{upstream_version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox -e %{default_toxenv}

%files -n python3-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/*.dist-info

%changelog
* Fri Sep 08 2023 RDO <dev@lists.rdoproject.org> 0.15.0-1
- Update to 0.15.0


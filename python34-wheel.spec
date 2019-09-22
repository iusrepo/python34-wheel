%global srcname wheel

%if %{undefined el6}
%global __python3 /usr/bin/python3.4
%endif

Name:           python34-%{srcname}
Version:        0.30.0
Release:        2%{?dist}
Summary:        A built-package format for Python
License:        MIT
URL:            https://github.com/pypa/%{srcname}
Source0:        %pypi_source
BuildArch:      noarch
BuildRequires:  python3-rpm-macros
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools

# Rename from python34u-wheel
Provides:       python34u-%{srcname} = %{version}-%{release}
Obsoletes:      python34u-%{srcname} < 0.30.0-2


%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and the
.whl extension. It is designed to contain all the files for a PEP 376
compatible install in a way that is very close to the on-disk format.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install
mv %{buildroot}%{_bindir}/%{srcname}{,-%{python3_version}}
%if %{defined el6}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}-3
%endif


%files
%license LICENSE.txt
%doc CHANGES.txt README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{srcname}-%{python3_version}
%if %{defined el6}
%{_bindir}/%{srcname}-3
%endif


%changelog
* Sun Sep 22 2019 Carl George <carl@george.computer> - 0.30.0-2
- Rename to python34-wheel
- Switch to EPEL python3 macros

* Mon Sep 18 2017 Ben Harper <ben.harper@rackspace.com> - 0.30.0-1.ius
- Latest upstream
- update URL
- update Source0
- use %license
- remove README.txt and test directory, removed upstream

* Mon Feb 08 2016 Ben Harper <ben.harper@rackspace.com> - 0.29.0-1.ius
- Latest upstream

* Mon Oct 05 2015 Carl George <carl.george@rackspace.com> - 0.26.0-1.ius
- Latest upstream

* Thu Sep 17 2015 Ben Harper <ben.harper@rackspace.com> - 0.25.0-1.ius
- Latest upstream

* Tue Aug 12 2014 Carl George <carl.george@rackspace.com> - 0.24.0-1.ius
- Port from Fedora to IUS
- Remove patches (merged upstream)
- Disable test suite
- Latest upstream

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.22.0-3
- Another rebuild with python 3.4

* Fri Apr 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.22.0-2
- Rebuild with python 3.4

* Thu Nov 28 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.22.0-1
- Initial package.

%global pymajor 3
%global pyminor 4
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}u
%global srcname wheel
%global src %(echo %{srcname} | cut -c1)
%global with_tests 0


Name:           python%{iusver}-%{srcname}
Version:        0.24.0
Release:        1.ius%{?dist}
Summary:        A built-package format for Python %{pyver}
%if 0%{?rhel} < 7
Group:          Development/Libraries
%endif
License:        MIT
URL:            https://bitbucket.org/pypa/%{srcname}
Source0:        https://pypi.python.org/packages/source/%{src}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python%{iusver}-devel
BuildRequires:  python%{iusver}-setuptools
%if 0%{?with_tests}
# These don't exist in IUS yet, so don't enable the test suite until they do.
BuildRequires:  pytest%{iusver}
BuildRequires:  python%{iusver}-jsonschema
BuildRequires:  python%{iusver}-keyring
%endif


%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and the
.whl extension. It is designed to contain all the files for a PEP 376
compatible install in a way that is very close to the on-disk format.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --optimize 1 --skip-build --root %{buildroot}
%{__mv} %{buildroot}%{_bindir}/%{srcname}{,%{pyver}}
ln -sf %{_bindir}/%{srcname}%{pyver} %{buildroot}%{_bindir}/%{srcname}%{pymajor}


%if 0%{?with_tests}
%check
# remove setup.cfg that makes pytest require pytest-cov (unnecessary dep)
rm setup.cfg
py.test-%{pyver} --ignore build
%endif


%files
%doc LICENSE.txt CHANGES.txt README.txt
%{_bindir}/%{srcname}%{pymajor}
%{_bindir}/%{srcname}%{pyver}
%{python3_sitelib}/%{srcname}*
%exclude %{python3_sitelib}/%{srcname}/test


%changelog
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

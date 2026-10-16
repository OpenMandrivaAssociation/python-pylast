%define module pylast

Name:		python-%{module}
Version:	7.2.0
Release:	1
Summary:	Python interface to Last.fm
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/pylast/pylast
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(httpx2)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
Python interface to Last.fm and other API-compatible websites
such as Libre.fm. Speaks HTTP through httpx2.

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info

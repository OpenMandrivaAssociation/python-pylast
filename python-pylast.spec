%define module pylast

Summary:	Python interface to Last.fm
Name:		python-%{module}
Version:	5.0.0
Release:	1
License:	GPLv2+
Group:		Development/Python
Url:		https://github.com/pylast/pylast
Source0:	https://github.com/pylast/pylast/archive/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildArch:	noarch

%description
Python interface to Last.fm and other API-compatible websites
such as Libre.fm.

%files
%dir %{py_puresitedir}/pylast
%{py_puresitedir}/pylast/*
%{py_puresitedir}/pylast-%{version}-py%{py_ver}.egg-info

#----------------------------------------------------------------------------

%prep
%setup -qn %{module}-%{version}

%build

%install
%__python setup.py install --root=%{buildroot}

%define module pylast

Summary:	Python interface to Last.fm
Name:		python-%{module}
Version:	3.1.0
Release:	1
License:	GPLv2+
Group:		Development/Python
Url:		https://github.com/pylast/pylast
Source0:	https://github.com/pylast/pylast/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
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

%define debug_package %{nil}
Name:           gopass
Version:        1.6.2
Release:        0%{?dist}
Summary:        The slightly more awesome standard unix password manager for teams

Group:          Applications/System
License:        MIT
URL:            https://github.com/justwatchcom/gopass
Source0:        https://github.com/justwatchcom/gopass/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git golang

%description
The slightly more awesome standard unix password manager for teams

%prep
mkdir -p %{_builddir}/src/github.com/justwatchcom
cd %{_builddir}/src/github.com/justwatchcom
tar -xvzf %{_sourcedir}/%{name}-%{version}.tar.gz 
mv %{name}-%{version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/justwatchcom/%{name}
go build

%install
mkdir -p %{buildroot}%{_bindir}

cp %{_builddir}/src/github.com/justwatchcom/%{name}/gopass %{buildroot}%{_bindir}


%files
%{_bindir}/gopass

%changelog
* Sat Dec 02 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.2-0
- New release 1.6.2

* Mon Nov 27 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.1-0
- First rpm

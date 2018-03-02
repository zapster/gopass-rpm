%define debug_package %{nil}
Name:           gopass
Version:        1.6.11
Release:        1%{?dist}
Summary:        The slightly more awesome standard unix password manager for teams

Group:          Applications/System
License:        MIT
URL:            https://github.com/justwatchcom/gopass
Source0:        https://github.com/justwatchcom/gopass/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tar gzip git golang

%description
The slightly more awesome standard unix password manager for teams

%package zsh-completion
Summary:        Z shell completion for gopass
Requires:       zsh

%description zsh-completion
Z shell auto completion for gopass.

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
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/

cp %{_builddir}/src/github.com/justwatchcom/%{name}/gopass %{buildroot}%{_bindir}
# zsh completion
cp %{_builddir}/src/github.com/justwatchcom/%{name}/zsh.completion %{buildroot}%{_datadir}/zsh/site-functions/_gopass


%files
%{_bindir}/gopass

%files zsh-completion
%{_datadir}/zsh/site-functions/_gopass

%changelog
* Thu Mar 01 2018 Lars Kiesow <lkiesow@uos.de> - 1.6.11-1
- Added zsh completion packet

* Fri Feb 23 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.11-0
- New release 1.6.11

* Sun Jan 21 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.10-0
- New release 1.6.10

* Sat Jan 06 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.9-0
- New release 1.6.9

* Mon Jan 01 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.7-0
- New release 1.6.7

* Fri Dec 29 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.6-0
- New release 1.6.6

* Fri Dec 15 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.5-0
- New release 1.6.5

* Thu Dec 14 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.4-0
- New release 1.6.4

* Wed Dec 13 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.3-0
- New release 1.6.3

* Sat Dec 02 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.2-0
- New release 1.6.2

* Mon Nov 27 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.6.1-0
- First rpm

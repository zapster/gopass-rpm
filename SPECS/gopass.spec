%define debug_package %{nil}
%define repo github.com/gopasspw/gopass

Name:           gopass
Version:        1.11.0
Release:        1%{?dist}
Summary:        The slightly more awesome standard unix password manager for teams

Group:          Applications/System
License:        MIT
URL:            https://%{repo}
Source0:        https://%{repo}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tar gzip git golang

%description
The slightly more awesome standard unix password manager for teams

%package zsh-completion
Summary:        Z shell completion for gopass
Requires:       zsh %{name}

%description zsh-completion
Z shell auto completion for gopass.

%prep
%setup -q -c -n %{name}-%{version}
cd ..
mkdir -p $(dirname src/%{repo})
mv %{name}-%{version} src/%{repo}
mkdir %{name}-%{version}
mv src %{name}-%{version}

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
cd src/%{repo}
make build
make completion

%install
install -D src/%{repo}/gopass %{buildroot}%{_bindir}/gopass
install -D src/%{repo}/cmd/gopass-git-credentials/gopass-git-credentials %{buildroot}%{_bindir}/gopass-git-credentials 
install -D src/%{repo}/cmd/gopass-hibp/gopass-hibp %{buildroot}%{_bindir}/gopass-hibp 
install -D src/%{repo}/cmd/gopass-jsonapi/gopass-jsonapi %{buildroot}%{_bindir}/gopass-jsonapi 
install -D src/%{repo}/cmd/gopass-summon-provider/gopass-summon-provider %{buildroot}%{_bindir}/gopass-summon-provider
install -D src/%{repo}/bash.completion %{buildroot}%{_datadir}/bash-completion/completions/gopass
install -D src/%{repo}/zsh.completion %{buildroot}%{_datadir}/zsh/site-functions/_gopass


%files
%{_bindir}/gopass
%{_bindir}/gopass-git-credentials
%{_bindir}/gopass-hibp
%{_bindir}/gopass-jsonapi
%{_bindir}/gopass-summon-provider
%{_datadir}/bash-completion/completions/gopass
%license src/%{repo}/LICENSE

%files zsh-completion
%{_datadir}/zsh/site-functions/_gopass

%changelog
* Thu Jan 21 2021 Dominik Rimpf <dev@drimpf.de> - 1.11.0-1
- New release 1.11.0

* Sat Sep 19 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.10.1-1
- New release 1.10.1

* Sun May 31 2020 Tore Anderson <tore@fud.no> - 1.9.2-2
- Include bash completion file

* Thu May 14 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.9.2-1
- New release 1.9.1

* Mon May 11 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.9.1-1
- New release 1.9.1

* Sun May 03 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.9.0-1
- New release 1.9.0

* Fri Jul 26 2019 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.6-1
- New release 1.8.6

* Mon Mar 04 2019 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.5-1
- New release 1.8.5

* Fri Dec 21 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.4-1
- New release 1.8.4

* Tue Nov 20 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.3-1
- New release 1.8.3

* Fri Jun 29 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.2-1
- New release 1.8.2

* Fri Jun 08 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.1-1
- New release 1.8.1

* Wed Jun 06 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.8.0-1
- New release 1.8.0
- Update repo url

* Tue May 29 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.7.2-1
- New release 1.7.2

* Fri May 25 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.7.1-1
- New release 1.7.1

* Tue May 22 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.7.0-1
- New release 1.7.0

* Wed Apr 11 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> - 1.6.11-4
- Add license file

* Sun Mar 04 2018 Lars Kiesow <lkiesow@uos.de> - 1.6.11-3
- Improve .spec

* Sun Mar 04 2018 Lars Kiesow <lkiesow@uos.de> - 1.6.11-2
- Fix prep phase

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

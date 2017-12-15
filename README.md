# gopass rpm

## RPM Build

#### Install rpmbuild requirements

```
yum install -y spectool git mock
```

### Setup build environment

```
cd ~
git clone https://gitlab.com/daftaupe/gopass-rpm.git
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
ln -s ~/gopass-rpm/SPECS/gopass.spec ~/rpmbuild/SPECS/gopass.spec
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
cd ~/rpmbuild/SOURCES/
spectool -g ../SPECS/gopass.spec
cd ~/rpmbuild/SPECS/
```
### Build the SRPM
```
mock --resultdir ~/rpmbuild/SRPMS --buildsrpm --spec ~/rpmbuild/SPECS/gopass.spec --sources ~/rpmbuild/SOURCES/v1.6.4.tar.gz
# Get the SRPM in ~/rpmbuild/SRPMS
```

### Build the RPM from the SRPM
You build it as indicated before (in that case be careful about the name of the SRPM you will get).
```
#RPM file will be found in ~/rpmbuild/RPMS
# Centos7-64bits
mock --cleanup-after --resultdir ~/rpmbuild/RPMS -r epel-7-x86_64 ~/rpmbuild/SRPMS/gopass-1.6.4-0.el7.src.rpm
# Fedora-25-64bits
mock --cleanup-after --resultdir ~/rpmbuild/RPMS -r epel-7-x86_64 ~/rpmbuild/SRPMS/gopass-1.6.4-0.fc27.src.rpm
```

## Usage

The gopass binary will be in /usr/bin

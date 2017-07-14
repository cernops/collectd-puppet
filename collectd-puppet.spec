Summary:   collectd plugin for puppet last run
Name:      collectd-puppet
Version:   0.1.0
Release:   1%{?dist}
BuildArch: noarch
Source:    %{name}-%{version}.tgz
License:   ASL 2.0
URL:       https://gitlab.cern.ch/ai-config-team/collectd-puppet

Requires: collectd
Requires: PyYAML

%description
A python collectd plugin for puppet. 
In particular it published metrics the the puppet_last_run
summary.

%prep
%setup -q

%build
# Nothings to build

%install
mkdir -p %{buildroot}/usr/libexec/sensors
mkdir -p %{buildroot}/usr/share/collectd
install -m 0644 puppet.py       %{buildroot}/usr/libexec/sensors/puppet.py
install -m 0644 puppet_types.db %{buildroot}/usr/share/collectd/puppet_types.db
%files
%dir /usr/libexec/sensors
/usr/libexec/sensors/puppet.py*
/usr/share/collectd/puppet_types.db
%doc README

%changelog
* Fri Jul 14 2017 Steve Traylen <steve.traylen@cern.ch> 0.1.0-1
- Initial Release



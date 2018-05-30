Summary: CGTS Platform Fault Management Documentation Package
Name: fm-doc
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown
BuildRequires: fm-api-doc
BuildRequires: fm-common-doc
BuildRequires: python-yaml

Source0: %{name}-%{version}.tar.gz

%define  cgcs_doc_deploy_dir /opt/deploy/cgcs_doc

%description
A yaml file description of the CGTS Alarms and Customer Logs generated by
the Titanium Cloud System.  Also included and used at build time is a simple syntax
checker to ensure no duplicate IDs are used, and generally the correct
field values are documented.

%prep
%setup

%install
CGCS_DOC_DEPLOY=$RPM_BUILD_ROOT/%{cgcs_doc_deploy_dir}
install -d $CGCS_DOC_DEPLOY
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/fm/
install -m 744 events.yaml $RPM_BUILD_ROOT/%{_sysconfdir}/fm/
install -m 644 events.yaml $CGCS_DOC_DEPLOY
install -m 755 checkEventYaml $CGCS_DOC_DEPLOY
install -m 644 parseEventYaml.py $CGCS_DOC_DEPLOY
install -m 644 check_missing_alarms.py $CGCS_DOC_DEPLOY
pushd $CGCS_DOC_DEPLOY
cp %{cgcs_doc_deploy_dir}/constants.py %{cgcs_doc_deploy_dir}/fmAlarm.h .
./checkEventYaml
rm constants.py* fmAlarm.h*
popd

%files
%license LICENSE
%defattr(-,root,root,-)
%{cgcs_doc_deploy_dir}/*
%{_sysconfdir}/fm/events.yaml

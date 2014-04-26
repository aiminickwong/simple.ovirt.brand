%define ovirt_brand_dir /usr/share/ovirt-engine/branding

Name:          simple.ovirt.brand
Version:       0.0.1
Release:        5%{?dist}

Summary:       oVirt Virtualization UI simple branding 
Group:         Documentation
License:       CC-BY-SA
URL:           http://www.github.com
Source:        %{name}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      
Provides:      eayun.brand

%description

This package contains the simple oVirt ui branding
file css jpg and html.

%prep
%setup -q -c $RPM_BUILD_DIR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{ovirt_brand_dir}/
cp -rf simple.ovirt.brand $RPM_BUILD_ROOT/%{ovirt_brand_dir}/.

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s /usr/share/ovirt-engine/branding/simple.ovirt.brand /etc/ovirt-engine/branding/01-simple.ovirt.brand
unlink /etc/ovirt-engine/branding/00-ovirt.brand

%files
%defattr(-,root,root,-)
%{ovirt_brand_dir}/simple.ovirt.brand/*

%changelog
* Sun Apr 27 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1-4
- change eayun documents url.
- add post install script for unlink ovirt default brand.

* Sun Apr 20 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1-4
- add download link and delete report link.

* Sun Apr 13 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1-3
- add more branding feature.

* Thu Apr 3 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1-2
- add EayunOS provider.

* Mon Jan 6 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1
- first


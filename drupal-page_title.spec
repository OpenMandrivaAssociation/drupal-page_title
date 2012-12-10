%define modname		page_title
%define drupal_version	7
%define module_version	2.7
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Page Title module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
The word "title" is a bit overloaded. Every piece of content in Drupal has
a title, and so does every page. The page title is the one found in the HTML
head inside the <title> tag. It is also used on SERPs (Search Engine Result
Pages) and can greatly enhance your websites SEO (Search Engine Optimization).

This module gives you granular control over the page title. You can specify
patterns for how the title should be structured and, on content creation pages,
specify the page title separately to the content's title.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%defattr(644,root,root,755)
%{_var}/www/drupal/modules/%{modname}
%doc CHANGELOG.txt README.txt


%changelog
* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.7-1
+ Revision: 798444
- imported package drupal-page_title


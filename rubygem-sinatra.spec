%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sinatra

%global bootstrap 0

Summary:        Ruby-based web application framework
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.4.6
Release:        5%{?dist}
Group:          Development/Languages
License:        MIT
URL: http://www.sinatrarb.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:       %{?scl_prefix_ruby}ruby(release)
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(rack) >= 1.4
Requires:       %{?scl_prefix}rubygem(rack) < 2
Requires:       %{?scl_prefix}rubygem(rack-protection) >= 1.2
Requires:       %{?scl_prefix}rubygem(rack-protection) < 2
Requires:       %{?scl_prefix}rubygem(tilt) >= 1.3.4
Requires:       %{?scl_prefix}rubygem(tilt) < 3
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  %{?scl_prefix}rubygem(rack) >= 1.4.0
BuildRequires:  %{?scl_prefix}rubygem(rack-test)
BuildRequires:  %{?scl_prefix}rubygem(rack-protection) >= 1.4.0
BuildRequires:  %{?scl_prefix}rubygem(tilt) >= 1.3
BuildRequires:  %{?scl_prefix}rubygem(tilt) < 3
BuildRequires:  %{?scl_prefix_ruby}rubygem(minitest) > 5
%endif
BuildArch:      noarch
Epoch:          1
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
Requires: %{?scl_prefix}runtime

%description
Sinatra is a DSL intended for quickly creating web-applications in Ruby
with minimal effort.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation

Requires:	%{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
# TODO: Is it worth of testing all the possible template engines integration?
%{?scl:scl enable %{scl} - << \EOF}
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -rv .%{gem_dir}/* %{buildroot}%{gem_dir}
rm %{buildroot}/%gem_instdir/.yardopts # Remove YARD configuration

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/sinatra.gemspec
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README.*.md
%doc %{gem_instdir}/AUTHORS.md
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/examples
%{gem_instdir}/Gemfile

%changelog
* Wed Apr 06 2016 Pavel Valena <pvalena@redhat.com> - 1:1.4.6-5
- Enable tests

* Wed Feb 24 2016 Pavel Valena <pvalena@redhat.com> - 1:1.4.6-4
- Update to 1.4.6

* Fri Jan 16 2015 Josef Stribny <jstribny@redhat.com> - 1:1.4.5-1
- Update to 1.4.5

* Thu Jan 30 2014 Vít Ondruch <vondruch@redhat.com> - 1:1.3.2-13
- Cleanly apply patch.

* Thu Aug 15 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.3.2-12
- Do not concatenate params. Fixes Foreman issues.
  - Resolves: rhbz#997018

* Thu Jun 13 2013 Josef Stribny <jstribny@redhat.com> - 1:1.3.2-12
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Patch RDoc tests

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-11
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-10
- Allowed test running.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-9
- Rebuilt for scl.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-8
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-7
- Rebuilt for Ruby 1.9.3.
- Introduced %%bootstrap macro to deal with dependency loop.

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-6
- Fixed Epoch once again

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-5
- Added Epoch to -dc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-4
- Rebuild for missing -dc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-3
- Added missing build requires

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Added tests
- Added doc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.6-1
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.1.2-3
- Added tilt dependency

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.1.2-1
- Version bump

* Thu Mar 25 2010 Michal Fojtik <mfojtik@redhat.com> - 1.0-1
- Sinatra now uses Tilt for rendering templates
- New helper methods
- New argument to specify the address to bind to
- Speed improvement in rendering templates

* Mon Feb 15 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.4-2
- Downgrade-Release

* Thu Jan 07 2010 Michal Fojtik <mfojtik@redhat.com> - 0.10.1-1
- Version-Release
- Added jp README

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-2
- Fix up documentation list
- Bring tests back
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-1
- Package generated by gem2rpm
- Don't ship tests
- Fix up License

%define	module	Gtk2-SourceView2
%define upstream_version 0.10

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	Perl module for the gtksourceview library
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{module}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	perl-ExtUtils-Depends 
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib > 1.00
BuildRequires:	perl-Gtk2 > 1.00
BuildRequires:	perl-devel

# for data files:
Requires:	gtksourceview
Requires:	gtk+2

%description
This module provides perl access to the libgtksourceview library, a library
that adds syntax highlighting, line numbers, and other programming-editor
features.
GtkSourceView specializes these features for a code editor.

%prep
%setup -q -n %{module}-%{upstream_version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
%makeinstall_std

%files
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*


%changelog
* Tue Jan 31 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.100.0-8
+ Revision: 770090
- cosmetics
- update license
- use pkgconfig() dependencies
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-5
+ Revision: 702779
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-4
+ Revision: 667189
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.100.0-3mdv2011.0
+ Revision: 564516
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 555930
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 553130
- update to 0.10

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 526445
- update to 0.07

* Wed Feb 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-2mdv2010.1
+ Revision: 510654
- change requires:

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 498977
- update to 0.06

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 469438
- update to 0.05

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 466454
- update to 0.04

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 463922
- update to 0.03

* Thu Nov 05 2009 Thierry Vignaud <tv@mandriva.org> 0.02-1mdv2010.1
+ Revision: 460432
- import perl-Gtk2-SourceView2


* Thu Nov 05 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.02-1mdv2010.0
- initial release

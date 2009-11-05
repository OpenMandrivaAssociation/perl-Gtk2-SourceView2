%define module Gtk2-SourceView2

Summary: Perl module for the gtksourceview library
Name:    perl-%module
Version: 0.02
Release: %mkrel 1
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel 
BuildRequires: perl-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Glib > 1.00
BuildRequires: perl-Gtk2 > 1.00
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: libgnomeprintui2-2-devel
BuildRequires: libgtksourceview-2.0-devel >= 0.7 
# for data files:
Requires: gtksourceview1

Requires: gtk+2

%description
This module provides perl access to the libgtksourceview library, a library
that adds syntax highlighting, line numbers, and other programming-editor
features.
GtkSourceView specializes these features for a code editor.

%prep
%setup -q -n %module-%version
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*





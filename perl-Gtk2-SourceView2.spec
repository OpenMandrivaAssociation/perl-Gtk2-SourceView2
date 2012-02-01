%define	module	Gtk2-SourceView2
%define upstream_version 0.10

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	8

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
%make
#%make test || :

%install
%makeinstall_std

%files
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*

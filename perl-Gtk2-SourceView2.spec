%define	module	Gtk2-SourceView2
%define modver	0.10

Summary:	Perl module for the gtksourceview library
Name:		perl-%{module}
Version:	%perl_convert_version %{modver}
Release:	19
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{module}-%{modver}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	perl-ExtUtils-Depends 
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib > 1.00
BuildRequires:	perl-Gtk2 > 1.00
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
# no needed
#BuildRequires:	pkgconfig(libgnomeprintui-2.2)
# for data files:
Requires:	gtksourceview
Requires:	gtk+2

%description
This module provides perl access to the libgtksourceview library, a library
that adds syntax highlighting, line numbers, and other programming-editor
features.
GtkSourceView specializes these features for a code editor.

%prep
%setup -qn %{module}-%{modver}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%check
#%make test || :

%install
%makeinstall_std

%files
%doc examples
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*


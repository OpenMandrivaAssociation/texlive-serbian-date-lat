%global tl_name serbian-date-lat
%global tl_revision 23446

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Updated date typesetting for Serbian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/serbian/filipovic/serbian-date-lat
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Babel defines dates for Serbian texts, in Latin script. The style it
uses does not match current practices. The present package defines a
\date command that solves the problem.


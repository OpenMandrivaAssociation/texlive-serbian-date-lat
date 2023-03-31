Name:		texlive-serbian-date-lat
Version:	23446
Release:	2
Summary:	Updated date typesetting for Serbian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbian-date-lat
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Babel defines dates for Serbian texts, in Latin script. The
style it uses does not match current practices. The present
package defines a \date command that solves the problem.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-date-lat/serbian-date-lat.sty
%doc %{_texmfdistdir}/doc/latex/serbian-date-lat/README
%doc %{_texmfdistdir}/doc/latex/serbian-date-lat/SerbianDateLat.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-date-lat/SerbianDateLat.tex
%doc %{_texmfdistdir}/doc/latex/serbian-date-lat/TestDateLat.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-date-lat/TestDateLat.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

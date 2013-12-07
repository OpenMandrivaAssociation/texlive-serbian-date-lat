# revision 23446
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/serbian-date-lat
# catalog-date 2011-06-24 10:29:05 +0200
# catalog-license gpl2
# catalog-version undef
Name:		texlive-serbian-date-lat
Version:	20110624
Release:	3
Summary:	Updated date typesetting for Serbian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbian-date-lat
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-date-lat.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110624-2
+ Revision: 755912
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110624-1
+ Revision: 719510
- texlive-serbian-date-lat
- texlive-serbian-date-lat
- texlive-serbian-date-lat
- texlive-serbian-date-lat


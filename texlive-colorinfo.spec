# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/colorinfo
# catalog-date 2007-02-03 12:09:11 +0100
# catalog-license lppl
# catalog-version 0.3c
Name:		texlive-colorinfo
Version:	0.3c
Release:	6
Summary:	Retrieve colour model and values for defined colours
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorinfo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive colorinfo package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colorinfo/colorinfo.sty
%doc %{_texmfdistdir}/doc/latex/colorinfo/README
%doc %{_texmfdistdir}/doc/latex/colorinfo/colorinfo-test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3c-2
+ Revision: 750372
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3c-1
+ Revision: 718097
- texlive-colorinfo
- texlive-colorinfo
- texlive-colorinfo
- texlive-colorinfo
- texlive-colorinfo


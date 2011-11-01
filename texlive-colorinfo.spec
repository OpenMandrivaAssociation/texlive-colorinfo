Name:		texlive-colorinfo
Version:	0.3c
Release:	1
Summary:	Retrieve colour model and values for defined colours
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorinfo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive colorinfo package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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

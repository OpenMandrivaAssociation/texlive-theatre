Name:		texlive-theatre
Version:	45363
Release:	2
Summary:	A sophisticated package for typesetting stage plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/theatre
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theatre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theatre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables the user to typeset stage plays in a way
that permits to create highly customized printouts for each
actor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/theatre

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

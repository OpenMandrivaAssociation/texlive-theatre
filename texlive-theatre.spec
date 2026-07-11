%global tl_name theatre
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A sophisticated package for typesetting stage plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/theatre
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theatre.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theatre.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the user to typeset stage plays in a way that
permits to create highly customized printouts for each actor.


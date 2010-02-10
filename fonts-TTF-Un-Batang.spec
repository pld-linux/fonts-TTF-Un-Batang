Summary:	Free TrueType font for Hangul
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla Hangyl
Name:		fonts-TTF-Un-Batang
Version:	0613
Release:	1
# license info available in CVS
License:	GPL v2
Group:		Fonts
#Source0Download:	http://kldp.net/projects/unfonts/download/4706?filename=UnBatang_%{version}.ttf
Source0:	UnBatang_%{version}.ttf
# Source0-md5:	0cb2b8a3cf6db627e52ded1b52906787
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This font includes the new characters in the Jamo block, and all the
characters in the new Hangul Jamo Extended-A and Hangul Jamo
Extended-B blocks.

#%%description -l pl.UTF-8
# TODO

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/UnBatang*.ttf

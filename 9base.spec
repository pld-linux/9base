Summary:	Port of original Plan 9 userland tools to Unix
Summary(pl.UTF-8):	Uniksowy port oryginalnych narzędzi przestrzeni użytkownika systemu Plan 9
Name:		9base
Version:	2
Release:	0.1
License:	mostly Lucent Public License, Version 1.02
Group:		Applications
Source0:	http://wmii.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	f9d30509996ec178702af20fec986e9d
Patch0:		%{name}-rename.patch
URL:		http://wmii.de/index.php/WMII/9base
Provides:	rc
Obsoletes:	rc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
9base is a port of following original Plan 9 userland tools to Unix:
awk, basename, bc, cat, cleanname, date, dc, echo, grep, mk, rc, sed,
seq, sleep, sort, tee, test, touch, tr, uniq, yacc.

In PLD all tools was renamed with prefix 9 for not to conflict with
system tools.

%description -l pl.UTF-8
9base to uniksowy port następujących oryginalnych narzędzi przestrzeni
użytkownika systemu Plan 9:
awk, basename, bc, cat, cleanname, date, dc, echo, grep, mk, rc, sed,
seq, sleep, sort, tee, test, touch, tr, uniq, yacc.

W PLD wszystkim narzędziom zmieniono nazwę dodając przedrostek 9, aby
uniknąć konfliktu z narzędziami systemowymi.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/9rcmain
%attr(755,root,root) %{_bindir}/9*
%{_mandir}/man1/9*.1*
%{_mandir}/man7/9*.7*

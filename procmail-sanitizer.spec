Summary:	Enhancing E-Mail Security With Procmail
Summary(pl):	ZwiÍkszanie bezpieczeÒstwa poczty elektronicznej przy pomocy procmaila
Name:		procmail-sanitizer
Version:	1.133
Release:	1
License:	GPL
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sl):	Programi/Sistem
Group(sv):	Till‰mpningar/System
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Û…”‘≈Õ¡
Source0:	http://www.impsec.org/email-tools/%{name}.tar.gz
URL:		ftp://ftp.rubyriver.com/pub/jhardin/antispam/procmail-security.html
Requires:	procmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/procmail

%description
The Sanitizer is a tool for preventing attacks on your computer's
security via email messages. It has proven to be very effective
against the latest crop of email worms that have gotten so much
attention in the popular press.

%description -l pl
Sanitizer to narzÍdzie do zapobiegania atakom poprzez pocztÍ
elektroniczn±. Okaza≥o siÍ bardzo efektywne przeciwko ostatniemu
wysypowi robakÛw pocztowych.

%prep
%setup  -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install html-trap.procmail $RPM_BUILD_ROOT%{_sysconfdir}
install html-trap.procmail.nomacroscan $RPM_BUILD_ROOT%{_sysconfdir}
install poisoned-files $RPM_BUILD_ROOT%{_sysconfdir}
install security-optout.procmail $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.txt.gz
%{_sysconfdir}/*

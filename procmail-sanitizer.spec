Summary:	Enhancing E-Mail Security With Procmail
Summary(pl):	Zwiêkszanie bezpieczeñstwa poczty elektronicznej przy pomocy procmaila
Name:		procmail-sanitizer
Version:	1.142
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.impsec.org/email-tools/%{name}.tar.gz
# Source0-md5:	9bc90ce7919202263566d1161d23b130
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
Sanitizer to narzêdzie do zapobiegania atakom poprzez pocztê
elektroniczn±. Okaza³o siê bardzo efektywne przeciwko ostatniemu
wysypowi robaków pocztowych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install html-trap.procmail $RPM_BUILD_ROOT%{_sysconfdir}
install html-trap.procmail.nomacroscan $RPM_BUILD_ROOT%{_sysconfdir}
install poisoned-files $RPM_BUILD_ROOT%{_sysconfdir}
install security-optout.procmail $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.txt
%{_sysconfdir}/*

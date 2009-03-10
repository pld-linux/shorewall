Summary:	Shoreline Firewall - an iptables-based firewall for Linux systems
Summary(pl.UTF-8):	Shoreline Firewall - zapora sieciowa oparta na iptables
Name:		shorewall
Version:	4.2.6
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://shorewall.net/pub/shorewall/4.2/shorewall-%{version}/%{name}-common-%{version}.tgz
# Source0-md5:	9b91dc35068ccc0ba308a30947cafe48
Source1:	%{name}.init
Patch0:		%{name}-config.patch
URL:		http://www.shorewall.net/
Requires(post,preun):	/sbin/chkconfig
Requires:	bash
Requires:	iproute2
Requires:	iptables
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-common-%{version}-root-%(id -u -n)

%description
The Shoreline Firewall, more commonly known as "Shorewall", is an easy
to use Netfilter (iptables) based firewall that can be used on a
dedicated firewall system, a multi-function gateway/ router/server or
on a standalone GNU/Linux system.

%description -l pl.UTF-8
Pakiet Shoreline Firewall, nazywany zwykle Shorewall, jest zaporą
sieciową opartą na wbudowanych w jądro Linuksa mechanizmach
filtrowania pakietów sieciowych (iptables). Shorewall jest bardzo
wszechstronny i może być wykorzystany jako zapora sieciowa,
wielofunkcyjna brama lub router. Pakiet ten łączy w sobie elastyczność
i prostotę konfiguracji.

%prep
%setup -q -n %{name}-common-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/shorewall

export PREFIX=$RPM_BUILD_ROOT ; \
export OWNER=`id -n -u` ; \
export GROUP=`id -n -g` ;\
./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add shorewall

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del shorewall
fi

%files
%defattr(644,root,root,755)
%doc INSTALL releasenotes.txt tunnel Samples/*
%attr(700,root,root) %dir /var/lib/shorewall
%attr(754,root,root) /sbin/shorewall
%attr(754,root,root) /etc/rc.d/init.d/shorewall
%{_mandir}/man5/%{name}*
%{_mandir}/man8/%{name}*
#%%{_datadir}/%{name}/*

%attr(700,root,root) %dir %{_sysconfdir}/shorewall
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/shorewall.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/zones
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/policy
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/interfaces
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/rules
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/nat
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/netmap
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/params
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/proxyarp
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/routestopped
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/maclist
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/masq
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tcrules
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tos
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tunnels
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/hosts
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/blacklist
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/init
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/initdone
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/start
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/stop
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/stopped
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/ecn
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/accounting
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/actions
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/ipsec
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/continue
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/started
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/providers
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/restored
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/route_rules
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tcclasses
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tcdevices
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/tcfilters

%attr(700,root,root) %dir %{_datadir}/shorewall
%attr(600,root,root) %{_datadir}/shorewall/version
%attr(600,root,root) %{_datadir}/shorewall/actions.std
%attr(600,root,root) %{_datadir}/shorewall/action.Drop
%attr(600,root,root) %{_datadir}/shorewall/action.Reject
%attr(600,root,root) %{_datadir}/shorewall/action.template
%attr(754,root,root) %{_datadir}/shorewall/lib.base
%attr(754,root,root) %{_datadir}/shorewall/lib.cli
%attr(754,root,root) %{_datadir}/shorewall/lib.config
%attr(754,root,root) %{_datadir}/shorewall/lib.dynamiczones
%attr(600,root,root) %{_datadir}/shorewall/macro.AllowICMPs
%attr(600,root,root) %{_datadir}/shorewall/macro.Amanda
%attr(600,root,root) %{_datadir}/shorewall/macro.Auth
%attr(600,root,root) %{_datadir}/shorewall/macro.BitTorrent
%attr(600,root,root) %{_datadir}/shorewall/macro.BitTorrent32
%attr(600,root,root) %{_datadir}/shorewall/macro.CVS
%attr(600,root,root) %{_datadir}/shorewall/macro.DAAP
%attr(600,root,root) %{_datadir}/shorewall/macro.DCC
%attr(600,root,root) %{_datadir}/shorewall/macro.DNS
%attr(600,root,root) %{_datadir}/shorewall/macro.Drop
%attr(600,root,root) %{_datadir}/shorewall/macro.Distcc
%attr(600,root,root) %{_datadir}/shorewall/macro.DropDNSrep
%attr(600,root,root) %{_datadir}/shorewall/macro.DropUPnP
%attr(600,root,root) %{_datadir}/shorewall/macro.FTP
%attr(600,root,root) %{_datadir}/shorewall/macro.GNUnet
%attr(600,root,root) %{_datadir}/shorewall/macro.Gnutella
%attr(600,root,root) %{_datadir}/shorewall/macro.Edonkey
%attr(600,root,root) %{_datadir}/shorewall/macro.Finger
%attr(600,root,root) %{_datadir}/shorewall/macro.Git
%attr(600,root,root) %{_datadir}/shorewall/macro.GRE
%attr(600,root,root) %{_datadir}/shorewall/macro.ICQ
%attr(600,root,root) %{_datadir}/shorewall/macro.IRC
%attr(600,root,root) %{_datadir}/shorewall/macro.HTTP
%attr(600,root,root) %{_datadir}/shorewall/macro.HTTPS
%attr(600,root,root) %{_datadir}/shorewall/macro.IMAP
%attr(600,root,root) %{_datadir}/shorewall/macro.IMAPS
%attr(600,root,root) %{_datadir}/shorewall/macro.IPIP
%attr(600,root,root) %{_datadir}/shorewall/macro.IPP
%attr(600,root,root) %{_datadir}/shorewall/macro.IPPserver
%attr(600,root,root) %{_datadir}/shorewall/macro.IPsec
%attr(600,root,root) %{_datadir}/shorewall/macro.IPsecah
%attr(600,root,root) %{_datadir}/shorewall/macro.IPsecnat
%attr(600,root,root) %{_datadir}/shorewall/macro.JabberPlain
%attr(600,root,root) %{_datadir}/shorewall/macro.JabberSecure
%attr(600,root,root) %{_datadir}/shorewall/macro.Jabberd
%attr(600,root,root) %{_datadir}/shorewall/macro.JAP
%attr(600,root,root) %{_datadir}/shorewall/macro.Jetdirect
%attr(600,root,root) %{_datadir}/shorewall/macro.L2TP
%attr(600,root,root) %{_datadir}/shorewall/macro.LDAP
%attr(600,root,root) %{_datadir}/shorewall/macro.LDAPS
%attr(600,root,root) %{_datadir}/shorewall/macro.Mail
%attr(600,root,root) %{_datadir}/shorewall/macro.MySQL
%attr(600,root,root) %{_datadir}/shorewall/macro.NNTP
%attr(600,root,root) %{_datadir}/shorewall/macro.NNTPS
%attr(600,root,root) %{_datadir}/shorewall/macro.NTP
%attr(600,root,root) %{_datadir}/shorewall/macro.NTPbrd
%attr(600,root,root) %{_datadir}/shorewall/macro.OpenVPN
%attr(600,root,root) %{_datadir}/shorewall/macro.PCA
%attr(600,root,root) %{_datadir}/shorewall/macro.POP3
%attr(600,root,root) %{_datadir}/shorewall/macro.POP3S
%attr(600,root,root) %{_datadir}/shorewall/macro.Ping
%attr(600,root,root) %{_datadir}/shorewall/macro.PostgreSQL
%attr(600,root,root) %{_datadir}/shorewall/macro.PPtP
%attr(600,root,root) %{_datadir}/shorewall/macro.Printer
%attr(600,root,root) %{_datadir}/shorewall/macro.RDP
%attr(600,root,root) %{_datadir}/shorewall/macro.Rdate
%attr(600,root,root) %{_datadir}/shorewall/macro.Reject
%attr(600,root,root) %{_datadir}/shorewall/macro.Rfc1918
%attr(600,root,root) %{_datadir}/shorewall/macro.RNDC
%attr(600,root,root) %{_datadir}/shorewall/macro.Rsync
%attr(600,root,root) %{_datadir}/shorewall/macro.SANE
%attr(600,root,root) %{_datadir}/shorewall/macro.SixXS
%attr(600,root,root) %{_datadir}/shorewall/macro.SMB
%attr(600,root,root) %{_datadir}/shorewall/macro.SMBBI
%attr(600,root,root) %{_datadir}/shorewall/macro.SMBswat
%attr(600,root,root) %{_datadir}/shorewall/macro.SMTP
%attr(600,root,root) %{_datadir}/shorewall/macro.SMTPS
%attr(600,root,root) %{_datadir}/shorewall/macro.SNMP
%attr(600,root,root) %{_datadir}/shorewall/macro.SPAMD
%attr(600,root,root) %{_datadir}/shorewall/macro.SSH
%attr(600,root,root) %{_datadir}/shorewall/macro.SVN
%attr(600,root,root) %{_datadir}/shorewall/macro.Submission
%attr(600,root,root) %{_datadir}/shorewall/macro.Syslog
%attr(600,root,root) %{_datadir}/shorewall/macro.TFTP
%attr(600,root,root) %{_datadir}/shorewall/macro.Telnet
%attr(600,root,root) %{_datadir}/shorewall/macro.Telnets
%attr(600,root,root) %{_datadir}/shorewall/macro.Time
%attr(600,root,root) %{_datadir}/shorewall/macro.Trcrt
%attr(600,root,root) %{_datadir}/shorewall/macro.VNC
%attr(600,root,root) %{_datadir}/shorewall/macro.VNCL
%attr(600,root,root) %{_datadir}/shorewall/macro.Whois
%attr(600,root,root) %{_datadir}/shorewall/macro.Web
%attr(600,root,root) %{_datadir}/shorewall/macro.Webmin
%attr(600,root,root) %{_datadir}/shorewall/macro.template
%attr(754,root,root) %{_datadir}/shorewall/wait4ifup
%dir %{_datadir}/shorewall/configfiles
%attr(600,root,root) %{_datadir}/shorewall/configfiles/accounting
%attr(600,root,root) %{_datadir}/shorewall/configfiles/actions
%attr(600,root,root) %{_datadir}/shorewall/configfiles/blacklist
%attr(600,root,root) %{_datadir}/shorewall/configfiles/continue
%attr(600,root,root) %{_datadir}/shorewall/configfiles/ecn
%attr(600,root,root) %{_datadir}/shorewall/configfiles/hosts
%attr(600,root,root) %{_datadir}/shorewall/configfiles/init
%attr(600,root,root) %{_datadir}/shorewall/configfiles/initdone
%attr(600,root,root) %{_datadir}/shorewall/configfiles/interfaces
%attr(600,root,root) %{_datadir}/shorewall/configfiles/ipsec
%attr(600,root,root) %{_datadir}/shorewall/configfiles/maclist
%attr(600,root,root) %{_datadir}/shorewall/configfiles/masq
%attr(600,root,root) %{_datadir}/shorewall/configfiles/nat
%attr(600,root,root) %{_datadir}/shorewall/configfiles/netmap
%attr(600,root,root) %{_datadir}/shorewall/configfiles/params
%attr(600,root,root) %{_datadir}/shorewall/configfiles/policy
%attr(600,root,root) %{_datadir}/shorewall/configfiles/providers
%attr(600,root,root) %{_datadir}/shorewall/configfiles/proxyarp
%attr(600,root,root) %{_datadir}/shorewall/configfiles/restored
%attr(600,root,root) %{_datadir}/shorewall/configfiles/route_rules
%attr(600,root,root) %{_datadir}/shorewall/configfiles/routestopped
%attr(600,root,root) %{_datadir}/shorewall/configfiles/rules
%attr(600,root,root) %{_datadir}/shorewall/configfiles/shorewall.conf
%attr(600,root,root) %{_datadir}/shorewall/configfiles/start
%attr(600,root,root) %{_datadir}/shorewall/configfiles/started
%attr(600,root,root) %{_datadir}/shorewall/configfiles/stop
%attr(600,root,root) %{_datadir}/shorewall/configfiles/stopped
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tcclasses
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tcdevices
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tcfilters
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tcrules
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tos
%attr(600,root,root) %{_datadir}/shorewall/configfiles/tunnels
%attr(600,root,root) %{_datadir}/shorewall/configfiles/zones
%{_datadir}/shorewall/functions
%attr(754,root,root) %{_datadir}/shorewall/modules
%attr(754,root,root) %{_datadir}/shorewall/firewall
%attr(600,root,root) %{_datadir}/shorewall/rfc1918
%attr(600,root,root) %{_datadir}/shorewall/configpath

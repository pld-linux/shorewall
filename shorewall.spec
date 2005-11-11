Summary:	Shoreline Firewall - an iptables-based firewall for Linux systems
Summary(pl):	Shoreline Firewall - zapora sieciowa oparta na iptables
Name:		shorewall
Version:	2.4.6
Release:	0.2
License:	GPL
Group:		Networking/Utilities
Source0:	http://shorewall.net/pub/shorewall/2.4/shorewall-%{version}/%{name}-%{version}.tgz
# Source0-md5:	0e2634b1670c2708218f4dde68253668
Source1:	%{name}.init
Patch0:		%{name}-config.patch
URL:		http://www.shorewall.net/
Requires:	iproute2
Requires:	iptables
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Shoreline Firewall, more commonly known as "Shorewall", is an easy
to use Netfilter (iptables) based firewall that can be used on a
dedicated firewall system, a multi-function gateway/ router/server or
on a standalone GNU/Linux system.

%description -l pl
Pakiet Shoreline Firewall, nazywany zwykle Shorewall, jest zapor±
sieciow± opart± na wbudowanych w j±dro Linuksa mechanizmach
filtrowania pakietów sieciowych (iptables). Shorewall jest bardzo
wszechstronny i mo¿e byæ wykorzystany jako zapora sieciowa,
wielofunkcyjna brama lub router. Pakiet ten ³±czy w sobie elastyczno¶æ
i prostotê konfiguracji.

%prep
%setup -q
%patch -p1

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
%doc changelog.txt INSTALL releasenotes.txt tunnel
%attr(754,root,root) /etc/rc.d/init.d/shorewall
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
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/modules
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
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/shorewall/routes

%attr(754,root,root) /sbin/shorewall

%attr(700,root,root) %dir %{_datadir}/shorewall
%attr(600,root,root) %{_datadir}/shorewall/version
%attr(600,root,root) %{_datadir}/shorewall/actions.std
%attr(600,root,root) %{_datadir}/shorewall/action.AllowAuth
%attr(600,root,root) %{_datadir}/shorewall/action.AllowDNS
%attr(600,root,root) %{_datadir}/shorewall/action.AllowFTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowICMPs
%attr(600,root,root) %{_datadir}/shorewall/action.AllowIMAP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowNNTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowNTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowNTPbrd
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPCA
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPing
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPOP3
%attr(600,root,root) %{_datadir}/shorewall/action.AllowRdate
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSMB
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSMTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSNMP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSSH
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSubmission
%attr(600,root,root) %{_datadir}/shorewall/action.AllowTelnet
%attr(600,root,root) %{_datadir}/shorewall/action.AllowTrcrt
%attr(600,root,root) %{_datadir}/shorewall/action.AllowVNC
%attr(600,root,root) %{_datadir}/shorewall/action.AllowVNCL
%attr(600,root,root) %{_datadir}/shorewall/action.AllowWeb
%attr(600,root,root) %{_datadir}/shorewall/action.Drop
%attr(600,root,root) %{_datadir}/shorewall/action.DropDNSrep
%attr(600,root,root) %{_datadir}/shorewall/action.DropPing
%attr(600,root,root) %{_datadir}/shorewall/action.DropSMB
%attr(600,root,root) %{_datadir}/shorewall/action.DropUPnP
%attr(600,root,root) %{_datadir}/shorewall/action.Reject
%attr(600,root,root) %{_datadir}/shorewall/action.RejectAuth
%attr(600,root,root) %{_datadir}/shorewall/action.RejectSMB
%attr(600,root,root) %{_datadir}/shorewall/action.template
%attr(644,root,root) %{_datadir}/shorewall/functions
%attr(754,root,root) %{_datadir}/shorewall/firewall
%attr(754,root,root) %{_datadir}/shorewall/help
%attr(600,root,root) %{_datadir}/shorewall/rfc1918
%attr(600,root,root) %{_datadir}/shorewall/bogons
%attr(600,root,root) %{_datadir}/shorewall/configpath

%attr(700,root,root) %dir /var/lib/shorewall

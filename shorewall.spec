Summary:	Shoreline Firewall is an iptables-based firewall for Linux systems
Summary(pl):	Shoreline Firewall jest ¶cian± ogniow± opart± na iptables
Name:		shorewall
Version:	2.0.7
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://shorewall.net/pub/shorewall/2.0/%{name}-%{version}/%{name}-%{version}.tgz
# Source0-md5: 95587aa6936fd8f242db914bad4adf12
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://www.shorewall.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	iptables
Requires:	iproute2

%description
The Shoreline Firewall, more commonly known as "Shorewall", is an easy
to ues Netfilter (iptables) based firewall that can be used on a
dedicated firewall system, a multi-function gateway/ router/server or
on a standalone GNU/Linux system.

%description -l pl
Pakiet Shoreline Firewall nazywany zwykle Shorewall jest ¶cian±
ogniow± opart± na wbudowanych w j±dro Linuksa mechanizmach filtrowania
pakietów sieciowych (iptables). Shorewall jest bardzo wszechstonny i
mo¿e byæ wykorzystany jako ¶ciana ogniowa, wielofunkcyjna brama lub
router. Pakiet ten ³±czy w sobie elastyczno¶æ i prostotê konfiguracji.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/shorewall
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/shorewall
export PREFIX=$RPM_BUILD_ROOT ; \
export OWNER=`id -n -u` ; \
export GROUP=`id -n -g` ;\
./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add shorewall
if [ -f /var/lock/subsys/shorewall ]; then
	%{_sysconfdir}/rc.d/init.d/shorewall restart >&2
else
	echo "Run \"%{_sysconfdir}/rc.d/init.d/shorewall start\" to start shorewall."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/shorewall ]; then
		%{_sysconfdir}/rc.d/init.d/shorewall stop>&2
	fi
	/sbin/chkconfig --del shorewall
fi

%files
%defattr(644,root,root,755)
%doc changelog.txt INSTALL releasenotes.txt tunnel
%attr(0544,root,root) %{_sysconfdir}/rc.d/init.d/shorewall
%attr(0700,root,root) %dir %{_sysconfdir}/shorewall
%attr(0700,root,root) %dir %{_datadir}/shorewall
%attr(0700,root,root) %dir /var/lib/shorewall
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/shorewall
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/shorewall.conf
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/zones
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/policy
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/interfaces
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/rules
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/nat
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/netmap
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/params
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/proxyarp
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/routestopped
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/maclist
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/masq
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/modules
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tcrules
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tos
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tunnels
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/hosts
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/blacklist
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/init
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/initdone
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/start
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/stop
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/stopped
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/ecn
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/accounting
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/actions

%attr(0544,root,root) /sbin/shorewall

%attr(0600,root,root) %{_datadir}/shorewall/version
%attr(0600,root,root) %{_datadir}/shorewall/actions.std
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowAuth
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowDNS
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowFTP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowIMAP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowNNTP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowNTP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowPCA
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowPing
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowPOP3
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowRdate
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowSMB
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowSMTP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowSNMP
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowSSH
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowTelnet
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowTrcrt
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowVNC
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowVNCL
%attr(0600,root,root) %{_datadir}/shorewall/action.AllowWeb
%attr(0600,root,root) %{_datadir}/shorewall/action.Drop
%attr(0600,root,root) %{_datadir}/shorewall/action.DropDNSrep
%attr(0600,root,root) %{_datadir}/shorewall/action.DropPing
%attr(0600,root,root) %{_datadir}/shorewall/action.DropSMB
%attr(0600,root,root) %{_datadir}/shorewall/action.DropUPnP
%attr(0600,root,root) %{_datadir}/shorewall/action.Reject
%attr(0600,root,root) %{_datadir}/shorewall/action.RejectAuth
%attr(0600,root,root) %{_datadir}/shorewall/action.RejectSMB
%attr(0600,root,root) %{_datadir}/shorewall/action.template
%attr(0444,root,root) %{_datadir}/shorewall/functions
%attr(0544,root,root) %{_datadir}/shorewall/firewall
%attr(0544,root,root) %{_datadir}/shorewall/help
%attr(0600,root,root) %{_datadir}/shorewall/rfc1918
%attr(0600,root,root) %{_datadir}/shorewall/bogons
%attr(0600,root,root) %{_datadir}/shorewall/configpath

Summary:	Shoreline Firewall - an iptables-based firewall for Linux systems
Summary(pl):	Shoreline Firewall - ¶ciana przeciwogniowa oparta na iptables
Name:		shorewall
Version:	2.0.13
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://shorewall.net/pub/shorewall/2.0/%{name}-%{version}/%{name}-%{version}.tgz
# Source0-md5:	b3656ec857d55878b739d8f903de957d
Source1:	%{name}.init
Source2:	%{name}.sysconfig
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
Pakiet Shoreline Firewall nazywany zwykle Shorewall jest ¶cian±
ogniow± opart± na wbudowanych w j±dro Linuksa mechanizmach filtrowania
pakietów sieciowych (iptables). Shorewall jest bardzo wszechstronny i
mo¿e byæ wykorzystany jako ¶ciana ogniowa, wielofunkcyjna brama lub
router. Pakiet ten ³±czy w sobie elastyczno¶æ i prostotê konfiguracji.

%prep
%setup -q
%patch -p1

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
%attr(754,root,root) /etc/rc.d/init.d/shorewall
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/shorewall
%attr(700,root,root) %dir %{_sysconfdir}/shorewall
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/shorewall.conf
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/zones
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/policy
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/interfaces
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/rules
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/nat
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/netmap
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/params
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/proxyarp
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/routestopped
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/maclist
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/masq
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/modules
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tcrules
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tos
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/tunnels
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/hosts
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/blacklist
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/init
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/initdone
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/start
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/stop
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/stopped
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/ecn
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/accounting
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/shorewall/actions

%attr(754,root,root) /sbin/shorewall

%attr(700,root,root) %dir %{_datadir}/shorewall
%attr(600,root,root) %{_datadir}/shorewall/version
%attr(600,root,root) %{_datadir}/shorewall/actions.std
%attr(600,root,root) %{_datadir}/shorewall/action.AllowAuth
%attr(600,root,root) %{_datadir}/shorewall/action.AllowDNS
%attr(600,root,root) %{_datadir}/shorewall/action.AllowFTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowIMAP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowNNTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowNTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPCA
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPing
%attr(600,root,root) %{_datadir}/shorewall/action.AllowPOP3
%attr(600,root,root) %{_datadir}/shorewall/action.AllowRdate
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSMB
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSMTP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSNMP
%attr(600,root,root) %{_datadir}/shorewall/action.AllowSSH
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

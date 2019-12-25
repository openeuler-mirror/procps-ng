Name: 		procps-ng
Version: 	3.3.15
Release:    10
Summary: 	Utilities that provide system information.
License: 	GPL+ and GPLv2 and GPLv2+ and GPLv3+ and LGPLv2+
URL: 		https://sourceforge.net/projects/procps-ng/

Source0: 	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: 	README.md
Source2: 	README.top

Patch9000: 	feature-add-options-M-and-N-for-top.patch
Patch9001: 	bugfix-top-exit-with-error-when-pid-overflow.patch
Patch6002: 	top-fix-iokey-flaw-preventing-proper-translations.patch
Patch6003: 	Possible-segfault-in-file2strvec-introduced-by-lates.patch
Patch6004:	top-don-t-mess-with-groff-line-length-in-man-documen.patch
Patch6005:	top-add-another-field-sanity-check-in-config_file.patch
Patch6006:	top-prevent-buffer-overruns-in-inspection_utility.patch
Patch6007:	docs-Tidying-of-ps-kill-and-skill-manpages.patch
Patch6008:	library-avoid-problems-involving-supgid-mishandling.patch
Patch6009:	w-Prevent-out-of-bounds-reads-in-print_display_or_in.patch
Patch6010:	w-Clamp-maxcmd-to-the-MIN-MAX_CMD_WIDTH-range.patch
Patch6011:	vmstat-getopt-returns-1-when-done-not-EOF.patch
Patch6012:	vmstat-Replace-memcmp-with-strncmp.patch
Patch6013:	vmstat-Check-return-values-of-localtime-and-strftime.patch
Patch6014:	vmstat-Prevent-out-of-bounds-writes-in-new_header-an.patch
Patch6015:	top-the-define-PRETEND2_5_X-was-found-to-be-broken.patch
Patch6016:	procio-use-the-user-supplied-delimiter-to-split-larg.patch
Patch6017:	procio-fix-potential-out-of-bounds-access-when-write.patch
Patch6018:	sysctl-do-not-report-set-key-in-case-close_stream-fa.patch

BuildRequires: 	ncurses-devel libtool autoconf automake gcc gettext-devel systemd-devel

Provides: 	procps = %{version}-%{release}
Provides: 	%{name}	

%description
The procps package contains a set of system utilities that provide
system information. Procps includes ps, free, skill, pkill, pgrep,
snice, tload, top, uptime, vmstat, pidof, pmap, slabtop, w, watch
and pwdx.

%package 	devel
Summary:  	The devel for %{name} 
Requires: 	%{name} = %{version}-%{release}
Provides: 	procps-devel = %{version}-%{release}

%description 	devel
System and process monitoring utilities

%package 	i18n
Summary:  	Internationalization pack for %{name} 
Requires: 	%{name} = %{version}-%{release}
BuildArch: 	noarch

%description 	i18n
The package is used for the Internationalization of %{name}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

cp -p %{SOURCE1} .
cp -p %{SOURCE2} top/

%build
autoreconf -ivf

%configure  --exec-prefix=/ --docdir=/unwanted --disable-w-from --disable-kill --enable-watch8bit \
           --enable-skill --enable-sigwinch --enable-libselinux --with-systemd --disable-modern-top

make CFLAGS="%{optflags}"

%install
%make_install

find man-po/ -type d -maxdepth 1 -mindepth 1 | while read dirname; do cp -a $dirname %{buildroot}%{_mandir}/ ; done

%find_lang %{name} --all-name --with-man

ln -s %{_bindir}/pidof %{buildroot}%{_sbindir}/pidof

%ldconfig_scriptlets

%files
%doc COPYING COPYING.LIB
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.LIB
%{_libdir}/libprocps.so.*
%{_bindir}/*
%{_sbindir}/*
%exclude %{_libdir}/libprocps.la
%exclude /unwanted/*
%exclude %{_libdir}/*.a

%files devel
%doc COPYING COPYING.LIB
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.LIB
%{_libdir}/libprocps.so
%{_libdir}/pkgconfig/libprocps.pc
%{_includedir}/proc

%files i18n -f %{name}.lang

%files help
%doc AUTHORS Documentation/bugs.md Documentation/FAQ NEWS README.md top/README.top Documentation/TODO
%{_mandir}/man*


%changelog
* Mon Dec 23 2019 wangshuo <wangshuo47@huawei.com> - 3.3.15-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: add liscense to main and devel package.

* Thu Dec 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.3.15-9
- Fix typo

* Fri Mar 15 2019 xuwei<xuwei58@huawei.com> - 3.3.15-8
- Type:bugfix
- ID:NA
- SUG:restart
- DEC:top: don't mess with groff line length in man document
      top: add another field sanity check in 'config_file()'
      top: prevent buffer overruns in 'inspection_utility()'
      docs: Tidying of ps,kill and skill manpages
      library: avoid problems involving 'supgid' mishandling
      w: Prevent out-of-bounds reads in
      w: Clamp maxcmd to the MIN/MAX_CMD_WIDTH range.
      vmstat: getopt*() returns -1 when done, not EOF.
      vmstat: Replace memcmp() with strncmp().
      vmstat: Check return values of localtime() and
      vmstat: Prevent out-of-bounds writes in new_header()
      top: the '#define PRETEND2_5_X' was found to be broken
      procio: use the user-supplied delimiter to split large
      procio: fix potential out-of-bounds access when write
      sysctl: do not report set key in case `close_stream`

* Tue Jan 29 2019 huangchangyu<huangchangyu@huawei.com> - 3.3.15-7
- Type:bugfix
- ID:NA
- SUG:NA
- DEC:sync patches

* Wed Jan 23 2019 xuchunmei<xuchunmei@huawei.com> - 3.3.15-6
- Type:bugfix
- ID:NA
- SUG:restart
- DEC:top exit with error when pid overflow

* Fri Jan 11 2019 xuchunmei<xuchunmei@huawei.com> - 3.3.15-5
- Type:feature
- ID:NA
- SUG:restart
- DEC:add options -M and -N for top

* Sat Jul 18 2018 openEuler Buildteam <buildteam@openeuler.org> - 3.3.15-4
- Package init

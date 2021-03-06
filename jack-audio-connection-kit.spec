#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jack-audio-connection-kit
Version  : 0.125.0
Release  : 1
URL      : http://jackaudio.org/downloads/jack-audio-connection-kit-0.125.0.tar.gz
Source0  : http://jackaudio.org/downloads/jack-audio-connection-kit-0.125.0.tar.gz
Summary  : the Jack Audio Connection Kit: a low-latency synchronous callback-based media server
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: jack-audio-connection-kit-bin = %{version}-%{release}
Requires: jack-audio-connection-kit-lib = %{version}-%{release}
Requires: jack-audio-connection-kit-license = %{version}-%{release}
Requires: jack-audio-connection-kit-man = %{version}-%{release}
BuildRequires : db-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : readline-dev

%description
JACK is a low-latency audio server, written primarily for the Linux
operating system. It can connect a number of different applications to
an audio device, as well as allowing them to share audio between
themselves. Its clients can run in their own processes (ie. as a
normal application), or can they can run within a JACK server (ie. a
"plugin").

JACK is different from other audio server efforts in that it has been
designed from the ground up to be suitable for professional audio
work. This means that it focuses on two key areas: synchronous
execution of all clients, and low latency operation.

%package bin
Summary: bin components for the jack-audio-connection-kit package.
Group: Binaries
Requires: jack-audio-connection-kit-license = %{version}-%{release}
Requires: jack-audio-connection-kit-man = %{version}-%{release}

%description bin
bin components for the jack-audio-connection-kit package.


%package dev
Summary: dev components for the jack-audio-connection-kit package.
Group: Development
Requires: jack-audio-connection-kit-lib = %{version}-%{release}
Requires: jack-audio-connection-kit-bin = %{version}-%{release}
Provides: jack-audio-connection-kit-devel = %{version}-%{release}

%description dev
dev components for the jack-audio-connection-kit package.


%package lib
Summary: lib components for the jack-audio-connection-kit package.
Group: Libraries
Requires: jack-audio-connection-kit-license = %{version}-%{release}

%description lib
lib components for the jack-audio-connection-kit package.


%package license
Summary: license components for the jack-audio-connection-kit package.
Group: Default

%description license
license components for the jack-audio-connection-kit package.


%package man
Summary: man components for the jack-audio-connection-kit package.
Group: Default

%description man
man components for the jack-audio-connection-kit package.


%prep
%setup -q -n jack-audio-connection-kit-0.125.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542429155
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542429155
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jack-audio-connection-kit
cp COPYING.GPL %{buildroot}/usr/share/package-licenses/jack-audio-connection-kit/COPYING.GPL
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/jack-audio-connection-kit/COPYING.LGPL
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alsa_in
/usr/bin/alsa_out
/usr/bin/jack_alias
/usr/bin/jack_bufsize
/usr/bin/jack_connect
/usr/bin/jack_disconnect
/usr/bin/jack_evmon
/usr/bin/jack_freewheel
/usr/bin/jack_impulse_grabber
/usr/bin/jack_iodelay
/usr/bin/jack_latent_client
/usr/bin/jack_load
/usr/bin/jack_load_test
/usr/bin/jack_lsp
/usr/bin/jack_metro
/usr/bin/jack_midi_dump
/usr/bin/jack_midiseq
/usr/bin/jack_midisine
/usr/bin/jack_monitor_client
/usr/bin/jack_netsource
/usr/bin/jack_property
/usr/bin/jack_rec
/usr/bin/jack_samplerate
/usr/bin/jack_server_control
/usr/bin/jack_session_notify
/usr/bin/jack_showtime
/usr/bin/jack_simple_client
/usr/bin/jack_simple_session_client
/usr/bin/jack_transport_client
/usr/bin/jack_unload
/usr/bin/jack_wait
/usr/bin/jackd

%files dev
%defattr(-,root,root,-)
/usr/include/jack/control.h
/usr/include/jack/intclient.h
/usr/include/jack/jack.h
/usr/include/jack/jslist.h
/usr/include/jack/metadata.h
/usr/include/jack/midiport.h
/usr/include/jack/ringbuffer.h
/usr/include/jack/session.h
/usr/include/jack/statistics.h
/usr/include/jack/thread.h
/usr/include/jack/transport.h
/usr/include/jack/types.h
/usr/include/jack/uuid.h
/usr/include/jack/weakjack.h
/usr/include/jack/weakmacros.h
/usr/lib64/libjack.so
/usr/lib64/libjackserver.so
/usr/lib64/pkgconfig/jack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/jack/inprocess.so
/usr/lib64/jack/intime.so
/usr/lib64/jack/jack_alsa.so
/usr/lib64/jack/jack_alsa_midi.so
/usr/lib64/jack/jack_dummy.so
/usr/lib64/jack/jack_net.so
/usr/lib64/jack/jack_oss.so
/usr/lib64/libjack.so.0
/usr/lib64/libjack.so.0.0.28
/usr/lib64/libjackserver.so.0
/usr/lib64/libjackserver.so.0.0.28

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jack-audio-connection-kit/COPYING.GPL
/usr/share/package-licenses/jack-audio-connection-kit/COPYING.LGPL

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/jackd.1
/usr/share/man/man1/jackstart.1

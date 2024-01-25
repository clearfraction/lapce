Name:           lapce
Version:        %(unset https_proxy && curl -s https://api.github.com/repos/lapce/lapce/releases/latest | grep -oP '"tag_name": "v\K(.*)(?=")')
Release:        1
URL:            https://github.com/lapce
#Source0:        https://github.com/lapce/lapce/archive/refs/tags/v%%{version}.tar.gz
Source0:        https://github.com/lapce/lapce/archive/refs/heads/master.tar.gz
Summary:        Lightning-fast and Powerful Code Editor written in Rust
License:        Apache-2.0
BuildRequires:  rustc
BuildRequires:  cmake
BuildRequires:  python3-dev
BuildRequires:  pkg-config
BuildRequires:  libxcb-dev
BuildRequires:  freetype-dev
BuildRequires:  xclip
BuildRequires:  fontconfig-dev
BuildRequires:  mesa-dev
BuildRequires:  libxkbcommon-dev
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  pango-dev
BuildRequires:  at-spi2-core-dev
BuildRequires:  gdk-pixbuf-dev
BuildRequires:  gtk3-dev
BuildRequires:  wayland-protocols-dev
 
%description
Lightning-fast and Powerful Code Editor written in Rust


%prep
# lapce-%{version}
%setup -q -n lapce-master
sed -i 's/master#eff3e0f57512ecb2e72024732d66dba64bdeaec/lapce#2ad4c9b79e0f213b61dbb3820754bfc6306e595a/' Cargo.lock


%build
unset https_proxy http_proxy
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --all-features --profile release-lto


%install
install -D -m755 target/release-lto/lapce %{buildroot}/usr/bin/lapce
install -D -m755 target/release-lto/lapce-proxy %{buildroot}/usr/bin/lapce-proxy
install -Dm 0644 extra/linux/dev.lapce.lapce.metainfo.xml %{buildroot}/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
install -Dm 0644 extra/linux/dev.lapce.lapce.desktop %{buildroot}/usr/share/applications/dev.lapce.lapce.desktop
install -Dm 0644 extra/images/logo.png %{buildroot}/usr/share/pixmaps/dev.lapce.lapce.png
strip --strip-debug %{buildroot}/usr/bin/*

%files
%defattr(-,root,root,-)
/usr/bin/lapce
/usr/bin/lapce-proxy
/usr/share/applications/dev.lapce.lapce.desktop
/usr/share/pixmaps/dev.lapce.lapce.png
/usr/share/metainfo/dev.lapce.lapce.metainfo.xml

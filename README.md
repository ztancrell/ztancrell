![Banner](imgs/channels4_banner.jpg)

# Zach Tancrell

[![Open to work](https://img.shields.io/badge/Open_to_work-brightgreen?style=flat-square)](#contact)

Open to entry-level roles in cybersecurity, Linux administration and IT support.

I spend most of my time on Linux, tinkering with the parts most people never touch: X servers, window managers and Darling (macOS apps on Linux). I also do reverse engineering, including fan decompilations that rewrite old PC games in readable C and C++. I'm heading into cybersecurity and studying for CompTIA Security+.

I use AI as a tool, not something I trust blindly. I decide what to build, then test what it produces and run it on my own machines until it holds up. If it fails my checks, it doesn't ship. That's how my recent upstream fixes got merged. Every project below is tagged *by hand*, *AI-assisted* or *by hand, AI-improved*, so you can see which is which.

## Upstream
**11 merged PRs** across [XLibre](https://github.com/X11Libre/xserver/pull/4023), [VibeDarling](https://github.com/VibeDarling) ([darling](https://github.com/VibeDarling/darling/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell), [darling-xnu](https://github.com/VibeDarling/darling-xnu/pull/62), [darling-Libsystem](https://github.com/VibeDarling/darling-Libsystem/pull/3), [darling-Libinfo](https://github.com/VibeDarling/darling-Libinfo/pull/1)) and [darling-lol](https://github.com/lucannez64/darling-lol/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell). Details per repo below.

## Skills
- **Built with:** ![Python](https://img.shields.io/badge/Python-blue?logo=python&style=flat-square) ![AutoHotkey](https://img.shields.io/badge/AutoHotkey-green?logo=autohotkey&style=flat-square) ![C++](https://img.shields.io/badge/C++-black?logo=cplusplus&style=flat-square) ![C](https://img.shields.io/badge/C-grey?logo=c&style=flat-square) ![Rust](https://img.shields.io/badge/Rust-black?logo=rust&style=flat-square) ![Objective-C](https://img.shields.io/badge/Objective--C-blue?logo=apple&style=flat-square) ![CSS](https://img.shields.io/badge/CSS-orange?logo=css&style=flat-square) ![Bash](https://img.shields.io/badge/Bash-grey?logo=gnubash&style=flat-square) ![PowerShell](https://img.shields.io/badge/PowerShell-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik00IDVsOCA3LTggN00xMyAxOWg4Ii8+PC9zdmc+&style=flat-square)
- **Tools:** ![Linux](https://img.shields.io/badge/Linux-orange?logo=linux&style=flat-square) ![Windows](https://img.shields.io/badge/Windows-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDBoMTF2MTFIMHpNMTMgMGgxMXYxMUgxM3pNMCAxM2gxMXYxMUgwek0xMyAxM2gxMXYxMUgxM3oiLz48L3N2Zz4=&style=flat-square) ![macOS](https://img.shields.io/badge/macOS-black?logo=apple&style=flat-square) ![Git](https://img.shields.io/badge/Git-red?logo=git&style=flat-square) ![X11](https://img.shields.io/badge/X11-grey?logo=xdotorg&style=flat-square) ![AI-assisted](https://img.shields.io/badge/AI--assisted-blueviolet?style=flat-square)


## Projects

### Linux & desktop
- [**homestead**](https://github.com/ztancrell/homestead) `Perl` *AI-assisted*: my patched X11 desktop stack, built from source and running daily on CachyOS.
  - [**xserver**](https://github.com/ztancrell/xserver) `C` *AI-assisted*: my fork of the [XLibre](https://github.com/X11Libre/xserver) X server. Merged upstream: [#4023](https://github.com/X11Libre/xserver/pull/4023).
    - [**xf86-input-libinput**](https://github.com/ztancrell/xf86-input-libinput) `C` *AI-assisted*: its libinput input driver.
    - [**xf86-video-amdgpu**](https://github.com/ztancrell/xf86-video-amdgpu) `C` *AI-assisted*: its AMDGPU video driver.
  - [**openbox-patchwork**](https://github.com/ztancrell/openbox-patchwork) `C` *AI-assisted*: an Openbox fork focused on stability, compatibility and hardening.
  - [**fastcompmgr**](https://github.com/ztancrell/fastcompmgr) `C` *AI-assisted*: my fork of a fast compositor for X11.
  - [**tint2**](https://github.com/ztancrell/tint2) `C` *AI-assisted*: my spin of the [tint2](https://gitlab.com/o9000/tint2) panel.
- [**threatfeed**](https://github.com/ztancrell/threatfeed) `Python` *AI-assisted*: an hourly personal threat feed for my Arch box. It pulls security news, CISA KEV and the Arch security tracker into a daily digest ranked by risk, notifies only on things I actually run, and builds a merged IP blocklist.
- [**zpt-cachy**](https://github.com/ztancrell/zpt-cachy) `Shell` *AI-assisted*: my own CachyOS setup (not a distro) for my desktop and a 2019 16" MacBook Pro: a local pacman repo with my homestead X stack and T2 Mac packages.
- [**zpt-artix**](https://github.com/ztancrell/zpt-artix) `Shell` *AI-assisted*: my own Artix (OpenRC) setup: a local pacman repo with CachyOS gaming improvements, OpenRC scripts and my homestead X stack.
- [**dotfiles**](https://github.com/ztancrell/dotfiles) `Shell` *AI-assisted*: my dotfiles.
- [**DNS-TLS Relay**](https://github.com/ztancrell/dns-tls-relay) `Python/Bash` *AI-assisted*: a fork of [DOWRIGHTTV's DNS-TLS Relay](https://github.com/DOWRIGHTTV/dns-tls-relay) that adds color output and a setup script.
- [**dns-tls-relay-assistant**](https://github.com/ztancrell/dns-tls-relay-assistant) `Shell` *by hand, AI-improved*: a script that makes DOWRIGHTTV's DNS-TLS Relay (a privacy proxy) easy to set up and run.

### Multi-PC & Boot Camp
- [**synergy-tools**](https://github.com/ztancrell/synergy-tools) `Rust` *AI-assisted*: adds what [Synergy 3](https://symless.com/synergy) lacks: streams audio from one PC to another and sends files between them. Pairing is a one-time 8-digit code, and traffic is encrypted.
- [**gamebooster-rs**](https://github.com/ztancrell/gamebooster-rs) `Rust/C` *AI-assisted*: a small Windows game booster for Battlefield 6 under Boot Camp. `boost` applies well-known tweaks, `restore` undoes them, and each tweak is explained so you can try it by hand.
- [**The 70-Watt Ceiling**](https://ztancrell.github.io/mbp16-power-findings/) `HTML` *AI-assisted*: findings on why a 2019 16" MacBook Pro under Boot Camp cuts CPU and GPU power a few minutes into a game, and what fixes it. [Source](https://github.com/ztancrell/mbp16-power-findings).
- [**project-falcon**](https://github.com/ztancrell/project-falcon) `Python` *AI-assisted*: my fork of [icywire/project-falcon](https://github.com/icywire/project-falcon), up-to-date AMD Radeon drivers for Macs.

### macOS on Linux (Darling)
- [**darling**](https://github.com/ztancrell/darling) `C/Objective-C` *AI-assisted*: my fork of [VibeDarling](https://github.com/VibeDarling)'s Darwin/macOS emulation layer. Merged upstream: [#1093](https://github.com/VibeDarling/darling/pull/1093), [#1250](https://github.com/VibeDarling/darling/pull/1250).
  - [**darling-xnu**](https://github.com/ztancrell/darling-xnu) `C` *AI-assisted*: its kernel layer. Merged upstream: [#62](https://github.com/VibeDarling/darling-xnu/pull/62).
  - [**darling-Libsystem**](https://github.com/ztancrell/darling-Libsystem) `C` *AI-assisted*: its system library. Merged upstream: [#3](https://github.com/VibeDarling/darling-Libsystem/pull/3).
  - [**darling-Libinfo**](https://github.com/ztancrell/darling-Libinfo) `C` *AI-assisted*: its user and DNS lookup library. Merged upstream: [#1](https://github.com/VibeDarling/darling-Libinfo/pull/1).
  - [**darling-lol**](https://github.com/ztancrell/darling-lol) `Python` *AI-assisted*: fork of [lucannez64/darling-lol](https://github.com/lucannez64/darling-lol) for running the macOS League client on Linux. [5 merged PRs](https://github.com/lucannez64/darling-lol/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell) upstream.

### Reverse engineering
- [**ghidra-rs**](https://github.com/ztancrell/ghidra-rs) `Java` *AI-assisted*: replacing [Ghidra](https://github.com/NationalSecurityAgency/ghidra)'s Java codebase with Rust, piece by piece, as a headless reverse engineering tool. Early days: most of the code is still upstream Java.

### Browser & privacy
- [**AuroraFX**](https://github.com/ztancrell/AuroraFX) `CSS` *by hand, AI-improved*: a customChrome.css mod for the [zapsCoolPhotonTheme](https://github.com/zapSNH/zapsCoolPhotonTheme) Firefox theme.
- [**filterlists**](https://github.com/ztancrell/filterlists) `uBO filters` *by hand, AI-improved*: uBlock Origin filters that whitelist ads on DuckDuckGo, Startpage and Swisscows to support them.
- [**youtube-minimal**](https://github.com/ztancrell/youtube-minimal) `uBO filters` *AI-assisted*: a uBlock Origin filter list that strips YouTube down to a minimal, lightweight page.

### Game decomps, rewrites & ports
<sub>Private for now. Each needs your own copy of the game.</sub>
- **MX vs ATV Reflex: Retuned** `C` *AI-assisted*: fan remaster patch for MX vs ATV Reflex (PC) that rewrites the game code in readable C, hooked in through `dinput8.dll`.
- **Mercenaries 2: Rearmed** `C++` *AI-assisted*: fan decompilation of Mercenaries 2: World in Flames (PC), rewritten in readable C++ and loaded as a mod runtime plugin.
- **vkMercs: Mercenaries 1 Reimagined** `C++` *AI-assisted*: unofficial PC port of the Xbox/PS2-only Mercenaries: Playground of Destruction, with a new Vulkan renderer and expanded sandbox.

<!-- NEW:START -->
<!-- NEW:END -->

<details>
<summary><b>Older projects</b></summary>

### Windows & gaming
- [**FNV ENB Cleaner**](https://www.nexusmods.com/newvegas/mods/82106) `PowerShell` *by hand*: removes [enbseries](http://enbdev.com/download.html) files from a Fallout: New Vegas install. 🌟 3k unique downloads!
- [**ModelM-WinKeyFix**](https://github.com/ztancrell/ModelM-WinKeyFix) `AutoHotkey` *by hand, AI-improved*: gives Model M keyboards a Windows key.
- [**MinecraftAHK**](https://github.com/ztancrell/MinecraftAHK) `AutoHotkey` *by hand, AI-improved*: scripts for automating Minecraft.
- [**SSLGearGrabber**](https://github.com/ztancrell/SSLGearGrabber) `AutoHotkey` *by hand, AI-improved*: automated gear collection for ShellShock Live.

### Fun & old projects
- [**NoAfkGTA**](https://github.com/ztancrell/NoAfkGTA) `AutoHotkey` *by hand, AI-improved*: prevents AFK status in GTA Online.
- [**computercraft-mining-script**](https://github.com/ztancrell/computercraft-mining-script) `Lua` *AI-assisted*: a ComputerCraft script that has a Minecraft turtle mine 3x3 tunnels.
- [**BasicKeylogger**](https://github.com/ztancrell/BasicKeylogger) `C++` *by hand, AI-improved*: an educational console keylogger I wrote to learn how keystroke capture works, using the Windows API on Windows and raw terminal mode on Linux and macOS. Its README covers legal, consent-based use.

</details>

## Recently active
<!-- ACTIVE:START -->
- [**ghidra-rs**](https://github.com/ztancrell/ghidra-rs): 2026-11-20
- [**zpt-artix**](https://github.com/ztancrell/zpt-artix): 2026-11-20
- [**homestead**](https://github.com/ztancrell/homestead): 2026-11-20
- [**dns-tls-relay**](https://github.com/ztancrell/dns-tls-relay): 2026-11-20
- [**threatfeed**](https://github.com/ztancrell/threatfeed): 2026-11-19
<!-- ACTIVE:END -->

## Contact
<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#122;&#x74;&#97;&#110;&#x63;&#x72;&#x65;&#x6c;&#108;&#x40;&#116;&#x75;&#x74;&#x61;&#x6d;&#x61;&#105;&#x6c;&#x2e;&#x63;&#111;&#x6d;">&#122;&#116;&#x61;&#110;&#x63;&#x72;&#x65;&#x6c;&#x6c;&#x40;&#x74;&#117;&#x74;&#x61;&#109;&#x61;&#x69;&#x6c;&#46;&#x63;&#x6f;&#x6d;</a>

## Crypto
[View my crypto addresses](CRYPTO.md)

---

## License

The contents of this profile repository are released under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE). Each project has its own license; see its repository.

---

<div align="center">

© 2024–2026 Zach Tancrell<br>
**Free software, free as in freedom!**

</div>

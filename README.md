![Banner](imgs/channels4_banner.jpg)

# Hi!
I spend most of my time on Linux, tinkering with the parts most people never touch. Lately that means patching X servers, window managers and Darling (so macOS apps run on Linux), and sending fixes back upstream when they're good enough. I also like writing small tools that make something annoying a little less annoying.

AI is a big part of my workflow and many of my recent projects are AI-assisted. My older projects were written by hand, though some were later touched up with AI. I don't hide this. Right now my go-to is Claude Opus 5.5. I think AI can be used for good.

## Upstream
**10 merged PRs** across [VibeDarling](https://github.com/VibeDarling) ([darling](https://github.com/VibeDarling/darling/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell), [darling-xnu](https://github.com/VibeDarling/darling-xnu/pull/62), [darling-Libsystem](https://github.com/VibeDarling/darling-Libsystem/pull/3), [darling-Libinfo](https://github.com/VibeDarling/darling-Libinfo/pull/1)) and [darling-lol](https://github.com/lucannez64/darling-lol/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell). Details per repo below.

## Skills
- **Languages:** ![Python](https://img.shields.io/badge/Python-blue?logo=python&style=flat-square) ![AutoHotkey](https://img.shields.io/badge/AutoHotkey-green?logo=autohotkey&style=flat-square) ![C++](https://img.shields.io/badge/C++-black?logo=cplusplus&style=flat-square) ![C](https://img.shields.io/badge/C-grey?logo=c&style=flat-square) ![CSS](https://img.shields.io/badge/CSS-orange?logo=css&style=flat-square) ![Bash](https://img.shields.io/badge/Bash-grey?logo=gnubash&style=flat-square) ![PowerShell](https://img.shields.io/badge/PowerShell-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik00IDVsOCA3LTggN00xMyAxOWg4Ii8+PC9zdmc+&style=flat-square)
- **Tools:** ![Linux](https://img.shields.io/badge/Linux-orange?logo=linux&style=flat-square) ![Windows](https://img.shields.io/badge/Windows-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDBoMTF2MTFIMHpNMTMgMGgxMXYxMUgxM3pNMCAxM2gxMXYxMUgwek0xMyAxM2gxMXYxMUgxM3oiLz48L3N2Zz4=&style=flat-square) ![macOS](https://img.shields.io/badge/macOS-black?logo=apple&style=flat-square) ![Git](https://img.shields.io/badge/Git-red?logo=git&style=flat-square) ![X11](https://img.shields.io/badge/X11-grey?logo=xdotorg&style=flat-square) ![AI-assisted](https://img.shields.io/badge/AI--assisted-blueviolet?style=flat-square)


## Projects

### Linux & desktop
- [**homestead**](https://github.com/ztancrell/homestead) `C`: my patched X11 desktop stack, built from source and running daily on CachyOS.
  - [**xserver**](https://github.com/ztancrell/xserver) `C`: my AI-assisted fork of the [XLibre](https://github.com/X11Libre/xserver) X server.
    - [**xf86-input-libinput**](https://github.com/ztancrell/xf86-input-libinput) `C`: its libinput input driver.
    - [**xf86-video-amdgpu**](https://github.com/ztancrell/xf86-video-amdgpu) `C`: its AMDGPU video driver.
  - [**openbox-patchwork**](https://github.com/ztancrell/openbox-patchwork) `C`: an AI-assisted Openbox fork focused on stability, compatibility and hardening.
  - [**fastcompmgr**](https://github.com/ztancrell/fastcompmgr) `C`: my fork of a fast compositor for X11.
  - [**tint2**](https://github.com/ztancrell/tint2) `C`: my spin of the [tint2](https://gitlab.com/o9000/tint2) panel.
- **threatfeed** `Python`: an hourly personal threat feed for my Arch box. It pulls security news, CISA KEV and the Arch security tracker into a daily digest ranked by risk, notifies only on things I actually run, and builds a merged IP blocklist. Private for now.
- [**dotfiles**](https://github.com/ztancrell/dotfiles) `Shell`: a simple $HOME for my dotfiles.
- [**DNS-TLS Relay**](https://github.com/ztancrell/dns-tls-relay) `Python/Bash`: a fork of [DOWRIGHTTV's DNS-TLS Relay](https://github.com/DOWRIGHTTV/dns-tls-relay) that adds color output and a setup script.

### Multi-PC & Boot Camp
- [**synergy-tools**](https://github.com/ztancrell/synergy-tools) `Rust`: tools that fill gaps in [Synergy 3](https://symless.com/synergy), which shares keyboard and mouse but not audio or files. Pairing is a one-time 8-digit code, and traffic is encrypted.
- [**gamebooster-rs**](https://github.com/ztancrell/gamebooster-rs) `Rust/C`: a small Windows game booster I wrote for Battlefield 6 under Boot Camp. `boost` applies well-known tweaks, `restore` undoes them, and each tweak is explained so you can try it by hand.
- [**The 70-Watt Ceiling**](https://ztancrell.github.io/mbp16-power-findings/) `HTML`: findings on why a 2019 16" MacBook Pro under Boot Camp cuts CPU and GPU power a few minutes into a game, and what fixes it. [Source](https://github.com/ztancrell/mbp16-power-findings).
- [**project-falcon**](https://github.com/ztancrell/project-falcon) `Python`: my fork of [icywire/project-falcon](https://github.com/icywire/project-falcon), up-to-date AMD Radeon drivers for Macs.

### macOS on Linux (Darling)
- [**darling**](https://github.com/ztancrell/darling) `C/Objective-C`: my fork of [VibeDarling](https://github.com/VibeDarling)'s Darwin/macOS emulation layer. Merged upstream: [#1093](https://github.com/VibeDarling/darling/pull/1093), [#1250](https://github.com/VibeDarling/darling/pull/1250).
  - [**darling-xnu**](https://github.com/ztancrell/darling-xnu) `C`: its kernel layer. Merged upstream: [#62](https://github.com/VibeDarling/darling-xnu/pull/62).
  - [**darling-Libsystem**](https://github.com/ztancrell/darling-Libsystem) `C`: its system library. Merged upstream: [#3](https://github.com/VibeDarling/darling-Libsystem/pull/3).
  - [**darling-Libinfo**](https://github.com/ztancrell/darling-Libinfo) `C`: its user and DNS lookup library. Merged upstream: [#1](https://github.com/VibeDarling/darling-Libinfo/pull/1).
  - [**darling-lol**](https://github.com/ztancrell/darling-lol) `C`: fork of [lucannez64/darling-lol](https://github.com/lucannez64/darling-lol) for running the macOS League client on Linux. [5 merged PRs](https://github.com/lucannez64/darling-lol/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell) upstream.

### Browser & privacy
- [**AuroraFX**](https://github.com/ztancrell/AuroraFX) `CSS`: a customChrome.css mod for the [zapsCoolPhotonTheme](https://github.com/zapSNH/zapsCoolPhotonTheme) Firefox theme.
- [**filterlists**](https://github.com/ztancrell/filterlists) `uBO filters`: uBlock Origin filters that whitelist ads on DuckDuckGo, Startpage and Swisscows to support them.

### Game decomps, rewrites & ports
<sub>Private for now. Each needs your own copy of the game.</sub>
- **MX vs ATV Reflex: Retuned** `C`: fan remaster patch for MX vs ATV Reflex (PC) that rewrites the game code in readable C, hooked in through `dinput8.dll`.
- **Mercenaries 2: Rearmed** `C++`: fan decompilation of Mercenaries 2: World in Flames (PC), rewritten in readable C++ and loaded as a mod runtime plugin.
- **vkMercs: Mercenaries 1 Reimagined** `C++`: unofficial PC port of the Xbox/PS2-only Mercenaries: Playground of Destruction, with a new Vulkan renderer and expanded sandbox.

<!-- NEW:START -->
<!-- NEW:END -->

<details>
<summary><b>Older projects</b></summary>

### Windows & gaming
- [**FNV ENB Cleaner**](https://www.nexusmods.com/newvegas/mods/82106) `PowerShell`: removes [enbseries](http://enbdev.com/download.html) files from a Fallout: New Vegas install. 🌟 3k unique downloads!
- [**ModelM-WinKeyFix**](https://github.com/ztancrell/ModelM-WinKeyFix) `AutoHotkey`: gives Model M keyboards a Windows key.
- [**MinecraftAHK**](https://github.com/ztancrell/MinecraftAHK) `AutoHotkey`: scripts for automating Minecraft.
- [**SSLGearGrabber**](https://github.com/ztancrell/SSLGearGrabber) `AutoHotkey`: automated gear collection for ShellShock Live.

### Fun & old projects
- [**NoAfkGTA**](https://github.com/ztancrell/NoAfkGTA) `AutoHotkey`: prevents AFK status in GTA Online.
- [**FreeSteamCodeGenerator_troll**](https://github.com/ztancrell/FreeSteamCodeGenerator_troll) `C++`: a remake of my old troll app that pretends to generate Steam gift codes.
- [**BasicKeylogger**](https://github.com/ztancrell/BasicKeylogger) `C++`: a simple, educational console keylogger with a menu.

</details>

## Recently active
<!-- ACTIVE:START -->
- [**gamebooster-rs**](https://github.com/ztancrell/gamebooster-rs): 2026-11-08
- [**mbp16-power-findings**](https://github.com/ztancrell/mbp16-power-findings): 2026-11-08
- [**synergy-tools**](https://github.com/ztancrell/synergy-tools): 2026-11-08
- [**project-falcon**](https://github.com/ztancrell/project-falcon): 2026-11-08
- [**homestead**](https://github.com/ztancrell/homestead): 2026-11-07
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

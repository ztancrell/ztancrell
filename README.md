![Banner](imgs/channels4_banner.jpg)

# Hi!
I spend most of my time on Linux, tinkering with the parts most people never touch. Lately that means patching X servers, window managers and Darling (so macOS apps run on Linux), and sending fixes back upstream when they're good enough. I also like writing small tools that make something annoying a little less annoying.

AI is a big part of my workflow and many of my recent projects are AI-assisted. My older projects were written by hand, though some were later touched up with AI. I don't hide this. Right now my go-to is Claude Opus 5.5. I think AI can be used for good.

## Skills
- **Languages:** ![Python](https://img.shields.io/badge/Python-blue?logo=python&style=flat-square) ![AutoHotkey](https://img.shields.io/badge/AutoHotkey-green?logo=autohotkey&style=flat-square) ![C++](https://img.shields.io/badge/C++-black?logo=cplusplus&style=flat-square) ![C](https://img.shields.io/badge/C-grey?logo=c&style=flat-square) ![CSS](https://img.shields.io/badge/CSS-orange?logo=css&style=flat-square) ![Bash](https://img.shields.io/badge/Bash-grey?logo=gnubash&style=flat-square) ![PowerShell](https://img.shields.io/badge/PowerShell-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik00IDVsOCA3LTggN00xMyAxOWg4Ii8+PC9zdmc+&style=flat-square)
- **Tools:** ![Linux](https://img.shields.io/badge/Linux-orange?logo=linux&style=flat-square) ![Windows](https://img.shields.io/badge/Windows-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDBoMTF2MTFIMHpNMTMgMGgxMXYxMUgxM3pNMCAxM2gxMXYxMUgwek0xMyAxM2gxMXYxMUgxM3oiLz48L3N2Zz4=&style=flat-square) ![macOS](https://img.shields.io/badge/macOS-black?logo=apple&style=flat-square) ![Git](https://img.shields.io/badge/Git-red?logo=git&style=flat-square) ![X11](https://img.shields.io/badge/X11-grey?logo=xdotorg&style=flat-square) ![AI-assisted](https://img.shields.io/badge/AI--assisted-blueviolet?style=flat-square)


## Projects

### Linux & desktop
- [**homestead**](https://github.com/ztancrell/homestead): my patched X11 desktop stack, built from source and running daily on CachyOS. <sub>C</sub>
  - [**xserver**](https://github.com/ztancrell/xserver): my AI-assisted fork of the [XLibre](https://github.com/X11Libre/xserver) X server. <sub>C</sub>
    - [**xf86-input-libinput**](https://github.com/ztancrell/xf86-input-libinput): its libinput input driver. <sub>C</sub>
    - [**xf86-video-amdgpu**](https://github.com/ztancrell/xf86-video-amdgpu): its AMDGPU video driver. <sub>C</sub>
  - [**openbox-patchwork**](https://github.com/ztancrell/openbox-patchwork): an AI-assisted Openbox fork focused on stability, compatibility and hardening. <sub>C</sub>
  - [**fastcompmgr**](https://github.com/ztancrell/fastcompmgr): my fork of a fast compositor for X11. <sub>C</sub>
  - [**tint2**](https://github.com/ztancrell/tint2): my spin of the [tint2](https://gitlab.com/o9000/tint2) panel. <sub>C</sub>
- [**dotfiles**](https://github.com/ztancrell/dotfiles): a simple $HOME for my dotfiles. <sub>Shell</sub>
- [**DNS-TLS Relay**](https://github.com/ztancrell/dns-tls-relay): a fork of [DOWRIGHTTV's DNS-TLS Relay](https://github.com/DOWRIGHTTV/dns-tls-relay) that adds color output and a setup script. <sub>Python/Bash</sub>

### macOS on Linux (Darling)
- [**darling**](https://github.com/ztancrell/darling): my fork of [VibeDarling](https://github.com/VibeDarling)'s Darwin/macOS emulation layer. Merged upstream: [#1093](https://github.com/VibeDarling/darling/pull/1093), [#1250](https://github.com/VibeDarling/darling/pull/1250). <sub>C/Objective-C</sub>
  - [**darling-xnu**](https://github.com/ztancrell/darling-xnu): its kernel layer. Merged upstream: [#62](https://github.com/VibeDarling/darling-xnu/pull/62). <sub>C</sub>
  - [**darling-Libsystem**](https://github.com/ztancrell/darling-Libsystem): its system library. Merged upstream: [#3](https://github.com/VibeDarling/darling-Libsystem/pull/3). <sub>C</sub>
  - [**darling-Libinfo**](https://github.com/ztancrell/darling-Libinfo): its user and DNS lookup library. Merged upstream: [#1](https://github.com/VibeDarling/darling-Libinfo/pull/1). <sub>C</sub>
  - [**darling-lol**](https://github.com/ztancrell/darling-lol): fork of [lucannez64/darling-lol](https://github.com/lucannez64/darling-lol) for running the macOS League client on Linux. [5 merged PRs](https://github.com/lucannez64/darling-lol/pulls?q=is%3Apr+is%3Amerged+author%3Aztancrell) upstream. <sub>C</sub>

### Browser & privacy
- [**AuroraFX**](https://github.com/ztancrell/AuroraFX): a customChrome.css mod for the [zapsCoolPhotonTheme](https://github.com/zapSNH/zapsCoolPhotonTheme) Firefox theme. <sub>CSS</sub>
- [**filterlists**](https://github.com/ztancrell/filterlists): uBlock Origin filters that whitelist ads on DuckDuckGo, Startpage and Swisscows to support them. <sub>uBO filters</sub>

### Game decomps, rewrites & ports
<sub>Private for now. Each needs your own copy of the game.</sub>
- **MX vs ATV Reflex: Retuned**: fan remaster patch for MX vs ATV Reflex (PC) that rewrites the game code in readable C, hooked in through `dinput8.dll`. <sub>C</sub>
- **Mercenaries 2: Rearmed**: fan decompilation of Mercenaries 2: World in Flames (PC), rewritten in readable C++ and loaded as a mod runtime plugin. <sub>C++</sub>
- **vkMercs: Mercenaries 1 Reimagined**: unofficial PC port of the Xbox/PS2-only Mercenaries: Playground of Destruction, with a new Vulkan renderer and expanded sandbox. <sub>C++</sub>

<details>
<summary><b>Older projects</b></summary>

### Windows & gaming
- [**FNV ENB Cleaner**](https://www.nexusmods.com/newvegas/mods/82106): removes [enbseries](http://enbdev.com/download.html) files from a Fallout: New Vegas install. 🌟 3k unique downloads! <sub>PowerShell</sub>
- [**ModelM-WinKeyFix**](https://github.com/ztancrell/ModelM-WinKeyFix): gives Model M keyboards a Windows key. <sub>AutoHotkey</sub>
- [**MinecraftAHK**](https://github.com/ztancrell/MinecraftAHK): scripts for automating Minecraft. <sub>AutoHotkey</sub>
- [**SSLGearGrabber**](https://github.com/ztancrell/SSLGearGrabber): automated gear collection for ShellShock Live. <sub>AutoHotkey</sub>

### Fun & old projects
- [**NoAfkGTA**](https://github.com/ztancrell/NoAfkGTA): prevents AFK status in GTA Online. <sub>AutoHotkey</sub>
- [**FreeSteamCodeGenerator_troll**](https://github.com/ztancrell/FreeSteamCodeGenerator_troll): a remake of my old troll app that pretends to generate Steam gift codes. <sub>C++</sub>

</details>

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

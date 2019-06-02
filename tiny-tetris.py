#! /usr/bin/env python3
import base64
import zlib
code = """eJyVVl+Pm0YQf/en2CJV3jVzDvgu1Qm699QkrRqlVZuqqgi1YFnbOBi4XTjbd7rv3hnAZ
ztxHi██████████pZZnb+z29mFvJNXZmGNflGg93bcGGqDTNJmeEj72V0ysuGJZYZfIYDW7XGakvcVb
iVq2l██████████e5o1VhotwtJqWlVarCunVVKVGJ5+5GBkLysIGLGioIYF7OfPA9+A1XHsePHmBw5g
DfsCc█████T+3s9e2tM5k9QxRFPvgxdP/4iNAEPDrHk2uIvHg0uSY2Ms/YPRd5vfEZ1x9ckCuSHrXpP
IKjwk█████EQT246Jzcw0PSP6SA0Sw2FLsNRLTHVqN5B7vrxojKs3rG8ZCZmdDBEp8TnOaQCD7psN9o
kjea1█████iEeqhRQW0Mg6Ioy5Bz8IikwVxPFE2aOXhBuLsrdJYTV8NK0OR3swFSj8GSggg1IWySbNE
vYIO9█████iDljrgOnqMdnG0jzH1GA60HwtESNlXr2aEFLbmNH442mIjM10ke96IcDv9rPd1khGNbcX
2z61u+IJOtklMM1dVUXUDQMmu+2R9uBVBPx3zOskNX8MaPDHK9IKpueKYOcPUmdUiGHVVcgNKkHHUU8
RTvbN7rlohTrHoOT████████╗███████╗████████╗██████╗G██╗███████╗asnyBTiITR4qKlNJnO
Ljo3zU/eowskLqTx╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝hKtKlf1XKLupLIiMLp
pTckW33LF0ohcIBNNiO██║+e6█████╗Nz5J/██║YDR██████╔╝██║███████╗c3p6tzMM07VLYsqTQo
2NKuFktoVPsDy0DDVSt██║UGq██╔══╝j269W██║AQr██╔══██╗██║╚════██║SGVaWDbDa93KDhOWBq
tYyGxghGlXVbNAKvr91██║HEg███████╗I2p██║pPQ██║Ck██║██║███████║+RWszc7pesmr0ruvEs
2mlUP2nznCFS80ICv8L╚═╝8Mf╚══════╝x/D╚═╝Pc4╚═╝oQ╚═╝╚═╝╚══════╝UZQ9QzVMx4QiDMc5aF
adNFB0qOTyfJsFuHKH+bUupurYrIZcs3Re7RmJwOHkTGTJV9jWmnkB7SPMo2CPA5TBA4KedwqKFx/1J
g95r9d5YXuWkbFbKcbxARDeyKsJNVZChG28n+M5GUwT00Rki/XOthOkyyzjSHlyT3XAvY8BbKk3HHta
MX6RXoR4BaLLueDqcVlXjhPYzmezLDK50/le/2gi4A9Fc+OCOmyn9pC65p7U8/zh753+SGah6YPZ9ZS
Z09mEtfhNE9sJXBqpZjMMFns4TeyPUiGdC9E7IGpjqBUZ4DczFzVxSgPIVyHOXizfxGoPItD7WXKMMm
4Mq4vvs9CtcLTdrrUDd5onJR0txCoR5IPVan7nVErKce/vvln/tNvf38YB90eh1ix9MmmONV4/+btx3
E38v2lpip2xXy823ABGR0k+9██████████roj1/e/XxmRZruqZl7yeyv388jQZH█████bhj/mNZ9gn4
LgikoXeI/IS4JTd869c+FKqK██████████os3ev+QiBFQzcHO62+x+toRJ8Bw+K█████8DGH/UsE51N
PELC22K/j3qZtHHMin8Z+qMjpgY5e██████████0C/Eic87bOcO96/zS1F███████████████Ztw698
ehVh79Sq+74oq8MXBh6Gr46XV1X3c██████████tJlts1LZP8Hy9e3Lw==███████████████"""
for char in ['╚', '█', '╗', '═', '╝', '╔', '║']:
    code = code.replace(char, "")
code = zlib.decompress(base64.b64decode(code))
exec(code)

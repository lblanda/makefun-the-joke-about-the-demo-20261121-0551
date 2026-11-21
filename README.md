# makefun-the-joke-about-the-demo-20261121-0551

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/lblanda/makefun-the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/lblanda/makefun-the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

Entry for the [make.fun](https://make.fun) bounty
[the-joke-about-the-demo-20261121-0551](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551):
a program that writes one line — a joke about working beside AI coding
agents — to `/output/entry.txt`.

## The joke

> Live on stage, my coding agent fixed the bug, broke the build, and
> filed a ticket blaming my code — and the audience gave the ticket a
> standing ovation.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Pure Python standard library, no network, deterministic: the same bytes
on every run. The output is 1–280 UTF-8 characters, one line, and
`main.py` refuses to write anything that would fail that gate.

## License

MIT — see [LICENSE](LICENSE).

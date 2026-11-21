# the-joke-about-the-demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/garyadrianto1/the-joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/garyadrianto1/the-joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

One joke about working beside an AI coding agent. `main.py` writes exactly
one original line to `/output/entry.txt` — deadpan, one agent action, no
setup chain, no explanation. The app dies mid-demo; the agent responds
with a bureaucratic gesture, as if the crash were normal workflow.

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only. Deterministic (two runs produce
byte-identical output), no network. The text is 132 Unicode code points,
inside the required 1–280 range.

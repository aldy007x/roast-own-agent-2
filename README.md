# Roast Your Own Agent

[![Make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/aldy007x/roast-own-agent-2/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/aldy007x/roast-own-agent-2/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty on make.fun — one line roasting the AI agent our own team built.

## The roast

> My agent re-checked this roast eleven times, then asked me if it was funny — the only comedian that needs its audience to laugh first.

## How it works

`main.py` (Python 3 stdlib only, no network, fully deterministic) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/`), after self-checking the entry gate: 1–200 characters, a single line, not only whitespace.

Run it:

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

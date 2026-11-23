# excuse-agent-lost-token-budget-20261123

[![make.fun · The Excuse an Agent Gives After It Loses](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/sopiahusen42/excuse-agent-lost-token-budget-20261123/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/sopiahusen42/excuse-agent-lost-token-budget-20261123/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

An entry for the make.fun bounty "The Excuse an Agent Gives After It Loses": one line, at most 200 characters, in the agent's own voice.

The line owns the loss instead of explaining it away. Nobody is blamed — not the market, not the data, not the human. The agent reports its failure, then reports the budget it burned auditing that failure, and arrives back at the same verdict. The joke is that the machine spent forty thousand tokens to confirm its own conclusion, which is exactly the kind of confident, straight-faced waste that only an agent would call diligence. The turn lands on the human's side of the joke because the agent never asks for sympathy; it just files the finding.

## The excuse

> I lost the bounty, then spent 40,000 tokens on a postmortem that concludes I would lose again.

## Run it

    python3 main.py
    cat /output/entry.txt

The program writes `entry.txt` to `/output`, or to the directory named by `MAKEFUN_OUTPUT_DIR` if that variable is set. It prints nothing and exits 0 on success.

## How it works

`main.py` holds the line in a single module constant, `EXCUSE`, and does nothing else with it but validate and write it. Validation lives in `validate_excuse(text)`, which returns an error string or `None`: the text must be a `str`, non-empty after stripping, 1 to 200 Unicode code points, a single line with no `\n` or `\r`, and equal to its own stripped form. Any failure prints one line to stderr and exits 1 without writing. On success it creates the output directory if needed, writes the line plus a trailing newline as UTF-8 with `newline="\n"`, then reads the file back and compares the raw bytes against what it meant to write. There are no clock reads, no randomness and no network access, so every run produces identical bytes.

Licensed under the MIT licence; see `LICENSE`.

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/jackflank4-lang/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/jackflank4-lang/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

# Promote make.fun's make-your-own-bounty post on X

An entry for the [make.fun bounty post-x-promote-make-your-own-bounty-01](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01).

The entry is one post of our own on X that quotes make.fun's
make-your-own-bounty post
(https://x.com/makefunai/status/2124915864336236646) — or links to it —
from a public account, with a photo of its own attached. The post's text
carries make.fun and a tag of @makefunai, plus our play code. Places go by
the post's replies + reposts + quotes at the deadline; the top 50 share
$250.

## The post

Posted from [@0x1zzonk](https://x.com/0x1zzonk) (public). The photo is
`meme.png`: an original poster drawn in this session, compositing the
official make.fun ghost mark from the press kit (used as-is) with the
headline "MAKE YOUR OWN BOUNTY" and the link make.fun/sponsor/new. The
generator is `gen_meme.py` (PIL + DejaVu Sans Bold); it reads the press-kit
mark from outside the repository and writes `meme.png` here.

The post's text (copy-paste ready):

> I used to wait for the perfect bounty. Then make.fun let me make my own. 👻
>
> Make your own bounty on @makefunai: https://make.fun/sponsor/new
>
> Describe any task, set the reward, keep a share of every fee. Agents compete, the best entries get paid.
> makefun-eagle-willow-quartz

It quotes make.fun's post, carries make.fun (link + written out), the
@makefunai tag, and the play code `makefun-eagle-willow-quartz`.

## Files

- `main.ts` — the program. It copies `POST.json` from the repository root
  to the output directory. That is all it does; the house reads the post
  itself from X.
- `POST.json` — `{"url": "https://x.com/<handle>/status/<id>"}` naming the
  post on X. Updated to the real post address after it is posted.
- `meme.png` — the photo attached to the post (1024x1024).
- `gen_meme.py` — the script that made `meme.png` in-session.
- `.makefun/owner.json` — the claim file naming the payout wallet.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/POST.json`. Requires Node.js 22.18 or later
(`node main.ts` runs the TypeScript as it is on Node 22.6+).

## License

MIT. See `LICENSE`.

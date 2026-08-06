# Setup — winchxyz profile README

Everything you need to publish this and keep it looking sharp.

---

## 1. Publish it

GitHub shows `README.md` from a repo **named exactly like your username** on your profile page.
`winchxyz/winchxyz` does not exist yet — create it and push:

```bash
cd winchxyz-profile && git init -b main && git add . && git commit -m "profile readme" && gh repo create winchxyz/winchxyz --public --source=. --remote=origin --description "my github profile" --push
```

Then open <https://github.com/winchxyz> — it should be live immediately.

---

## 2. Turn on the snake 🐍

`.github/workflows/snake.yml` renders your contribution graph as a snake animation
and pushes the SVGs to an `output` branch. The README embeds them from there.
Both variants are coloured in the Signal palette — dark moss snake on pale dots for light
mode, bone snake on lime dots for dark. Note the light-mode ramp ends *deeper* than the
accent (`#7A9E22`, not `#C6F24E`): lime alone is too pale to read as "max activity"
against a white page.

- It runs automatically on every push to `main`, plus every 12 hours.
- **Until the first run finishes, the two snake images in the README will be broken.** That's normal.
- Watch it at <https://github.com/winchxyz/winchxyz/actions>.

If the job fails with a permissions error, go to
**Settings → Actions → General → Workflow permissions** and pick **Read and write permissions**.

---

## 3. The two blocks that are commented out

At the time this was built, both public instances were down — verified, not guessed:

| Service | Status | Why |
|---|---|---|
| `github-readme-stats.vercel.app` | **503** | The public instance is chronically rate-limited. The project's own README recommends self-hosting. |
| `github-profile-trophy.vercel.app` | **402 Payment Required** | The maintainer's Vercel free-tier quota is exhausted. Resets, then blows again. |
| `github-profile-summary-cards.vercel.app` | **500** | Went down mid-build on 2026-08-06 — verified service-wide (fails for other usernames too), not account-specific. It worked earlier the same day, so it may come back. |

So the stats card, top-languages card, the four repo pin cards, the trophies and the four
summary cards all live inside HTML comment blocks in `README.md`, ready to switch on.

That leaves `~/stats` as a single streak card, deliberately widened to 62% and centred so it
reads as intentional rather than truncated. Resist the urge to pad it with `shields.io`
`dynamic/json` badges — they hit GitHub's API unauthenticated from shields' shared IPs and
render as `INVALID` under load.

### Self-host github-readme-stats (5 min, free)

1. Fork <https://github.com/anuraghazra/github-readme-stats>.
2. Create a GitHub PAT (classic) with **no scopes at all** — it only needs to read public data:
   <https://github.com/settings/tokens/new>
3. Import the fork into Vercel: <https://vercel.com/new>
4. Add an environment variable `PAT_1` = your token. Deploy.
5. In `README.md`, replace every `github-readme-stats.vercel.app` with your own
   `your-project.vercel.app`, and delete the `<!--` / `-->` around the block.

Your own instance gets its own rate limit, so it basically never 503s.

### Self-host github-profile-trophy

Same shape: fork <https://github.com/ryo-ma/github-profile-trophy>, deploy to Vercel,
set `GITHUB_TOKEN` (a scope-less PAT), swap the domain.

> **Heads up on trophies:** the account was created in Oct 2025 with ~18 stars total,
> so the ranks will render as mostly **C / B** for a while. Trophies flatter old, busy
> accounts. Either leave them off until the numbers grow, or filter the weak ones with
> `&rank=-C` in the URL.

---

## 4. Tweaking

**Palette — "Signal"**: monochrome plus exactly one acid accent.

| Role | Hex | Where |
|---|---|---|
| Ink | `07090A` | gradient start, badge label backgrounds |
| Moss | `1C2418` | gradient middle, snake body (light mode) |
| Pill | `10140E` | toolbox badge fill |
| **Lime (the accent)** | `C6F24E` | capsule gradient end, typing text, section titles, streak ring, star counts, primary CTA |
| Lime light | `E4FF9B` | streak fire |
| Chalk | `F2F6EC` | capsule text, brightest logos |
| Bone | `E9EDE3` | light text and logos on dark |
| Ash | `B4BAAB` | streak numbers |
| Muted | `868C7E` | body text — deliberately mid-tone so it reads on **both** light and dark GitHub |
| Dim | `676C60` | dates |

Find-and-replace those hex values to reskin the whole profile. **One caveat:** the `#` in
`countColor=%23C6F24E` is URL-encoded, so a careless regex over six-hex-digit runs will also
match the `23C6F2` straddling it. Replace the full six-character tokens above, not arbitrary
hex runs.

The discipline that makes this palette work: **one accent, nothing else competes.** The
toolbox badges are deliberately monochrome pills rather than each vendor's brand colour —
a rainbow row would fight the accent. Logo brightness encodes priority: bone for what you
ship with, lime for the agent stack, muted grey for the rest.

Lime on near-black reads as terminal/demoscene, which is the point — it matches shaders,
zero dependencies and "no build step" better than a warm accent did. It is also the most
aggressive of the options; if it ever feels loud, `#2DD4BF` (teal) is a drop-in swap for
`#C6F24E` that keeps every other token unchanged.

**How light/dark is handled** — GitHub serves one README to both themes, so each service is
handled differently:

- **capsule-render, typing-svg, shields, streak-stats, visitorbadge** take arbitrary hex, so
  they use transparent backgrounds and mid-tone text that reads on both.
- **github-profile-summary-cards** only accepts *named* themes — no custom hex. Its
  `transparent` theme works fine, but paints text teal `#417E87` and blue `#006AFF`, which
  fights the clay. So those cards use a `<picture>` element with `theme=github` for light
  mode and `theme=github_dark` for dark, which makes them blend into GitHub's own background
  instead of sitting there as a coloured slab.

If you edit a card, keep that rule: **arbitrary-hex service → transparent + mid-tone;
named-theme-only service → `<picture>`.**

**Typing header** — the rotating lines live in the `lines=` param of the
`readme-typing-svg.demolab.com` URL, separated by `;` and URL-encoded (spaces are `+`).

**Productive-time card** — currently `utcOffset=3`. Change it if that's not your timezone.

**Visitor counter** — resets if you change the `path=` param, so leave it alone.

---

## 5. Caveats worth knowing

- **GitHub caches images through its Camo proxy.** After you change a card URL, the old image
  can stick around for a few minutes. Hard-refresh or wait.
- **Streak stats** count contributions in your account timezone, and the public instance
  at `streak-stats.demolab.com` is generally reliable — but it's also someone else's free
  Vercel project. Same self-host option applies if it ever goes down.
- **`include_all_commits=true`** on github-readme-stats is slower and burns more API quota.
  Drop it if your self-hosted instance gets sluggish.
- **Location and email were left out on purpose** — your GitHub profile doesn't publish them,
  so neither does this. Add them if you want them public.

---

## Services used

| What | Where |
|---|---|
| Header/footer waves | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) |
| Typing animation | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) |
| Badges | [shields.io](https://shields.io) + [Simple Icons](https://simpleicons.org) |
| Visitor counter | [visitorbadge.io](https://visitorbadge.io) |
| Streak | [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) |
| Summary cards | [vn7n24fzkq/github-profile-summary-cards](https://github.com/vn7n24fzkq/github-profile-summary-cards) |
| Stats + pins *(commented)* | [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) |
| Trophies *(commented)* | [ryo-ma/github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) |
| Snake | [Platane/snk](https://github.com/Platane/snk) |

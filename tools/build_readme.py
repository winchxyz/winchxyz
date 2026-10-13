"""Writes README.md from the project list below.

Usage: python tools/build_readme.py
Add a project: put its 720x450 thumbnail in assets/p/<repo>.jpg (tools/thumbs.py makes them) and add a line here.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GH = 'https://github.com/winchxyz/'
PAGES = 'https://winchxyz.github.io/'

# (repo, one line, link label, live url or None for code only)
TOOLS = [
    ('loupe', 'A local website builder for Windows. AI makes the site, you fix it by hand on the live page.', 'Site', 'https://tryloupe.app/'),
    ('idea-to-build', 'A Claude Code plugin that turns a raw idea into a plan, with a critic that argues back.', None, None),
    ('motion-studio', 'A Claude Code workflow that turns one brief into a finished motion video. Every frame is code.', None, None),
    ('crunch-time', 'Watch your Claude Code agents work in a PS1-style office. The boss is your main session.', 'Open', PAGES + 'crunch-time/'),
    ('x-ghostwriter', 'Drafts X posts and replies in your voice with n8n, Grok and Claude. You press publish.', None, None),
    ('mc-print-3d', 'Turns Minecraft builds into multi-colour 3D-printable models.', None, None),
]

APPS = [
    ('spiralist', 'Turns a photo into a drawing made of one continuous line, and films it being drawn.', 'Open', PAGES + 'spiralist/'),
    ('typist', 'Turns a photo into text art you can paste into Instagram, X and Telegram.', 'Open', PAGES + 'typist/'),
    ('mosaiz', 'Turns a photo into a real mosaic, with a build video and a numbered 3D-print kit.', 'Open', PAGES + 'mosaiz/'),
    ('platen', 'A 3D manual typewriter. Write, draw typewriter art, or get a guide for your own machine.', 'Open', PAGES + 'platen/'),
    ('seedplot', 'A drawing machine with five styles. The same seed always gives the same picture.', 'Open', PAGES + 'seedplot/'),
    ('credits-cubed', 'A picture-cube puzzle made from Jack Butcher\'s Credits, each drawn from its onchain seed.', 'Play', PAGES + 'credits-cubed/'),
]

GAMES = [
    ('moon-rover', 'Drive a rover across the Moon and survey it. Every texture and sound is made in code.', 'Play', PAGES + 'moon-rover/'),
    ('tidewright', 'Build sandcastles on a beach that runs entirely on the GPU.', 'Play', PAGES + 'tidewright/'),
    ('celadon', 'A pottery game: throw a pot on the wheel, mix the glaze, fire the kiln.', 'Play', PAGES + 'celadon/'),
    ('vesper-street', 'Isometric survival horror in a drowned voxel town. The flashlight is your only weapon.', 'Play', PAGES + 'vesper-street/'),
    ('crayon-contraptions', 'A Rube Goldberg puzzle game drawn in crayon. 100 levels, seven crayons with their own physics.', 'Play', PAGES + 'crayon-contraptions/'),
    ('endless-fishing', 'An endless ocean under the same sky that is above you right now.', 'Play', PAGES + 'endless-fishing/'),
]

GRAPHICS = [
    ('motion-reels', 'Short motion videos made with AI and code.', 'Watch', PAGES + 'motion-reels/'),
    ('navis', 'A flooded Gothic cathedral rendered in real time, in one HTML file.', 'Open', PAGES + 'navis/'),
    ('aetherflow', 'A 3D fluid lab with real-time refraction and caustics.', 'Open', PAGES + 'aetherflow/'),
    ('cut', 'Slice objects along the exact path your mouse draws.', 'Play', PAGES + 'cut/'),
    ('solebound', 'A shoe-repair sim about roads that remember. One HTML file.', None, None),
    ('ant-farm', 'A 3D ant farm on a hand-written WebGL2 engine.', 'Play', PAGES + 'ant-farm/'),
]

INTRO = """I build whatever I need at the moment with Claude Code: AI tools I use every day, photo and design apps, browser games, motion videos, a converter from Minecraft builds to 3D prints. Everything here is open source, and most of it runs in the browser with nothing to install."""

LINKS = ('[X @winchxyz](https://x.com/winchxyz) &nbsp;·&nbsp; '
         '[winchxyz.github.io](https://winchxyz.github.io)')

ALSO = ('[zodiac-z13-z32](' + GH + 'zodiac-z13-z32) is a reproducible computational attack on two unsolved Zodiac ciphers, negative results included. '
        '[ar-butter](' + GH + 'ar-butter) lets you crack a stick of butter with your hands through a webcam. '
        '[winchxyz.github.io](' + GH + 'winchxyz.github.io) is my site, rendered on the GPU.')


def cell(repo, line, label, live):
    repo_url = GH + repo
    href = live or repo_url
    links = f'<a href="{live}">{label}</a> &nbsp;·&nbsp; <a href="{repo_url}">Code</a>' if live else f'<a href="{repo_url}">Code</a>'
    return (f'<td width="33%" valign="top">\n'
            f'<a href="{href}"><img src="assets/p/{repo}.jpg" alt="{repo}" width="100%"></a>\n'
            f'<br><b><a href="{repo_url}">{repo}</a></b>\n'
            f'<br><sub>{line}</sub>\n'
            f'<br><sub>{links}</sub>\n'
            f'</td>')


def grid(items):
    rows = []
    for i in range(0, len(items), 3):
        rows.append('<tr>\n' + '\n'.join(cell(*p) for p in items[i:i + 3]) + '\n</tr>')
    return '<table>\n' + '\n'.join(rows) + '\n</table>'


README = f"""<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.png">
  <img src="assets/header-light.png" alt="winchxyz. Tools, apps, games and video, built with Claude Code." width="100%">
</picture>

{INTRO}

{LINKS}

## Tools

{grid(TOOLS)}

## Photo and design apps

{grid(APPS)}

## Games

{grid(GAMES)}

## Graphics and video

{grid(GRAPHICS)}

## Also

{ALSO}

<sub>Every project on this page was built with Claude Code. All repositories: <a href="https://github.com/winchxyz?tab=repositories">github.com/winchxyz</a></sub>
"""

with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(README)
print('README.md written,', len(README), 'chars')

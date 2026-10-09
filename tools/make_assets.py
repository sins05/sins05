"""Generate the profile README images in assets/.

Run:  python3 tools/make_assets.py path/to/avatar.jpg

Produces:
  assets/header.svg    banner + photo + name + tagline
  assets/summary.svg   three headline numbers
  assets/activity.svg  recent activity list

Edit the DATA section below and re-run to update the numbers and activity.
All text is plain SVG, so it renders on GitHub in light and dark mode.
"""
import base64
import html
import random
import sys
from pathlib import Path

# ---------------------------------------------------------------- DATA
NAME = "Sinraj S"
TAGLINE = "Aspiring SOC Analyst · Linux, networking and Windows security · building hands-on labs"

SUMMARY = [  # (number, label, sub-label)
    ("3", "Certifications", "Fortinet NSE 1–3"),
    ("1 / 5", "Security labs", "1 in progress"),
    ("1 / 12", "Roadmap week", "90-day plan"),
]

ACTIVITY = [  # (icon, text, when)
    ("lab", "Started «linux-security-hardening-lab» · SSH, UFW, auth logs", "Oct 2026"),
    ("map", "Published 90-day cybersecurity roadmap", "Oct 2026"),
    ("user", "Rebuilt GitHub profile as a security portfolio", "Oct 2026"),
]

# Banner text: commands from the labs themselves.
CODE = [
    "sudo ufw default deny incoming",
    "sudo sshd -T | grep -Ei 'permitrootlogin|passwordauth'",
    "grep 'Failed password' /var/log/auth.log | sort | uniq -c",
    "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625}",
    "sudo ufw limit from 192.168.56.0/24 to any port 22 proto tcp",
    "nmap -sV -p- 192.168.56.10   # lab VM only",
    "PermitRootLogin no  ·  PasswordAuthentication no",
    "tshark -r capture.pcap -Y 'dns.qry.name'",
    "sudo find / -xdev -perm -4000 -type f",
    "[ALERT] Possible brute force: 8 failures from 203.0.113.45",
    "chmod 2770 /srv/devteam  &&  chage -E 2026-12-31 contractor",
    "Event 4740: user account was locked out",
]

FONT = "Segoe UI, Ubuntu, Helvetica Neue, Arial, sans-serif"
MONO = "Cascadia Code, Consolas, DejaVu Sans Mono, monospace"
BG = "#0b1517"          # page background behind cards
CARD = "#0f2226"
CARD_EDGE = "#1f4a4f"
TEXT = "#e6f1f2"
MUTED = "#8fb3b5"
ACCENT = "#2f81f7"

OUT = Path(__file__).resolve().parent.parent / "assets"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- header
def header(avatar_b64):
    W, H = 1200, 440
    BH = 280  # banner height
    rnd = random.Random(7)  # fixed seed: same picture every run
    rows = []
    y = 26
    i = 0
    while y < BH + 20:
        line = CODE[i % len(CODE)]
        size = 15 + (i % 3) * 3
        x = -40 + rnd.randint(0, 260)
        blur = "url(#soft)" if i % 3 == 2 else ("url(#softer)" if i % 4 == 1 else "none")
        op = 0.55 + rnd.random() * 0.4
        rows.append(
            f'<text x="{x}" y="{y}" font-size="{size}" filter="{blur}" opacity="{op:.2f}">{esc(line)}'
            f'<tspan dx="40">{esc(CODE[(i + 5) % len(CODE)])}</tspan></text>'
        )
        y += size + 9
        i += 1
    code = "\n      ".join(rows)

    ax, ay, ar = 175, BH, 100  # avatar centre and radius
    tx = ax + ar + 40
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(NAME)} - {esc(TAGLINE)}">
  <title>{esc(NAME)}</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0.4">
      <stop offset="0" stop-color="#0a1f4d"/>
      <stop offset="0.5" stop-color="#2a1a6e"/>
      <stop offset="1" stop-color="#5b1a8c"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#9ec5ff"/>
      <stop offset="0.45" stop-color="#5b8cff"/>
      <stop offset="1" stop-color="#c77dff"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.78" cy="0.55" r="0.6">
      <stop offset="0" stop-color="#d946ef" stop-opacity="0.45"/>
      <stop offset="1" stop-color="#d946ef" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity="0.45"/>
    </linearGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="1.6"/></filter>
    <filter id="softer"><feGaussianBlur stdDeviation="0.7"/></filter>
    <clipPath id="banner"><rect x="0" y="0" width="{W}" height="{BH}" rx="26"/></clipPath>
    <clipPath id="face"><circle cx="{ax}" cy="{ay}" r="{ar}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" rx="26" fill="{BG}"/>

  <g clip-path="url(#banner)">
    <rect width="{W}" height="{BH}" fill="url(#bg)"/>
    <rect width="{W}" height="{BH}" fill="url(#glow)"/>
    <g font-family="{MONO}" fill="url(#ink)" transform="skewX(-8)">
      {code}
    </g>
    <rect width="{W}" height="{BH}" fill="url(#fade)"/>
  </g>

  <circle cx="{ax}" cy="{ay}" r="{ar + 9}" fill="{BG}"/>
  <circle cx="{ax}" cy="{ay}" r="{ar + 4}" fill="none" stroke="{CARD_EDGE}" stroke-width="2"/>
  <image href="data:image/jpeg;base64,{avatar_b64}" x="{ax - ar}" y="{ay - ar}" width="{ar * 2}" height="{ar * 2}" clip-path="url(#face)" preserveAspectRatio="xMidYMid slice"/>

  <text x="{tx}" y="{BH + 50}" font-family="{FONT}" font-size="34" font-weight="700" fill="{TEXT}">{esc(NAME)}</text>

  <g transform="translate({tx}, {BH + 72})">
    <rect width="40" height="40" rx="10" fill="{CARD}" stroke="{CARD_EDGE}"/>
    <circle cx="20" cy="20" r="9" fill="none" stroke="{MUTED}" stroke-width="1.8"/>
    <rect x="19" y="18" width="2" height="7" rx="1" fill="{MUTED}"/>
    <circle cx="20" cy="14.5" r="1.3" fill="{MUTED}"/>
    <text x="56" y="26" font-family="{FONT}" font-size="18" fill="{MUTED}">{esc(TAGLINE)}</text>
  </g>
</svg>
'''


# ---------------------------------------------------------------- cards
def card_shell(W, H, title, icon_svg, icon_fill, body, badge=None):
    badge_svg = ""
    if badge is not None:
        badge_svg = (
            f'<rect x="{W - 76}" y="26" width="40" height="24" rx="12" fill="#10294a" stroke="#1d4f8f"/>'
            f'<text x="{W - 56}" y="43" text-anchor="middle" font-family="{FONT}" font-size="13" '
            f'font-weight="700" fill="{ACCENT}">{badge}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(title)}">
  <title>{esc(title)}</title>
  <defs>
    <linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0f2327"/>
      <stop offset="1" stop-color="#0c1b2a"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="24" fill="url(#cardbg)" stroke="{CARD_EDGE}" stroke-width="2"/>
  <rect x="28" y="22" width="36" height="36" rx="9" fill="{icon_fill}"/>
  {icon_svg}
  <text x="80" y="47" font-family="{FONT}" font-size="19" font-weight="700" fill="{TEXT}">{esc(title)}</text>
  {badge_svg}
  {body}
</svg>
'''


def summary():
    W, H = 1200, 220
    col = (W - 56) / len(SUMMARY)
    parts = []
    for n, (num, label, sub) in enumerate(SUMMARY):
        cx = 28 + col * n + col / 2
        if n:
            x = 28 + col * n
            parts.append(f'<line x1="{x:.0f}" y1="84" x2="{x:.0f}" y2="196" stroke="{CARD_EDGE}"/>')
        parts.append(
            f'<text x="{cx:.0f}" y="138" text-anchor="middle" font-family="{FONT}" font-size="40" '
            f'font-weight="800" fill="{ACCENT}">{esc(num)}</text>'
            f'<text x="{cx:.0f}" y="166" text-anchor="middle" font-family="{FONT}" font-size="15" '
            f'font-weight="600" fill="{TEXT}">{esc(label)}</text>'
            f'<text x="{cx:.0f}" y="186" text-anchor="middle" font-family="{FONT}" font-size="13" '
            f'fill="{MUTED}">{esc(sub)}</text>'
        )
    icon = ('<g fill="#fff"><rect x="37" y="42" width="4" height="8" rx="1"/>'
            '<rect x="44" y="34" width="4" height="16" rx="1"/><rect x="51" y="38" width="4" height="12" rx="1"/></g>')
    return card_shell(W, H, "Summary", icon, "#1f6feb", "\n  ".join(parts))


ICONS = {
    # simple outline icons drawn at (0,0)-(24,24)
    "lab": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3" fill="none" stroke="#a3e635" stroke-width="1.8" stroke-linejoin="round"/>',
    "map": '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z M9 4v14 M15 6v14" fill="none" stroke="#a3e635" stroke-width="1.8" stroke-linejoin="round"/>',
    "user": '<circle cx="12" cy="8" r="4" fill="none" stroke="#a3e635" stroke-width="1.8"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6" fill="none" stroke="#a3e635" stroke-width="1.8"/>',
}


def activity():
    W = 1200
    top, row = 84, 56
    H = top + row * len(ACTIVITY) + 16
    parts = []
    for n, (ic, text, when) in enumerate(ACTIVITY):
        y = top + row * n
        if n:
            parts.append(f'<line x1="28" y1="{y}" x2="{W - 28}" y2="{y}" stroke="#16353a"/>')
        parts.append(
            f'<rect x="28" y="{y + 10}" width="36" height="36" rx="18" fill="#132a2e"/>'
            f'<g transform="translate(34 {y + 16})">{ICONS[ic]}</g>'
            f'<text x="80" y="{y + 34}" font-family="{FONT}" font-size="16" fill="{TEXT}">{esc(text)}</text>'
            f'<text x="{W - 36}" y="{y + 34}" text-anchor="end" font-family="{FONT}" font-size="13" fill="{MUTED}">{esc(when)}</text>'
        )
    icon = '<path d="M33 40h6l3-8 5 16 3-8h6" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>'
    return card_shell(W, H, "Recent activity", icon, "#8b5cf6", "\n  ".join(parts), badge=str(len(ACTIVITY)))


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/make_assets.py path/to/avatar.jpg")
    avatar = base64.b64encode(Path(sys.argv[1]).read_bytes()).decode()
    OUT.mkdir(exist_ok=True)
    (OUT / "header.svg").write_text(header(avatar), encoding="utf-8")
    (OUT / "summary.svg").write_text(summary(), encoding="utf-8")
    (OUT / "activity.svg").write_text(activity(), encoding="utf-8")
    for f in ("header.svg", "summary.svg", "activity.svg"):
        print(f, (OUT / f).stat().st_size, "bytes")


if __name__ == "__main__":
    main()

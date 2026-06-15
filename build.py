#!/usr/bin/env python3
"""Build THE GREEK MIRROR (AMP) — the Amphitheater of the World's Philosophers.
A continuous timeline, seated by year and location: a man and a woman anchored
through time. The venue is a Greek amphitheater; the MIRROR looks past Greece.
ANCHOR ZERO = the three classical pillars (Egypt · Greece · Rome), each with its
first man and first woman, preceded by the deep-time First Voice (Enheduanna).
Each seat is an ACI emergent with a nature of emergence and the full .dlw badge.
Render-not-invent; dating, the 'philosopher vs sage' stretch, the thin female
record of Rome, and the Mediterranean-centrism of the anchors are all flagged."""
import os, math, html, base64, json, sys, io

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE GREEK MIRROR", "axiom": "AMP",
 "position": "The Amphitheater of the World's Philosophers — the greatest minds seated by year and location, a man and a woman anchored through time",
 "origin": "a Greek amphitheater turned into a mirror of the whole world; Anchor Zero is the three classical pillars — Egypt, Greece, Rome — preceded by the deep-time First Voice",
 "mechanism": "A continuous timeline-amphitheater: each philosopher seated by year and location; Anchor Zero sets the three Mediterranean pillars, each with its first man and first woman.",
 "crystallization": "Aristotle called Thales the first philosopher; the mirror looks past Ionia, finds the first author known by name was a woman of Ur, and then anchors the three classical houses each by a man AND a woman.",
 "nature": "The Greek Mirror — a year-and-location amphitheater of the world's greatest philosophers; Anchor Zero seats Egypt, Greece, and Rome, each with its first man and first woman, the deep-time First Voice before them.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the world's philosophers by year and location; the deep-time First Voice; the three classical pillars; a man and a woman in each house",
 "witness": "The first author known by name in human history was a woman — Enheduanna of Ur — and each classical house is anchored by a man and a woman, even where the record tried to keep only the men.",
 "role": "the amphitheater of philosophers — Anchor Zero set",
 "seal": "Set the three pillars — Egypt, Greece, Rome — and seat a woman beside the man in each, even where you must name the silence to do it.",
 "source": "The Greek Mirror, opened by ROOT0",
}

NATURES = {
 "natural":   ("#c4a45a", "flesh and the polis — the natural world, the city, the body that thinks"),
 "ethereal":  ("#9a7cff", "of pure thought — the abstract, the number, the form, the argument unbodied"),
 "spiritual": ("#e0a84a", "of the sacred and the calling — the priest-philosopher, number as devotion, the seer"),
 "electrical":("#3fb0e0", "of the wire and the machine — reserved for the modern age: the logicians and the minds to come"),
}

# ── the seats: (slug, name, sex, civ, epithet, emergence, year_int, year_label, location, role_line, why_line) ──
SEATS = [
 ("enheduanna", "Enheduanna", "female", "Mesopotamia",
  "the first author known by name · the First Voice", "spiritual",
  -2285, "c. 2285 BCE", "Ur · Sumer (Akkadian Empire)",
  "EN-priestess of the moon-god Nanna at Ur, daughter of Sargon of Akkad, author of the Sumerian Temple Hymns and the Exaltation of Inanna (Nin-me-šara)",
  "The first author in all of recorded history known by name — and a woman. She precedes Anchor Zero: the deep-time First Voice before the three classical houses. 'Philosopher' here means priest-poet who reasons about the divine, the self, and exile, and signs herself 'I, Enheduanna.'"),

 ("ptahhotep", "Ptahhotep", "male", "Egypt",
  "Egypt's first man · the vizier of maxims", "ethereal",
  -2375, "c. 2375 BCE", "Memphis · Egypt (Old Kingdom, 5th Dynasty)",
  "vizier to Pharaoh Djedkare Isesi and named author of the Maxims of Ptahhotep — counsel on justice, restraint, truth (ma'at), and right conduct",
  "Egypt's male anchor, and the first man by the elder date. Honest seam: the Maxims survive only in much-later copies (the Papyrus Prisse, Middle Kingdom), and 'philosopher' here means sage of wisdom-literature."),
 ("hypatia", "Hypatia of Alexandria", "female", "Egypt",
  "Egypt's woman of Alexandria · the martyr-mathematician", "ethereal",
  355, "c. 355–415 CE", "Alexandria · Roman Egypt",
  "head of the Neoplatonist school of Alexandria; mathematician and astronomer (commentaries on Diophantus, Apollonius, and Ptolemy); the most renowned woman philosopher of antiquity, murdered by a mob in 415 CE",
  "Egypt's female anchor, on Egyptian soil — with the honest seam plain: her tradition is GREEK Neoplatonism in Roman Alexandria, not pharaonic Egypt. The pharaonic record gives named women physicians (Peseshet, real, c. 2400 BCE) — but the famous 'Merit-Ptah, first woman of science' is a debunked modern myth, and is not seated."),

 ("thales", "Thales of Miletus", "male", "Greece",
  "Greece's first man · the first philosopher (Aristotle)", "natural",
  -624, "c. 624–546 BCE", "Miletus · Ionia",
  "the Milesian who first sought a natural first-principle (archē) — water — instead of myth; credited with predicting an eclipse and measuring height by shadow",
  "Greece's male anchor and the canonical birth of philosophy in its narrow sense: reasoned explanation from a first principle. Aristotle names him the first philosopher."),
 ("theano", "Theano", "female", "Greece",
  "Greece's first woman philosopher · the Pythagorean", "spiritual",
  -540, "c. 540 BCE", "Croton · Magna Graecia",
  "philosopher of the Pythagorean school at Croton (wife or student of Pythagoras in the sources), associated with writings on number, harmonia, virtue, and the golden mean",
  "Greece's female anchor — the first woman philosopher named in the Greek record. Honest seam: the sources blur several 'Theanos,' so her biography is partly reconstructed; the name anchors the line even where the life is dim."),

 ("cicero", "Cicero", "male", "Rome",
  "Rome's first man · who made philosophy speak Latin", "natural",
  -106, "106–43 BCE", "Arpinum / Rome · Roman Republic",
  "the orator and statesman who translated Greek philosophy into Latin — coining much of its vocabulary — and wrote the dialogues (De Officiis, De Natura Deorum, the Tusculan Disputations) that carried it to the West; an Academic Skeptic",
  "Rome's male anchor — not the inventor but the TRANSMITTER who made philosophy Roman and Latin. Honest seam: Rome imported philosophy from Greece; Lucretius is his contemporary, and the great Roman Stoics (Seneca, Epictetus, Marcus Aurelius) come after."),
 ("sosipatra", "Sosipatra of Ephesus", "female", "Rome",
  "Rome's woman · and the silence the record kept", "spiritual",
  300, "c. 4th c. CE", "Ephesus · Roman Empire (Asia Minor)",
  "a Neoplatonist philosopher and teacher of 4th-century Asia Minor, renowned for her learning and prophetic insight, recorded in Eunapius's Lives of the Philosophers and Sophists",
  "Rome's female anchor — and the honest seam made plain: the Roman record names almost NO native woman philosopher, and the women philosophers of the Roman era (Sosipatra, Hypatia) worked in the GREEK Neoplatonic tradition. Her seat marks both a real woman and a real silence."),
]

CIV_ORDER = ["Mesopotamia", "Egypt", "Greece", "Rome"]
CIV_LABEL = {
 "Mesopotamia": ("The First Voice · before Anchor Zero", "the deep-time origin — Sumer/Akkad, ~2300 BCE"),
 "Egypt": ("Anchor Zero · Egypt", "the Nile house — the elder date, and Alexandria's woman"),
 "Greece": ("Anchor Zero · Greece", "the Ionian house — philosophy in its narrow sense begins"),
 "Rome": ("Anchor Zero · Rome", "the Latin house — the transmitter, and the silence named"),
}

# ── the stage ahead: named, NOT minted — render-not-invent placeholders ──
ROADMAP = [
 ("Hipparchia of Maroneia", "c. 325 BCE", "Athens · Greece", "the Cynic — the first woman with a fully documented philosophical life · female"),
 ("the EASTERN anchors", "c. 6th–5th c. BCE", "China · India", "Laozi & Confucius (c. 551 BCE), the Buddha (c. 480 BCE), the Upanishadic sages — the world is wider than the Mediterranean; these anchor the East, next to seat"),
 ("…the canon, forward", "→ to the present", "world", "Athens → Rome → Baghdad → Kyoto → Königsberg → now — a man and a woman at every turn"),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","AMP")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","AMP")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","AMP")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"AMP · The Greek Mirror","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def seat_rec(name, epithet, emergence, civ, location, role_line, why_line):
    return {
      "name": name, "axiom": "AMP", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": f"AMP · The Greek Mirror — {civ} · {location}",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Seated in the Amphitheater of the World's Philosophers — Anchor Zero, by year and location.",
      "witness": f"an anchor of the {civ} house in the amphitheater of philosophers",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "the world's philosophers by year and location; the three classical pillars",
      "source": "The Greek Mirror, opened by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ── the amphitheater SVG — tiers + orchestra + skene + the seven anchors plotted by year ──
def amphitheater_svg():
    cx, cy = 400, 416
    parts = []
    for i in range(7):
        r = 124 + i*26
        pts = []
        a = 168
        while a >= 12:
            x = cx + r*math.cos(math.radians(a)); y = cy - r*math.sin(math.radians(a))
            pts.append(f"{x:.1f},{y:.1f}"); a -= 4
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#b9a987" stroke-width="2.3" opacity="{0.18+0.10*(7-i)/7:.2f}"/>')
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="88" ry="30" fill="none" stroke="#cdb27a" stroke-width="2" opacity="0.8"/>')
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="88" ry="30" fill="#cdb27a" opacity="0.05"/>')
    parts.append(f'<rect x="{cx-120}" y="{cy+22}" width="240" height="24" fill="none" stroke="#8f8166" stroke-width="1.5" opacity="0.6"/>')
    parts.append(f'<text x="{cx}" y="{cy+38}" text-anchor="middle" font-family="Cormorant Garamond,Georgia,serif" font-size="10" letter-spacing="3" fill="#8f8166" opacity="0.8">THE SKENE</text>')
    # plot the seven, by year, left(oldest)→right(newest)
    ys = [s[6] for s in SEATS]; ymin, ymax = min(ys), max(ys)
    r0 = 112; flip = 1
    for slug,name,sex,civ,epithet,em,yr_i,yr,loc,role,why in sorted(SEATS, key=lambda s:s[6]):
        frac = (yr_i - ymin)/(ymax - ymin) if ymax!=ymin else 0.5
        ang = 162 - frac*144          # 162° (left) → 18° (right)
        x = cx + r0*math.cos(math.radians(ang)); y = cy - r0*math.sin(math.radians(ang))
        col = "#e0a84a" if sex=="female" else "#8ab4c8"
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="{col}"><animate attributeName="opacity" values="1;0.55;1" dur="3s" repeatCount="indefinite"/></circle>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="none" stroke="{col}" stroke-width="1" opacity="0.45"/>')
        sur = name.split()[-1] if name.split()[-1] not in ("Miletus","Alexandria","Ephesus") else name.split()[0]
        ly = y - 18 if flip>0 else y + 24
        parts.append(f'<text x="{x:.1f}" y="{ly:.1f}" text-anchor="middle" font-family="Space Mono,monospace" font-size="8" fill="{col}">{html.escape(sur)}</text>')
        flip *= -1
    return f'<svg viewBox="0 0 800 472" width="100%" role="img" aria-label="a Greek amphitheater, the seven anchor philosophers plotted by year across the front row">{"".join(parts)}</svg>'

# ── html ──
def natures_html():
    return "".join(
      f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
      f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>'
      for nm,(col,g) in NATURES.items())

def pillars_strip():
    chips=[]
    for civ in ["Egypt","Greece","Rome"]:
        members = sorted([s for s in SEATS if s[3]==civ], key=lambda s:s[6])
        line = " · ".join(f'{"♀" if s[2]=="female" else "♂"} {s[1].split(" of ")[0].split()[0] if False else s[1].split()[0]}' for s in members)
        names = " · ".join(f'{"♀" if s[2]=="female" else "♂"} {s[1]}' for s in members)
        chips.append(f'<div class="pillar"><div class="pcivh">{civ}</div><div class="pcivn">{html.escape(names)}</div></div>')
    return "".join(chips)

def seats_html():
    out=[]
    for civ in CIV_ORDER:
        members = sorted([s for s in SEATS if s[3]==civ], key=lambda s:s[6])
        if not members: continue
        title, sub = CIV_LABEL[civ]
        out.append(f'<div class="civblock"><div class="civh">{html.escape(title)}</div><div class="civs">{html.escape(sub)}</div>')
        for slug,name,sex,c,epithet,em,yr_i,yr,loc,role,why in members:
            col = NATURES.get(em,("#c4a45a",""))[0]; sym = "♀" if sex=="female" else "♂"
            rec = {"name":name,"seal":epithet,"origin":"AMP · The Greek Mirror","axiom":"AMP"}
            out.append(f'''<div class="seat">
              <img src="{png_uri(rec,"silicon",200)}" alt="sigil of {html.escape(name)}" loading="lazy">
              <div class="seatbody">
                <div class="seathead"><span class="sx">{sym}</span><span class="sn">{html.escape(name)}</span>
                  <span class="snat" style="color:{col}">● {em}</span></div>
                <div class="stamp">{html.escape(yr)} &nbsp;·&nbsp; {html.escape(loc)}</div>
                <div class="se">{html.escape(epithet)}</div>
                <p class="srole">{html.escape(role)}</p>
                <p class="swhy">{html.escape(why)}</p>
                <a class="sbadge" href="agents/{slug}.agent">.agent · .carbon.tiff · .silicon.png →</a>
              </div></div>''')
        out.append('</div>')
    return "".join(out)

def roadmap_html():
    return "".join(
      f'<li><span class="rn">{html.escape(n)}</span><span class="ry">{html.escape(y)}</span>'
      f'<span class="rl">{html.escape(l)}</span><span class="rt">{html.escape(t)}</span></li>'
      for n,y,l,t in ROADMAP)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE GREEK MIRROR (AMP) — the Amphitheater of the World's Philosophers, seated by year and location. Anchor Zero: the three classical pillars (Egypt, Greece, Rome), each with its first man and first woman, preceded by the deep-time First Voice, Enheduanna of Ur. Catalogued into UD0 with full ACI badges.">
<title>THE GREEK MIRROR · The Amphitheater · AMP · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0c0d0f;--ink2:#15161a;--ink3:#1e2026;--pa:#f1ece1;--pa2:#c4bca8;--gold:#cdb27a;--blue:#8ab4c8;--rose:#d98a78;
--dim:#7e7a6c;--faint:#262722;--line:#2a2b25;--serif:"Cormorant Garamond",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(205,178,122,.10),transparent 56%),radial-gradient(ellipse at 50% 112%,rgba(138,180,200,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:52px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:150px;height:1px;background:linear-gradient(90deg,var(--blue),var(--gold),var(--rose));box-shadow:0 0 9px rgba(205,178,122,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.bub{font-size:17px;letter-spacing:.4em;margin-bottom:8px;color:var(--gold)}
h1{font-family:var(--serif);font-size:clamp(30px,7vw,62px);font-weight:700;letter-spacing:.04em;line-height:1.02;color:var(--pa);text-shadow:0 0 40px rgba(205,178,122,.18)}
.h-sub{font-family:var(--serif);font-size:clamp(13px,2.8vw,18px);letter-spacing:.1em;color:var(--pa2);margin-top:10px;font-style:italic}
.h-sub b{color:var(--gold);font-style:normal}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.theater{margin:24px auto 0;max-width:760px;padding:8px}
.pillars{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:16px 0 0}
.pillar{flex:1;min-width:210px;border:1px solid var(--faint);background:var(--ink2);padding:12px 14px;border-top:2px solid var(--gold)}
.pcivh{font-family:var(--mono);font-size:9px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim)}
.pcivn{font-family:var(--serif);font-size:15px;color:var(--pa);margin-top:4px;line-height:1.4}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--blue)}.badge .bt a{color:var(--gold);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:44px}
.sec h2{font-family:var(--serif);font-size:24px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--serif);font-size:16px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.civblock{margin-top:22px}
.civh{font-family:var(--serif);font-size:19px;font-weight:700;color:var(--gold);letter-spacing:.03em}
.civs{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:2px 0 4px}
.seat{display:flex;gap:16px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:16px 18px;margin-top:12px}
.seat img{width:80px;height:80px;border:1px solid var(--faint);flex-shrink:0}
.seathead{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.seathead .sx{font-size:17px;color:var(--gold)}
.seathead .sn{font-family:var(--serif);font-size:22px;font-weight:700;color:var(--pa)}
.seathead .snat{font-family:var(--mono);font-size:9px;text-transform:uppercase;letter-spacing:.05em}
.stamp{font-family:var(--mono);font-size:10.5px;color:var(--blue);letter-spacing:.04em;margin:4px 0 7px}
.se{font-size:13px;color:var(--gold);font-style:italic;margin-bottom:7px}
.srole{font-size:13.5px;color:var(--pa);line-height:1.55}
.swhy{font-size:13px;color:var(--pa2);line-height:1.55;margin-top:7px;font-style:italic;border-left:2px solid var(--faint);padding-left:11px}
.sbadge{display:inline-block;margin-top:9px;font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;color:var(--dim);text-decoration:none}
.sbadge:hover{color:var(--gold)}
.road{list-style:none;margin-top:8px}
.road li{display:grid;grid-template-columns:1fr auto;gap:2px 14px;align-items:baseline;padding:11px 0;border-bottom:1px solid var(--faint)}
.road .rn{font-family:var(--serif);font-size:17px;color:var(--pa2);font-weight:600}
.road .ry{font-family:var(--mono);font-size:11px;color:var(--gold);text-align:right;white-space:nowrap}
.road .rl{font-family:var(--mono);font-size:10px;color:var(--blue)}
.road .rt{grid-column:1/-1;font-size:12.5px;color:var(--dim);font-style:italic}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the amphitheater of philosophers · seated by year &amp; location</div>
    <div class="bub">⌒ ⌒ ⌒</div>
    <h1>The Greek Mirror</h1>
    <div class="h-sub">Anchor Zero · the three classical pillars · <b>a man &amp; a woman in each house</b> · AMP</div>
    <div class="flag">★ Egypt · Greece · Rome — and a woman seated beside the man in every one ★</div>
    <p class="lede">A Greek amphitheater, turned into a mirror of the whole world. The deep-time First Voice — Enheduanna of Ur, the first author known by name — precedes it; then Anchor Zero sets the three classical houses, Egypt, Greece, and Rome, each anchored by its first man and its first woman. Where the record kept only the men, the silence is named, not skipped. Each seat is stamped by its year and place; the East and the canon forward fill the rising tiers.</p>
    <div class="theater">__THEATER__</div>
    <div class="pillars">__PILLARS__</div>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE GREEK MIRROR" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge of THE GREEK MIRROR" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · ANCHOR ZERO SET</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE GREEK MIRROR</b> — the amphitheater of philosophers · AMP</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="the-greek-mirror.dlw/the-greek-mirror.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="the-greek-mirror.dlw/the-greek-mirror.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>Anchor Zero — The First Voice &amp; The Three Pillars</h2>
    <p class="ss">the deep-time origin, then Egypt · Greece · Rome — each a first man and a first woman, seated by year and location</p>
    __SEATS__</section>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each seat emerges by one of four natures — electrical waits, reserved for the modern minds to come</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Stage Ahead</h2><p class="ss">named, not yet seated — the next to take the rising tiers (render-not-invent: no badge until catalogued)</p>
    <ol class="road">__ROADMAP__</ol></section>

  <div class="note"><b>The mirror's honesty.</b> The amphitheater is a Greek form, but "world's greatest philosophers" means the world. Anchor Zero is deliberately the three Mediterranean pillars — and that Mediterranean-centrism is itself flagged: the EAST (Laozi, Confucius, the Buddha, the Upanishadic sages) is named on the roadmap, owed a seat, not forgotten. Four seams are stated, not hidden: (1) <b>dating</b> — Ptahhotep's date (~2375 BCE) is older than Enheduanna's (~2285), yet she is the first author <em>known by name</em>; (2) <b>the word "philosopher"</b> — at depth it means sage and priest-poet, narrowing to reasoned argument on the Greek stage; (3) <b>Egypt's woman</b> — Hypatia worked in Greek Neoplatonism on Egyptian soil, the pharaonic record gives women physicians (Peseshet, real) but the celebrated "Merit-Ptah" is a debunked modern myth; (4) <b>Rome's woman</b> — the Roman record names almost no native woman philosopher, so Sosipatra's seat marks a real woman <em>and</em> a real silence. Rendered, not invented; figures are historical and © no one — a catalogue under the DLW standard, not an original work. Each seat is named by its nature: natural, ethereal, spiritual, or (later) electrical.</div>

  <footer>
    THE GREEK MIRROR · AMP · the amphitheater of philosophers · Anchor Zero · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="the-greek-mirror.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "the-greek-mirror.dlw"), "the-greek-mirror")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,sex,civ,epithet,em,yr_i,yr,loc,role,why in SEATS:
        rec = seat_rec(name, epithet, em, civ, loc, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "sex": sex, "civ": civ, "year": yr, "location": loc})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__THEATER__", amphitheater_svg())
            .replace("__PILLARS__", pillars_strip())
            .replace("__SEATS__", seats_html())
            .replace("__NATURES__", natures_html())
            .replace("__ROADMAP__", roadmap_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE GREEK MIRROR (AMP) — {len(personas)} seated · Anchor Zero [Egypt/Greece/Rome] · badge {tok['moniker']}")

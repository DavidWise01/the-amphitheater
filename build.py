#!/usr/bin/env python3
"""Build THE GREEK MIRROR (AMP) — the Amphitheater of the World's Philosophers.
A continuous timeline, seated by year and location: the greatest minds, a man and
a woman anchored through time. The venue is a Greek amphitheater; the MIRROR looks
past Greece and finds the first seat is neither Greek nor male. It opens in deep
time with the two firsts, then the Greek stage and the canon flow forward.
Each seat is an ACI emergent with a nature of emergence and the full .dlw badge.
Render-not-invent; dating and the 'philosopher vs sage/poet' stretch are flagged."""
import os, math, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE GREEK MIRROR", "axiom": "AMP",
 "position": "The Amphitheater of the World's Philosophers — the greatest minds seated by year and location, a man and a woman anchored through time",
 "origin": "a Greek amphitheater turned into a mirror of the whole world, so that the first seat is neither Greek nor a man",
 "mechanism": "A continuous timeline-amphitheater: each philosopher seated by year and location, opening with the deep-time prologue before Greece, then the Greek stage and the canon forward.",
 "crystallization": "Aristotle called Thales the first philosopher; the mirror looks past Ionia and finds, seventeen centuries earlier, a woman of Ur with her name already on the page.",
 "nature": "The Greek Mirror — a year-and-location amphitheater of the world's greatest philosophers; it begins not in 6th-century Miletus but in the deep time the Greek story leaves out.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the world's philosophers by year and location; the deep-time prologue; the Greek stage; a man and a woman through time",
 "witness": "The first author known by name in human history was a woman — Enheduanna of Ur — and the amphitheater seats her first.",
 "role": "the amphitheater of philosophers — opened",
 "seal": "Build the Greek theater, then turn it into a mirror: the front row was never Athens, and the first voice was never his.",
 "source": "The Greek Mirror, opened by ROOT0",
}

# cross-lineage taxonomy — AMP-flavored glosses (electrical reserved for the modern seats to come)
NATURES = {
 "natural":   ("#c4a45a", "flesh and the polis — the mortal life, the city, the body that thinks"),
 "ethereal":  ("#9a7cff", "of pure thought — the abstract, the form, the argument unbodied"),
 "spiritual": ("#e0a84a", "of the sacred and the calling — the priest-philosopher, wisdom as devotion"),
 "electrical":("#3fb0e0", "of the wire and the machine — reserved for the modern age: the logicians and the minds to come"),
}

# ── the seats: (slug, name, sex, epithet, emergence, year_int, year_label, location, role_line, why_line) ──
# year_int is for sorting only (negative = BCE).
SEATS = [
 ("ptahhotep", "Ptahhotep", "male", "the vizier of maxims · the first man, by the elder date", "ethereal",
  -2375, "c. 2375 BCE", "Memphis · Egypt (Old Kingdom, 5th Dynasty)",
  "vizier to Pharaoh Djedkare Isesi and named author of the Maxims of Ptahhotep — the Instruction: a father's counsel on justice, restraint, truth (ma'at), and right conduct",
  "He is the first man seated by the elder date: ethics set down as teaching. Honest seam — the Maxims survive only in much later copies (the Papyrus Prisse, Middle Kingdom), so the man is older than any page we hold of him, and 'philosopher' here means sage of wisdom-literature."),
 ("enheduanna", "Enheduanna", "female", "the first author known by name · the first voice of the mirror", "spiritual",
  -2285, "c. 2285 BCE", "Ur · Sumer (Akkadian Empire)",
  "EN-priestess (high priestess) of the moon-god Nanna at Ur, daughter of Sargon of Akkad, author of the Sumerian Temple Hymns and the Exaltation of Inanna (Nin-me-šara)",
  "She is the first author in all of recorded history known by name — and a woman. Her hymns do not merely praise; they reason about the divine, the self, and exile, and sign themselves 'I, Enheduanna.' The mirror seats her first. Honest seam — calling her 'philosopher' stretches the word from its Greek sense toward poet-theologian; that stretch is the point, not a slip."),
]

# ── the stage ahead: named, NOT minted — the next seats to fill (render-not-invent placeholders) ──
ROADMAP = [
 ("Thales of Miletus", "c. 624 BCE", "Miletus · Ionia", "the canonical 'first philosopher' (Aristotle) — the Greek stage opens here · male"),
 ("Theano", "c. 540 BCE", "Croton · Magna Graecia", "the first named woman philosopher of Greece, of the Pythagorean school · female"),
 ("Hipparchia of Maroneia", "c. 325 BCE", "Athens · Greece", "the Cynic — the first woman with a fully documented philosophical life · female"),
 ("…the canon, forward", "→ to the present", "world", "Athens → Rome → Baghdad → Kyoto → Königsberg → now — a man and a woman at every turn"),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
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

def seat_rec(name, epithet, emergence, location, role_line, why_line):
    return {
      "name": name, "axiom": "AMP", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": f"AMP · The Greek Mirror — {location}",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Seated in the Amphitheater of the World's Philosophers, by year and location.",
      "witness": "a voice of the deep-time prologue, before the Greek stage",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "the world's philosophers by year and location; the mirror that looks past Greece",
      "source": "The Greek Mirror, opened by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ── the amphitheater SVG (computed arcs + the two seated firsts) ──
def amphitheater_svg():
    cx, cy = 400, 412
    tiers = 7
    parts = []
    # rising tiers of stone (polylines, robust against arc-flag confusion)
    for i in range(tiers):
        r = 122 + i*26
        pts = []
        a = 168
        while a >= 12:
            x = cx + r*math.cos(math.radians(a)); y = cy - r*math.sin(math.radians(a))
            pts.append(f"{x:.1f},{y:.1f}"); a -= 4
        op = 0.20 + 0.10*(tiers-i)/tiers
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#b9a987" stroke-width="2.4" opacity="{op:.2f}"/>')
    # the diazoma (a brighter dividing arc)
    # orchestra — the round dancing floor, in perspective
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="86" ry="30" fill="none" stroke="#cdb27a" stroke-width="2" opacity="0.8"/>')
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="86" ry="30" fill="#cdb27a" opacity="0.05"/>')
    # the skene (stage building) below the orchestra
    parts.append(f'<rect x="{cx-120}" y="{cy+22}" width="240" height="26" fill="none" stroke="#8f8166" stroke-width="1.6" opacity="0.6"/>')
    parts.append(f'<text x="{cx}" y="{cy+39}" text-anchor="middle" font-family="Cormorant Garamond,Georgia,serif" font-size="11" letter-spacing="3" fill="#8f8166" opacity="0.8">THE SKENE</text>')
    # the two seated firsts — front tier
    seats_geo = [(108, "#e0a84a", "ENHEDUANNA", "c. 2285 BCE · Ur", "♀ first"),
                 (72,  "#8ab4c8", "PTAHHOTEP",  "c. 2375 BCE · Memphis", "♂ first")]
    r0 = 112
    for ang, col, nm, yl, tag in seats_geo:
        x = cx + r0*math.cos(math.radians(ang)); y = cy - r0*math.sin(math.radians(ang))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{col}"><animate attributeName="opacity" values="1;0.55;1" dur="3s" repeatCount="indefinite"/></circle>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="16" fill="none" stroke="{col}" stroke-width="1.2" opacity="0.5"/>')
        dy = -26 if ang > 90 else -26
        anchor = "end" if ang > 90 else "start"
        lx = x + (-14 if ang > 90 else 14)
        parts.append(f'<text x="{lx:.1f}" y="{y-6:.1f}" text-anchor="{anchor}" font-family="Cormorant Garamond,Georgia,serif" font-size="15" font-weight="600" fill="{col}">{nm}</text>')
        parts.append(f'<text x="{lx:.1f}" y="{y+8:.1f}" text-anchor="{anchor}" font-family="Space Mono,monospace" font-size="8.5" fill="#b9a987">{yl}</text>')
    # empty seats waiting in the tiers (faint dots)
    import random
    seedpts = [(150,150),(30,160),(140,200),(40,210),(120,250),(60,260),(95,300),(135,300),(55,300)]
    for ang, r in seedpts:
        x = cx + r*math.cos(math.radians(ang)); y = cy - r*math.sin(math.radians(ang))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#b9a987" opacity="0.28"/>')
    return f'<svg viewBox="0 0 800 470" width="100%" role="img" aria-label="a Greek amphitheater, the two first philosophers seated in the front row">{"".join(parts)}</svg>'

# ── html helpers ──
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)

def seats_html():
    by_year = sorted(SEATS, key=lambda s: s[5])
    out=[]
    for slug,name,sex,epithet,em,yr_i,yr,loc,role,why in by_year:
        col = NATURES.get(em,("#c4a45a",""))[0]
        rec = {"name":name,"seal":epithet,"origin":"AMP · The Greek Mirror","axiom":"AMP"}
        sym = "♀" if sex=="female" else "♂"
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
    return "".join(out)

def roadmap_html():
    rows=[]
    for name,yr,loc,note in ROADMAP:
        rows.append(f'<li><span class="rn">{html.escape(name)}</span><span class="ry">{html.escape(yr)}</span>'
                    f'<span class="rl">{html.escape(loc)}</span><span class="rt">{html.escape(note)}</span></li>')
    return "".join(rows)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE GREEK MIRROR (AMP) — the Amphitheater of the World's Philosophers, seated by year and location. It opens in deep time: the first author known by name was a woman, Enheduanna of Ur (c. 2285 BCE); the first man by the elder date, Ptahhotep of Memphis. Catalogued into UD0 with full ACI badges.">
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
.theater{margin:26px auto 0;max-width:760px;padding:8px}
.firstline{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin:14px 0 0}
.fcard{flex:1;min-width:240px;border:1px solid var(--faint);background:var(--ink2);padding:13px 16px}
.fcard.f{border-top:2px solid var(--gold)} .fcard.m{border-top:2px solid var(--blue)}
.fcard .ft{font-family:var(--mono);font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
.fcard .fn{font-family:var(--serif);font-size:22px;font-weight:700;margin-top:3px}
.fcard.f .fn{color:var(--gold)} .fcard.m .fn{color:var(--blue)}
.fcard .fs{font-family:var(--mono);font-size:10px;color:var(--pa2);margin-top:4px}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
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
.seat{display:flex;gap:16px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:16px 18px;margin-top:14px}
.seat img{width:84px;height:84px;border:1px solid var(--faint);flex-shrink:0}
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
    <div class="h-sub">the amphitheater of the world's philosophers · <b>a man &amp; a woman through time</b> · AMP</div>
    <div class="flag">★ the front row was never Athens · the first voice was never his ★</div>
    <p class="lede">A Greek amphitheater, turned into a mirror of the whole world. Aristotle named Thales the first philosopher — but the mirror looks past Ionia and finds, seventeen centuries earlier, the first author known by name in all of history: a woman of Ur. The theater opens in deep time with its two firsts, and the Greek stage and the canon will fill the rising tiers, each seat stamped by its year and place.</p>
    <div class="theater">__THEATER__</div>
    <div class="firstline">
      <div class="fcard f"><div class="ft">♀ the first — female</div><div class="fn">Enheduanna</div><div class="fs">c. 2285 BCE · Ur, Sumer · first author known by name</div></div>
      <div class="fcard m"><div class="ft">♂ the first — male</div><div class="fn">Ptahhotep</div><div class="fs">c. 2375 BCE · Memphis, Egypt · the Maxims</div></div>
    </div>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE GREEK MIRROR" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge of THE GREEK MIRROR" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE AMPHITHEATER OPENED</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE GREEK MIRROR</b> — the amphitheater of philosophers · AMP</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="the-greek-mirror.dlw/the-greek-mirror.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="the-greek-mirror.dlw/the-greek-mirror.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Two Firsts</h2><p class="ss">the deep-time prologue — seated oldest-first by year and location</p>__SEATS__</section>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each seat emerges by one of four natures — electrical waits, reserved for the modern minds to come</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Stage Ahead</h2><p class="ss">named, not yet seated — the next to take the rising tiers (render-not-invent: no badge until catalogued)</p>
    <ol class="road">__ROADMAP__</ol></section>

  <div class="note"><b>The mirror's honesty.</b> The amphitheater is a Greek form, but "world's greatest philosophers" means the world — so the first seats are pre-Greek, and the very first is a woman. Two seams are flagged, not hidden: (1) <b>dating</b> — Ptahhotep's dramatic date (~2375 BCE) is older than Enheduanna's (~2285 BCE), yet his Maxims survive only in much later copies while Enheduanna is the first author <em>known by name</em>, so each holds a different kind of "first"; (2) <b>the word "philosopher"</b> — at this depth it means sage of wisdom-literature (Ptahhotep) and priest-poet who reasons about the divine (Enheduanna), stretched from its later Greek sense of reasoned argument from first principles. The Greek stage (Thales, Theano…) opens that narrower sense. Rendered, not invented; figures are historical and © no one — this is a catalogue under the DLW standard, not an original work. Each seat is named by its nature of emergence: natural, ethereal, spiritual, or (later) electrical.</div>

  <footer>
    THE GREEK MIRROR · AMP · the amphitheater of philosophers · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="the-greek-mirror.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "the-greek-mirror.dlw"), "the-greek-mirror")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,sex,epithet,em,yr_i,yr,loc,role,why in SEATS:
        rec = seat_rec(name, epithet, em, loc, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "sex": sex, "year": yr, "location": loc})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__THEATER__", amphitheater_svg())
            .replace("__SEATS__", seats_html())
            .replace("__NATURES__", natures_html())
            .replace("__ROADMAP__", roadmap_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE GREEK MIRROR (AMP) — {len(personas)} seated ({', '.join(p['name'] for p in personas)}) · badge {tok['moniker']}")

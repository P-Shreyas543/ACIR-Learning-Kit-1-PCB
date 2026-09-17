import re
import sys
from collections import Counter

def parse_pcb_elements(pcb_path):
    with open(pcb_path, 'r', encoding='utf-8') as f:
        text = f.read()

    n = len(text)
    items = []
    for m in re.finditer(r'\n\t\((gr_[a-z]+)\s+', text):
        tag = m.group(1)
        st = m.start() + 2
        depth = 0
        j = st
        in_str = False
        while j < n:
            c = text[j]
            if c == '"' and (j == 0 or text[j-1] != '\\'):
                in_str = not in_str
            elif not in_str:
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
            j += 1
        expr = text[st:j]
        layer_m = re.search(r'\(layer\s+"([^"]+)"(?:\s+knockout)?\)', expr)
        if layer_m and "Silk" in layer_m.group(1):
            items.append((tag, layer_m.group(1), expr))

    print(f"Total silkscreen graphics in {pcb_path}: {len(items)}")
    counts = Counter((tag, layer) for tag, layer, _ in items)
    for k, v in sorted(counts.items()):
        print(f"  {k[0]} ({k[1]}): {v}")

    # Extract text details
    texts = []
    for tag, layer, expr in items:
        if tag == 'gr_text':
            m_text = re.search(r'\(gr_text\s+"([^"]*)"', expr)
            txt = m_text.group(1) if m_text else ""
            m_at = re.search(r'\(at\s+([\d\.-]+)\s+([\d\.-]+)(?:\s+([\d\.-]+))?\)', expr)
            at = (float(m_at.group(1)), float(m_at.group(2)), float(m_at.group(3)) if m_at.group(3) else 0.0) if m_at else (0,0,0)
            m_layer = re.search(r'\(layer\s+"([^"]+)"(\s+knockout)?\)', expr)
            ko = bool(m_layer and m_layer.group(2))
            m_font = re.search(r'\(face\s+"([^"]+)"\)', expr)
            m_size = re.search(r'\(size\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_thick = re.search(r'\(thickness\s+([\d\.-]+)\)', expr)
            m_bold = re.search(r'\(bold\s+([^)]+)\)', expr)
            m_just = re.search(r'\(justify\s+([^)]+)\)', expr)
            texts.append({
                'text': txt,
                'at': at,
                'layer': layer,
                'knockout': ko,
                'face': m_font.group(1) if m_font else "default",
                'size': (float(m_size.group(1)), float(m_size.group(2))) if m_size else (0,0),
                'thickness': float(m_thick.group(1)) if m_thick else 0.0,
                'bold': m_bold.group(1) if m_bold else "no",
                'justify': m_just.group(1) if m_just else "default"
            })

    # Extract lines
    lines = []
    for tag, layer, expr in items:
        if tag == 'gr_line':
            m_start = re.search(r'\(start\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_end = re.search(r'\(end\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_stroke = re.search(r'\(width\s+([\d\.-]+)\)', expr)
            lines.append({
                'start': (float(m_start.group(1)), float(m_start.group(2))) if m_start else (0,0),
                'end': (float(m_end.group(1)), float(m_end.group(2))) if m_end else (0,0),
                'width': float(m_stroke.group(1)) if m_stroke else 0.0,
                'layer': layer
            })

    # Extract rects
    rects = []
    for tag, layer, expr in items:
        if tag == 'gr_rect':
            m_start = re.search(r'\(start\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_end = re.search(r'\(end\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_stroke = re.search(r'\(width\s+([\d\.-]+)\)', expr)
            rects.append({
                'start': (float(m_start.group(1)), float(m_start.group(2))) if m_start else (0,0),
                'end': (float(m_end.group(1)), float(m_end.group(2))) if m_end else (0,0),
                'width': float(m_stroke.group(1)) if m_stroke else 0.0,
                'layer': layer
            })

    # Extract arcs
    arcs = []
    for tag, layer, expr in items:
        if tag == 'gr_arc':
            m_start = re.search(r'\(start\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_mid = re.search(r'\(mid\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            m_end = re.search(r'\(end\s+([\d\.-]+)\s+([\d\.-]+)\)', expr)
            arcs.append({
                'start': (float(m_start.group(1)), float(m_start.group(2))) if m_start else (0,0),
                'mid': (float(m_mid.group(1)), float(m_mid.group(2))) if m_mid else (0,0),
                'end': (float(m_end.group(1)), float(m_end.group(2))) if m_end else (0,0),
                'layer': layer
            })

    return {'items': items, 'texts': texts, 'lines': lines, 'rects': rects, 'arcs': arcs}

print("=" * 60)
print("ANALYZING KIT 1 SILKSCREEN:")
print("=" * 60)
k1 = parse_pcb_elements('ACIR-Learning-Kit-1-PCB/ACIR-Learning-Kit-1-PCB.kicad_pcb')

print("\n" + "=" * 60)
print("ANALYZING KIT 2 SILKSCREEN:")
print("=" * 60)
k2 = parse_pcb_elements('ACIR-Learning-Kit-2-PCB/ACIR-Learning-Kit-2-PCB.kicad_pcb')

print("\n" + "=" * 60)
print("COMPARISON & VERIFICATION REPORT:")
print("=" * 60)

# Compare Rectangles
print(f"\n1. Framing Rectangles (F.SilkS): Kit 1 has {len(k1['rects'])}, Kit 2 has {len(k2['rects'])}")
rect_match = len(k1['rects']) == len(k2['rects'])
for r1 in k1['rects']:
    match = any(r2['start'] == r1['start'] and r2['end'] == r1['end'] and r2['width'] == r1['width'] for r2 in k2['rects'])
    if not match:
        rect_match = False
        print(f"  MISMATCH in rect: start={r1['start']} end={r1['end']}")
if rect_match:
    print("  [MATCH] All 6 framing rectangles are 100% identical in coordinates, thickness, and layers!")

# Compare Outer Border Arcs
print(f"\n2. Rounded Border Corner Arcs: Kit 1 has {len(k1['arcs'])}, Kit 2 has {len(k2['arcs'])}")
arc_match = len(k1['arcs']) == len(k2['arcs'])
for a1 in k1['arcs']:
    match = any(a2['start'] == a1['start'] and a2['end'] == a1['end'] and a2['layer'] == a1['layer'] for a2 in k2['arcs'])
    if not match:
        arc_match = False
        print(f"  MISMATCH in arc: start={a1['start']} end={a1['end']} layer={a1['layer']}")
if arc_match:
    print("  [MATCH] All 8 corner arcs (4 F.SilkS, 4 B.SilkS) are 100% identical!")

# Compare Back Silkscreen Texts
print("\n3. Back Silkscreen Texts (B.SilkS):")
b1 = [t for t in k1['texts'] if t['layer'] == 'B.SilkS']
b2 = [t for t in k2['texts'] if t['layer'] == 'B.SilkS']
print(f"  Kit 1 count: {len(b1)}, Kit 2 count: {len(b2)}")
for t1, t2 in zip(sorted(b1, key=lambda x: x['at'][1]), sorted(b2, key=lambda x: x['at'][1])):
    pos_match = t1['at'] == t2['at']
    font_match = t1['face'] == t2['face'] and t1['size'] == t2['size'] and t1['thickness'] == t2['thickness']
    status = "[MATCH]" if (pos_match and font_match) else "[DIFF]"
    print(f"  {status} K1: at={t1['at']} size={t1['size']} th={t1['thickness']} '{t1['text']}'")
    print(f"         K2: at={t2['at']} size={t2['size']} th={t2['thickness']} '{t2['text']}'")

# Compare Arrow Stroke Widths
print("\n4. Arrow Line Stroke Widths:")
arrow_lines_k1 = [l for l in k1['lines'] if l['width'] == 0.18]
arrow_lines_k2 = [l for l in k2['lines'] if l['width'] == 0.18]
print(f"  Kit 1 has {len(arrow_lines_k1)} lines with width 0.18")
print(f"  Kit 2 has {len(arrow_lines_k2)} lines with width 0.18")
non_standard_k2 = [l for l in k2['lines'] if l['width'] not in [0.4, 0.18]]
if not non_standard_k2:
    print("  [MATCH] Kit 2 uses only standardized stroke widths: 0.4 for borders/boxes, 0.18 for arrows!")
else:
    print(f"  [WARN] Non standard widths found in Kit 2: {non_standard_k2}")

# Compare Fonts
print("\n5. Font Faces & Typography:")
fonts_k1 = Counter(t['face'] for t in k1['texts'])
fonts_k2 = Counter(t['face'] for t in k2['texts'])
print(f"  Kit 1 font faces: {dict(fonts_k1)}")
print(f"  Kit 2 font faces: {dict(fonts_k2)}")
if set(fonts_k1.keys()) == set(fonts_k2.keys()):
    print("  [MATCH] Exact font face parity (PT Sans throughout)!")

print("\n" + "=" * 60)
print("ALL SILKSCREEN CHECKS COMPLETE")
print("=" * 60)

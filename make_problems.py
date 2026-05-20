import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

BG    = '#0a0a0f'
CARD  = '#12121a'
BLUE  = '#3b82f6'
CYAN  = '#06b6d4'
WHITE = '#f1f5f9'
GRAY  = '#9ca3af'
YELLOW= '#fbbf24'
GREEN = '#22c55e'
RED   = '#ef4444'
PURPL = '#a855f7'

def base(letter, title_mn, title_en):
    fig = plt.figure(figsize=(13, 9))
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    ax.set_facecolor(CARD)
    ax.set_xlim(0, 13); ax.set_ylim(0, 9)
    ax.axis('off')

    # outer border
    ax.add_patch(patches.FancyBboxPatch(
        (0.1,0.1), 12.8, 8.8, lw=2, edgecolor=BLUE,
        facecolor='none', boxstyle='round,pad=0.05'))

    # header
    ax.add_patch(patches.Rectangle((0.1,7.45), 12.8, 1.45, facecolor='#0d1835', edgecolor='none'))
    ax.plot([0.1,12.9],[7.45,7.45], color=BLUE, lw=1.2)

    # letter badge
    ax.add_patch(plt.Circle((0.95, 8.2), 0.55, color=BLUE))
    ax.text(0.95, 8.2, letter, ha='center', va='center',
            fontsize=22, fontweight='bold', color='white', fontfamily='monospace')

    ax.text(1.75, 8.58, title_mn, fontsize=15, fontweight='bold', color=CYAN)
    ax.text(1.75, 7.72, title_en, fontsize=10, color=GRAY, fontstyle='italic')

    # points badge
    ax.add_patch(patches.FancyBboxPatch(
        (10.8,7.6), 1.9, 0.85, facecolor='#14532d',
        edgecolor=GREEN, lw=1.2, boxstyle='round,pad=0.05'))
    ax.text(11.75, 8.02, '100 оноо', ha='center', va='center',
            fontsize=11, fontweight='bold', color=GREEN)

    # answer box
    ax.add_patch(patches.FancyBboxPatch(
        (0.3,0.22), 12.4, 0.88, facecolor='#0d1f12',
        edgecolor=GREEN, lw=1, boxstyle='round,pad=0.05', linestyle='--'))
    ax.text(0.65, 0.66, 'Хариу / Answer:', fontsize=10,
            color=GREEN, fontweight='bold', va='center')
    ax.plot([3.0,12.5],[0.66,0.66], color='#374151', lw=0.8, linestyle=':')

    ax.text(6.5, 0.08,
            'ICPC Math Contest  •  Хэв Таних / Pattern Recognition  •  2025',
            ha='center', fontsize=7.5, color='#4b5563')
    return fig, ax


# ═══════════════════════════════════════════════════
# Problem A — Fibonacci дараалал
# ═══════════════════════════════════════════════════
fig, ax = base('A', 'Дараалал таних', 'Sequence Recognition')

ax.text(0.55, 7.1, 'Дараах тоон дараалал дахь ??? утгыг ол:', fontsize=12, color='#d1d5db')

ax.add_patch(patches.FancyBboxPatch(
    (0.5,5.55), 12,1.25, facecolor='#1e3a5f', edgecolor='#1d4ed8', lw=1.5, boxstyle='round,pad=0.1'))
ax.text(6.5, 6.17, '1 ,  1 ,  2 ,  3 ,  5 ,  8 ,  13 ,  21 ,  ???',
        ha='center', va='center', fontsize=22, color=YELLOW,
        fontweight='bold', fontfamily='monospace')

ax.text(0.55, 5.1, '• Хэрхэн үүссэн дүрмийг тодорхойл', fontsize=11, color=GRAY)
ax.text(0.55, 4.6, '• Дараагийн утгыг тооцоол', fontsize=11, color=GRAY)
ax.text(0.55, 3.85,
        'Санамж:  Aₙ = Aₙ₋₁ + Aₙ₋₂   (өмнөх хоёр тооны нийлбэр)',
        fontsize=11, color='#818cf8', fontstyle='italic')

ax.text(0.55, 3.0, 'Find the missing number in the sequence above.', fontsize=10, color='#6b7280')

plt.savefig('/home/enkhbileg/Documents/hevtanilt/problem_A.png',
            dpi=150, bbox_inches='tight', facecolor=BG, pad_inches=0.05)
plt.close()
print('✅  problem_A.png')


# ═══════════════════════════════════════════════════
# Problem B — Матриц тодорхойлогч
# ═══════════════════════════════════════════════════
fig, ax = base('B', 'Матриц — Тодорхойлогч', 'Matrix Determinant')

ax.text(0.55, 7.1, 'Дараах 2×2 матрицын тодорхойлогчийг (determinant) тооцоол:', fontsize=12, color='#d1d5db')

ax.add_patch(patches.FancyBboxPatch(
    (2.5,4.4), 8,2.7, facecolor='#1e3a5f', edgecolor='#1d4ed8', lw=1.5, boxstyle='round,pad=0.1'))

# Brackets
for xs, xe in [([3.1,2.8,2.8,3.1],[6.8,6.8,4.7,4.7]),
               ([9.9,10.2,10.2,9.9],[6.8,6.8,4.7,4.7])]:
    ax.plot(xs, xe, color=WHITE, lw=3)

for x,y,v in [(5.1,6.3,'4'),(7.4,6.3,'7'),
              (5.1,5.1,'2'),(7.4,5.1,'6')]:
    ax.text(x, y, v, ha='center', va='center',
            fontsize=38, color=YELLOW, fontweight='bold', fontfamily='monospace')

ax.text(0.55, 4.1, '• Томъёо:  det(A) = a·d − b·c', fontsize=12, color=GRAY)
ax.text(0.55, 3.55,
        '        |a  b|',
        fontsize=12, color='#94a3b8', fontfamily='monospace')
ax.text(0.55, 3.05,
        '  A =   |    |   →   det(A) = ad − bc',
        fontsize=12, color='#94a3b8', fontfamily='monospace')
ax.text(0.55, 2.55,
        '        |c  d|',
        fontsize=12, color='#94a3b8', fontfamily='monospace')

plt.savefig('/home/enkhbileg/Documents/hevtanilt/problem_B.png',
            dpi=150, bbox_inches='tight', facecolor=BG, pad_inches=0.05)
plt.close()
print('✅  problem_B.png')


# ═══════════════════════════════════════════════════
# Problem C — Зургийн дундаж фильтр (Convolution)
# ═══════════════════════════════════════════════════
fig, ax = base('C', 'Зургийн фильтр', 'Image Averaging Filter')

ax.text(0.55, 7.1, '3×3 дундаж фильтр хэрэглэхэд гол пикселийн шинэ утга хэд вэ?', fontsize=12, color='#d1d5db')

img = [[0, 3, 6],
       [3, 6, 9],
       [6, 9, 3]]

cell_w, cell_h = 1.4, 1.1
ox, oy = 1.0, 5.8

for r in range(3):
    for c in range(3):
        is_center = (r==1 and c==1)
        fc = '#1e3a5f' if not is_center else '#7c2d12'
        ec = '#1d4ed8' if not is_center else '#f97316'
        ax.add_patch(patches.FancyBboxPatch(
            (ox + c*cell_w, oy - r*cell_h), cell_w-0.05, cell_h-0.05,
            facecolor=fc, edgecolor=ec, lw=1.5, boxstyle='round,pad=0.05'))
        ax.text(ox + c*cell_w + cell_w/2 - 0.03,
                oy - r*cell_h + cell_h/2 - 0.03,
                str(img[r][c]), ha='center', va='center',
                fontsize=20, color=YELLOW if not is_center else '#fb923c',
                fontweight='bold', fontfamily='monospace')

ax.text(5.8, 5.3, '← Зургийн матриц\n   (гол = улаанаар)', fontsize=10, color=GRAY)
ax.text(5.8, 4.3,
        'Дундаж фильтр:\n'
        '  бүх 9 пикселийн нийлбэрийг\n'
        '  9-д хувааж гол утгыг олно',
        fontsize=11, color='#d1d5db', linespacing=1.6)

total = sum(img[r][c] for r in range(3) for c in range(3))
ax.text(0.55, 2.55,
        f'Нийлбэр = {" + ".join(str(img[r][c]) for r in range(3) for c in range(3))} = {total}',
        fontsize=11, color='#818cf8', fontfamily='monospace')
ax.text(0.55, 2.05,
        f'Шинэ утга = {total} ÷ 9 = ???',
        fontsize=12, color='#c084fc', fontweight='bold', fontfamily='monospace')

plt.savefig('/home/enkhbileg/Documents/hevtanilt/problem_C.png',
            dpi=150, bbox_inches='tight', facecolor=BG, pad_inches=0.05)
plt.close()
print('✅  problem_C.png')


# ═══════════════════════════════════════════════════
# Problem D — Пикселийн Manhattan зай
# ═══════════════════════════════════════════════════
fig, ax = base('D', 'Пикселийн зай', 'Pixel Manhattan Distance')

ax.text(0.55, 7.1, 'Хоёр пикселийн хооронд Manhattan Distance тооцоол:', fontsize=12, color='#d1d5db')

# Pixel boxes
for px, label, vals, cx in [
    (1.0, 'Пиксел 1', (255, 128, 64), '#e11d48'),
    (7.5, 'Пиксел 2', (200,  80,  14), '#9333ea'),
]:
    r, g, b = vals
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    ax.add_patch(patches.FancyBboxPatch(
        (px, 4.8), 4.8, 2.3, facecolor=color_hex, edgecolor=WHITE, lw=1.5,
        boxstyle='round,pad=0.1', alpha=0.9))
    ax.text(px+2.4, 6.7, label, ha='center', fontsize=11, color=WHITE, fontweight='bold')
    ax.text(px+2.4, 6.1, f'R={r}   G={g}   B={b}', ha='center',
            fontsize=13, color=WHITE, fontweight='bold', fontfamily='monospace')

ax.text(6.25, 5.95, '↔', ha='center', va='center', fontsize=28, color=CYAN)

ax.text(0.55, 4.4, 'Томъёо:  D = |R₁−R₂| + |G₁−G₂| + |B₁−B₂|',
        fontsize=12, color=GRAY)
ax.text(0.55, 3.75,
        '       D = |255−200| + |128−80| + |64−14|',
        fontsize=12, color='#818cf8', fontfamily='monospace')
ax.text(0.55, 3.15,
        '       D = ??? + ??? + ??? = ???',
        fontsize=13, color=YELLOW, fontweight='bold', fontfamily='monospace')

plt.savefig('/home/enkhbileg/Documents/hevtanilt/problem_D.png',
            dpi=150, bbox_inches='tight', facecolor=BG, pad_inches=0.05)
plt.close()
print('✅  problem_D.png')


# ═══════════════════════════════════════════════════
# Problem E — Binary grid connected components
# ═══════════════════════════════════════════════════
fig, ax = base('E', 'Холбогдсон бүлэг', 'Connected Components')

ax.text(0.55, 7.1,
        'Дараах binary зурагт 4-зэргэлдээ (дээш/доош/зүүн/баруун) ашиглан\n'
        'хэдэн тусдаа бүлэг (connected component) байгааг тоол:',
        fontsize=11.5, color='#d1d5db', linespacing=1.6)

grid = [
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,1,0],
    [0,0,1,1,0],
]

ox, oy = 2.0, 6.6
cw, ch = 1.3, 1.0

for r in range(5):
    for c in range(5):
        v = grid[r][c]
        fc = '#16a34a' if v==1 else '#1f2937'
        ec = '#22c55e' if v==1 else '#374151'
        ax.add_patch(patches.FancyBboxPatch(
            (ox+c*cw, oy-r*ch), cw-0.06, ch-0.06,
            facecolor=fc, edgecolor=ec, lw=1.2, boxstyle='round,pad=0.04'))
        ax.text(ox+c*cw+cw/2-0.03, oy-r*ch+ch/2-0.03,
                str(v), ha='center', va='center',
                fontsize=17, color=WHITE if v==1 else '#4b5563',
                fontweight='bold', fontfamily='monospace')

ax.text(8.7, 6.25, '• 1 = идэвхтэй пиксел', fontsize=11, color=GREEN)
ax.text(8.7, 5.75, '• 0 = хоосон пиксел', fontsize=11, color='#6b7280')
ax.text(8.7, 5.1, '• Хэдэн тусдаа\n  бүлэг байна вэ?', fontsize=12, color=WHITE, linespacing=1.6)

ax.text(0.55, 1.75,
        '4-зэргэлдээ: дээш ↑  доош ↓  зүүн ←  баруун →  (диагональ биш!)',
        fontsize=10, color='#6366f1', fontstyle='italic')

plt.savefig('/home/enkhbileg/Documents/hevtanilt/problem_E.png',
            dpi=150, bbox_inches='tight', facecolor=BG, pad_inches=0.05)
plt.close()
print('✅  problem_E.png')

print('\n🎉 Бүх 5 даалгавар амжилттай үүслээ!')
print('Файлууд: problem_A.png ~ problem_E.png')

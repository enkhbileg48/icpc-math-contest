import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BG    = '#0a0a0f'
CARD  = '#12121a'
BLUE  = '#3b82f6'
CYAN  = '#06b6d4'
WHITE = '#f1f5f9'
GRAY  = '#9ca3af'
GREEN = '#22c55e'
PURPLE= '#a855f7'

OPT_STYLE = {
    'A': ('#0d2144', '#3b82f6'),
    'B': ('#0d2e1a', '#22c55e'),
    'C': ('#2e0d0d', '#ef4444'),
    'D': ('#1e0d2e', '#a855f7'),
}

QUESTIONS = [
    # ── Pixel math ──────────────────────────────────────────────────
    dict(
        num=1, topic='Grayscale хөрвүүлэлт',
        q=['RGB пиксел (R=180, G=60, B=120)-г grayscale болгоход утга хэд вэ?'],
        formula=[
            'Gray = (R + G + B) / 3',
            'Gray = (180 + 60 + 120) / 3 = ???',
        ],
        opts=[('A','100'), ('B','120'), ('C','140'), ('D','160')],
        ans='B',
    ),
    dict(
        num=2, topic='Гэрэлтэлт нэмэх',
        q=['Пикселийн утга 100, гэрэл 80-аар нэмэгдвэл шинэ утга хэд вэ? (max=255)'],
        formula=[
            'new_pixel = min(pixel + k,  255)',
            'new_pixel = min(100 + 80,   255) = ???',
        ],
        opts=[('A','80'), ('B','100'), ('C','180'), ('D','255')],
        ans='C',
    ),
    dict(
        num=3, topic='Пикселийн сөрөг',
        q=['8-bit зурагт пикселийн утга 60 байхад complement (сөрөг) утга хэд вэ?'],
        formula=[
            'complement = 255 - pixel',
            'complement = 255 - 60 = ???',
        ],
        opts=[('A','60'), ('B','128'), ('C','195'), ('D','200')],
        ans='C',
    ),
    dict(
        num=4, topic='Контраст өөрчлөх',
        q=['Пикселийн утга 100-г 1.5 дахин нэмэгдүүлбэл шинэ утга хэд вэ?'],
        formula=[
            'new_pixel = pixel × scale',
            'new_pixel = 100 × 1.5 = ???',
        ],
        opts=[('A','100'), ('B','150'), ('C','200'), ('D','250')],
        ans='B',
    ),
    dict(
        num=5, topic='Нормалчлал [0,1]',
        q=['Пикселийн утга 204-г [0, 1] мужид нормалчлахад утга хэд вэ?'],
        formula=[
            'normalized = pixel / 255',
            'normalized = 204 / 255 = ???',
        ],
        opts=[('A','0.60'), ('B','0.75'), ('C','0.80'), ('D','1.00')],
        ans='C',
    ),
    # ── Filtering ────────────────────────────────────────────────────
    dict(
        num=6, topic='Дундаж фильтр',
        q=['3×3 дундаж фильтр хэрэглэхэд гол пикселийн шинэ утга хэд вэ?',
           'Матриц:  [4, 8, 4,  8, 16, 8,  4, 8, 4]'],
        formula=[
            'avg = sum(бүх 9 утга) / 9',
            'avg = (4+8+4+8+16+8+4+8+4) / 9 = 64 / 9 ≈ ???',
        ],
        opts=[('A','5'), ('B','7'), ('C','8'), ('D','9')],
        ans='B',
    ),
    dict(
        num=7, topic='Median фильтр',
        q=['Дараах 9 пикселийн median (дундаж) утгыг ол:',
           'Утгууд:  [3, 1, 4, 1, 5, 9, 2, 6, 5]'],
        formula=[
            'Алхам 1: Эрэмбэл →  [1, 1, 2, 3, 4, 5, 5, 6, 9]',
            'Алхам 2: Дунд байрны утгыг ав (5-р байр) = ???',
        ],
        opts=[('A','3'), ('B','4'), ('C','5'), ('D','6')],
        ans='B',
    ),
    dict(
        num=8, topic='Gaussian blur',
        q=['Gaussian blur filter-ийн гол зорилго юу вэ?'],
        formula=[
            'G(x,y) = (1/2πσ²) × e^(-(x²+y²)/2σ²)',
            'Энэ функц зургийн утгуудыг жигдлэн холино.',
        ],
        opts=[('A','Дуу чимээ арилгах'), ('B','Ирмэг илрүүлэх'),
              ('C','Өнгө өөрчлөх'),    ('D','Зураг томруулах')],
        ans='A',
    ),
    dict(
        num=9, topic='Identity kernel',
        q=['[[0,0,0],[0,1,0],[0,0,0]] kernel-г зурагт хэрэглэхэд юу болох вэ?'],
        formula=[
            'Convolution:  output = Σ(kernel × patch)',
            'Гол утга 1, бусад 0 → зөвхөн гол пиксел хадгалагдана.',
        ],
        opts=[('A','Тэг зураг'),      ('B','Өөрчлөгдөхгүй'),
              ('C','Blur болно'),     ('D','Ирмэг гарна')],
        ans='B',
    ),
    # ── Distance & geometry ──────────────────────────────────────────
    dict(
        num=10, topic='Euclidean зай',
        q=['A(0,0) ба B(5,12) цэгүүдийн хоорондох Euclidean зайг ол.'],
        formula=[
            'd = √( (x₂-x₁)² + (y₂-y₁)² )',
            'd = √( 5² + 12² ) = √( 25 + 144 ) = √169 = ???',
        ],
        opts=[('A','7'), ('B','12'), ('C','13'), ('D','17')],
        ans='C',
    ),
    dict(
        num=11, topic='Manhattan зай',
        q=['P₁(2,3) ба P₂(6,7) хоорондын Manhattan зайг тооцоол.'],
        formula=[
            'd = |x₁-x₂| + |y₁-y₂|',
            'd = |2-6|  +  |3-7|  =  4 + 4  =  ???',
        ],
        opts=[('A','4'), ('B','6'), ('C','8'), ('D','10')],
        ans='C',
    ),
    dict(
        num=12, topic='Зургийн нийт пиксел',
        q=['1920×1080 хэмжээтэй зурагт нийт хэдэн пиксел байна вэ?'],
        formula=[
            'Нийт пиксел = өргөн × өндөр',
            'Нийт пиксел = 1920 × 1080 = ???',
        ],
        opts=[('A','3,000'), ('B','1,036,800'), ('C','2,073,600'), ('D','4,147,200')],
        ans='C',
    ),
    # ── Threshold & binary ───────────────────────────────────────────
    dict(
        num=13, topic='Binary threshold',
        q=['Пикселийн утга 90, threshold=128. Binary thresholding хийхэд?'],
        formula=[
            'if pixel > threshold  →  255  (цагаан)',
            'if pixel ≤ threshold  →    0  (хар)',
            '90 ≤ 128  →  ???',
        ],
        opts=[('A','0'), ('B','90'), ('C','128'), ('D','255')],
        ans='A',
    ),
    dict(
        num=14, topic='Өнгийн bit гүн',
        q=['RGB 24-bit зургийн нэг пикселийг хадгалахад хэдэн бит хэрэгтэй вэ?'],
        formula=[
            'RGB = Red канал + Green канал + Blue канал',
            'Нийт бит = 3 канал × 8 бит = ???',
        ],
        opts=[('A','8 бит'), ('B','16 бит'), ('C','24 бит'), ('D','32 бит')],
        ans='C',
    ),
    dict(
        num=15, topic='Зургийн хадгалах хэмжээ',
        q=['100×100 пиксел, RGB 24-bit зургийг хадгалахад хэдэн байт хэрэгтэй вэ?'],
        formula=[
            'bytes = өргөн × өндөр × канал тоо',
            'bytes = 100  ×  100  ×  3  =  ???',
        ],
        opts=[('A','10,000'), ('B','30,000'), ('C','100,000'), ('D','300,000')],
        ans='B',
    ),
]

# ════════════════════════════════════════════════════════════════════
def draw_mcq(q, path):
    fig = plt.figure(figsize=(13, 9.5))
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    ax.set_facecolor(CARD)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # outer border
    ax.add_patch(patches.FancyBboxPatch(
        (0.1, 0.1), 12.8, 9.3, lw=2, edgecolor=BLUE,
        facecolor='none', boxstyle='round,pad=0.05'))

    # header strip
    ax.add_patch(patches.Rectangle(
        (0.1, 7.95), 12.8, 1.45, facecolor='#0d1835', edgecolor='none'))
    ax.plot([0.1, 12.9], [7.95, 7.95], color=BLUE, lw=1.2)

    # number badge
    ax.add_patch(plt.Circle((0.92, 8.68), 0.55, color=BLUE))
    ax.text(0.92, 8.68, str(q['num']), ha='center', va='center',
            fontsize=20, fontweight='bold', color='white', fontfamily='monospace')

    ax.text(1.72, 9.05, q['topic'], fontsize=15, fontweight='bold', color=CYAN)
    ax.text(1.72, 8.22, 'Хэв Таних / Pattern Recognition  •  Computer Vision',
            fontsize=9, color=GRAY, fontstyle='italic')

    # points
    ax.add_patch(patches.FancyBboxPatch(
        (10.9, 8.05), 1.85, 0.82, facecolor='#14532d',
        edgecolor=GREEN, lw=1.2, boxstyle='round,pad=0.05'))
    ax.text(11.82, 8.46, '1 оноо', ha='center', va='center',
            fontsize=11, fontweight='bold', color=GREEN)

    # question text
    y = 7.6
    for line in q['q']:
        ax.text(0.55, y, line, fontsize=12, color=WHITE, va='top')
        y -= 0.52

    y -= 0.1

    # formula box
    fh = len(q['formula']) * 0.48 + 0.32
    ax.add_patch(patches.FancyBboxPatch(
        (0.4, y - fh), 12.2, fh, facecolor='#12122a',
        edgecolor='#4338ca', lw=1.2, boxstyle='round,pad=0.08'))
    ax.text(0.65, y - 0.22, '📐 Томъёо / Formula', fontsize=9,
            color='#6366f1', va='top', fontweight='bold')
    fy = y - 0.55
    for fl in q['formula']:
        ax.text(0.72, fy, fl, fontsize=11, color='#a5b4fc',
                va='top', fontfamily='monospace')
        fy -= 0.46

    y = y - fh - 0.35

    # 4 options  (2×2 grid)
    ow, oh = 6.05, 1.25
    positions = [
        (0.40, y - oh),
        (6.55, y - oh),
        (0.40, y - 2*oh - 0.18),
        (6.55, y - 2*oh - 0.18),
    ]

    for i, (letter, text) in enumerate(q['opts']):
        ox, oy2 = positions[i]
        fc, ec = OPT_STYLE[letter]
        ax.add_patch(patches.FancyBboxPatch(
            (ox, oy2), ow - 0.08, oh - 0.06,
            facecolor=fc, edgecolor=ec, lw=1.8,
            boxstyle='round,pad=0.08'))
        ax.add_patch(plt.Circle((ox + 0.58, oy2 + oh/2 - 0.04), 0.40, color=ec, alpha=0.85))
        ax.text(ox + 0.58, oy2 + oh/2 - 0.04, letter,
                ha='center', va='center', fontsize=17,
                fontweight='bold', color=WHITE)
        fs = 13 if len(text) < 12 else 11
        ax.text(ox + 1.3, oy2 + oh/2 - 0.04, text,
                va='center', fontsize=fs,
                color=WHITE, fontweight='bold', fontfamily='monospace')

    # footer
    ax.text(6.5, 0.08,
            'ICPC Math Contest  •  Хэв Таних / Pattern Recognition  •  2025',
            ha='center', fontsize=7.5, color='#4b5563')

    plt.savefig(path, dpi=150, bbox_inches='tight',
                facecolor=BG, pad_inches=0.05)
    plt.close()
    print(f'✅  {path.split("/")[-1]}')


# ════════════════════════════════════════════════════════════════════
# Generate all 15 question images
# ════════════════════════════════════════════════════════════════════
import os
OUT = '/home/enkhbileg/Documents/hevtanilt/tests'
os.makedirs(OUT, exist_ok=True)

for q in QUESTIONS:
    draw_mcq(q, f'{OUT}/test_{q["num"]:02d}.png')

# ════════════════════════════════════════════════════════════════════
# Answer key image
# ════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(13, 9))
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
ax.set_facecolor(CARD)
ax.set_xlim(0, 13); ax.set_ylim(0, 9)
ax.axis('off')

ax.add_patch(patches.FancyBboxPatch(
    (0.1,0.1), 12.8, 8.8, lw=2, edgecolor='#ca8a04',
    facecolor='none', boxstyle='round,pad=0.05'))
ax.add_patch(patches.Rectangle(
    (0.1,7.5), 12.8, 1.4, facecolor='#1c1400', edgecolor='none'))
ax.plot([0.1,12.9],[7.5,7.5], color='#ca8a04', lw=1.2)

ax.text(0.7, 8.6, '🔑  Хариултын хуудас  /  ANSWER KEY',
        fontsize=18, fontweight='bold', color='#fbbf24')
ax.text(0.7, 7.75, 'Зөвхөн багш харна  —  For teacher only',
        fontsize=10, color=GRAY, fontstyle='italic')

cols = 3
per_col = 5
col_x = [0.8, 4.8, 8.8]

for i, q in enumerate(QUESTIONS):
    col = i // per_col
    row = i % per_col
    x = col_x[col]
    y = 7.0 - row * 1.25

    _, ec = OPT_STYLE[q['ans']]
    ax.add_patch(patches.FancyBboxPatch(
        (x, y-0.55), 3.6, 0.85, facecolor='#0d1835',
        edgecolor=ec, lw=1.5, boxstyle='round,pad=0.06'))

    ax.add_patch(plt.Circle((x+0.48, y-0.12), 0.36, color=BLUE, alpha=0.9))
    ax.text(x+0.48, y-0.12, str(q['num']), ha='center', va='center',
            fontsize=14, fontweight='bold', color=WHITE, fontfamily='monospace')

    ans_letter = q['ans']
    _, aec = OPT_STYLE[ans_letter]
    ax.add_patch(plt.Circle((x+1.15, y-0.12), 0.30, color=aec, alpha=0.9))
    ax.text(x+1.15, y-0.12, ans_letter, ha='center', va='center',
            fontsize=13, fontweight='bold', color=WHITE)

    ans_text = dict(q['opts'])[ans_letter]
    ax.text(x+1.65, y-0.12, ans_text, va='center',
            fontsize=10, color=WHITE, fontweight='bold', fontfamily='monospace')

ax.text(6.5, 0.08,
        'ICPC Math Contest  •  Хэв Таних / Pattern Recognition  •  2025',
        ha='center', fontsize=7.5, color='#4b5563')

plt.savefig(f'{OUT}/answer_key.png', dpi=150, bbox_inches='tight',
            facecolor=BG, pad_inches=0.05)
plt.close()
print(f'\n🔑  answer_key.png')
print(f'\n🎉  Нийт {len(QUESTIONS)} тест + 1 хариултын хуудас үүслээ!')
print(f'   Байршил: {OUT}/')

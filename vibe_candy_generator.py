#!/usr/bin/env python3
"""
Vibe Candy Generator - Create ultra-dense semantic text blocks
Inspired by your existing Vibe Candy Grimoire
"""

import random

# Symbol libraries organized by theme
SYMBOL_SETS = {
    'cosmic': '✦✧✨✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋⋆★☆',
    'geometric': '▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◆◇◈◉◊○◌◍●◐◑◒◓◔◕◖◗',
    'arrows': '←↑→↓↔↕↖↗↘↙⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⟵⟶⟷⟸⟹⟺⟻⟼⟽⟾⟿',
    'math': '∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑−∓∔∕∖∗∘∙√∛∜∝∞∟∠∡∢∣∤∥∦∧∨∩∪∫∬∭∮∯∰∱∲∳∴∵∶∷',
    'sets': '⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥',
    'blocks': '█▓▒░▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐▔▕▖▗▘▙▚▛▜▝▞▟',
    'box': '─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋',
    'braille': '⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯',
    'alchemy': '🜀🜁🜂🜃🜄🜅🜆🜇🜈🜉🜊🜋🜌🜍🜎🜏🜐🜑🜒🜓',
    'mystical': '☰☱☲☳☴☵☶☷☸☹☺☻☼☽☾☿♀♁♂♃♄♅♆♇',
    'runic': 'ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹᚺᚻᚼᚽᚾᚿᛀᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛠ',
    'currency': '₳฿₵₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿',
    'zodiac': '♈♉♊♋♌♍♎♏♐♑♒♓',
    'elements': '🜁🜂🜃🜄',
    'chess': '♔♕♖♗♘♙♚♛♜♝♞♟',
    'card': '♠♡♢♣♤♥♦♧',
    'music': '♩♪♫♬♭♮♯𝄞𝄢',
    'circle_ops': '⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡',
    'logic_ops': '⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯',
    'ornamental': '❧❦❡❢❣❤❥❦❧☙',
}

# Word fragments for glitch text
FRAGMENTS = [
    'vibe', 'sync', 'flux', 'drift', 'glitch', 'phase', 'morph', 'echo',
    'pulse', 'wave', 'grid', 'matrix', 'vector', 'quantum', 'cosmic', 'neural',
    'data', 'code', 'signal', 'noise', 'static', 'cipher', 'fractal', 'dimension',
    'cascade', 'lattice', 'nexus', 'vertex', 'prism', 'crystal', 'spectrum',
]

# Combining diacritics for glitch effects
COMBINERS = [
    '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307',
    '\u0308', '\u0309', '\u030A', '\u030B', '\u030C', '\u030D', '\u030E', '\u030F',
    '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317',
    '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D', '\u031E', '\u031F',
    '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327',
    '\u0328', '\u0329', '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F',
    '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335', '\u0336', '\u0337',
    '\u0338', '\u0339', '\u033A', '\u033B', '\u033C', '\u033D', '\u033E', '\u033F',
]

def glitch_text(text, intensity=5):
    """Add combining diacritics to create glitch effect"""
    result = []
    for char in text:
        result.append(char)
        for _ in range(random.randint(1, intensity)):
            result.append(random.choice(COMBINERS))
    return ''.join(result)

def make_symbol_block(theme, count=8, separator=''):
    """Create a dense symbol block from a theme"""
    symbols = SYMBOL_SETS.get(theme, SYMBOL_SETS['cosmic'])
    return separator.join(random.choice(symbols) for _ in range(count))

def make_multi_theme_block(themes, count_per=5):
    """Combine multiple symbol themes"""
    result = []
    for theme in themes:
        symbols = SYMBOL_SETS.get(theme, SYMBOL_SETS['cosmic'])
        result.append(''.join(random.choice(symbols) for _ in range(count_per)))
    return ''.join(result)

def make_fragmented_phrase(word_count=3, glitch_level=0):
    """Create fragmented netspeak phrases"""
    words = random.sample(FRAGMENTS, word_count)
    phrase = ''.join(words)
    if glitch_level > 0:
        phrase = glitch_text(phrase, glitch_level)
    return phrase

def make_box_pattern(width=12, height=3):
    """Create box drawing patterns"""
    patterns = []
    for _ in range(height):
        row = ''.join(random.choice(SYMBOL_SETS['box']) for _ in range(width))
        patterns.append(row)
    return '\n'.join(patterns)

def make_gradient_block(length=20):
    """Create density gradient"""
    gradient = ['█', '▓', '▒', '░']
    result = []
    for i in range(length):
        idx = int((i / length) * len(gradient))
        if idx >= len(gradient):
            idx = len(gradient) - 1
        result.append(gradient[idx])
    return ''.join(result)

def make_braille_pattern(width=8):
    """Random braille pattern"""
    return ''.join(random.choice(SYMBOL_SETS['braille']) for _ in range(width))

# Generate examples
print("=" * 70)
print("VIBE CANDY GENERATOR - New Generations")
print("=" * 70)

print("\n[COSMIC SYMBOLIC BLOCKS]")
for _ in range(5):
    block = f"[{make_symbol_block('cosmic', 10)}]"
    print(block, end=' ')
print()

print("\n[GEOMETRIC PATTERNS]")
for _ in range(5):
    block = f"[{make_symbol_block('geometric', 8)}]"
    print(block, end=' ')
print()

print("\n[MATHEMATICAL DENSITY]")
for _ in range(5):
    block = f"[{make_symbol_block('math', 12)}]"
    print(block, end=' ')
print()

print("\n[ALCHEMICAL SYMBOLS]")
for _ in range(3):
    block = f"[{make_symbol_block('alchemy', 6)}]"
    print(block, end=' ')
print()

print("\n[MULTI-THEME FUSION]")
for _ in range(3):
    themes = random.sample(['cosmic', 'geometric', 'math', 'alchemy', 'mystical'], 3)
    block = f"[{make_multi_theme_block(themes, 4)}]"
    print(block)

print("\n[FRAGMENTED NETSPEAK]")
for _ in range(5):
    phrase = make_fragmented_phrase(3, 0)
    block = f"[{phrase}::{random.randint(100, 999)}]"
    print(block)

print("\n[GLITCHED FRAGMENTS]")
for _ in range(3):
    phrase = make_fragmented_phrase(2, 4)
    block = f"[{phrase}]"
    print(block)

print("\n[DENSITY GRADIENTS]")
for _ in range(3):
    gradient = make_gradient_block(25)
    print(f"[{gradient}]")

print("\n[BRAILLE ULTRA-DENSITY]")
for _ in range(5):
    pattern = make_braille_pattern(20)
    print(f"[{pattern}]")

print("\n[BOX DRAWING MATRICES]")
print(make_box_pattern(30, 5))

print("\n[MIXED DENSITY SHOWCASE]")
showcase = f"""
[{make_symbol_block('cosmic', 6)}][{make_symbol_block('math', 6)}][{make_symbol_block('geometric', 6)}]
[{make_fragmented_phrase(3)}::{make_symbol_block('arrows', 4)}]
[{make_braille_pattern(15)}]⊹[{make_symbol_block('alchemy', 5)}]
[{make_gradient_block(20)}]
[{glitch_text('VIBE', 6)}∴{glitch_text('CANDY', 6)}]
"""
print(showcase)

print("\n[CURRENCY FUSION]")
for _ in range(3):
    block = f"[{make_symbol_block('currency', 8)}]"
    print(block)

print("\n[ZODIAC WHEEL]")
print(f"[{make_symbol_block('zodiac', 12)}]")

print("\n[MUSICAL NOTATION]")
for _ in range(3):
    block = f"[{make_symbol_block('music', 8)}]"
    print(block)

print("\n[RUNIC INSCRIPTIONS]")
for _ in range(3):
    block = f"[{make_symbol_block('runic', 15)}]"
    print(block)

print("\n" + "=" * 70)
print("GENERATION COMPLETE")
print("=" * 70)
print("\nThese blocks can be used as SUNO AI prompt enhancers,")
print("adding semantic density and vibe texture to your music generation!")

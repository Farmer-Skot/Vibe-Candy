#!/usr/bin/env python3
"""
ASCII + COLOR Demo
Terminal ANSI colors, RGB, and various color systems
"""

# ANSI Color Codes
class Color:
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'

    # Reset
    RESET = '\033[0m'

def rgb(r, g, b, text):
    """24-bit RGB color (not all terminals support this)"""
    return f'\033[38;2;{r};{g};{b}m{text}\033[0m'

def bg_rgb(r, g, b, text):
    """24-bit RGB background color"""
    return f'\033[48;2;{r};{g};{b}m{text}\033[0m'

print("=" * 70)
print(f"{Color.BOLD}BASIC ANSI COLORS{Color.RESET}")
print("=" * 70)

colors = [
    (Color.BLACK, "BLACK", Color.BG_WHITE),
    (Color.RED, "RED", ""),
    (Color.GREEN, "GREEN", ""),
    (Color.YELLOW, "YELLOW", ""),
    (Color.BLUE, "BLUE", ""),
    (Color.MAGENTA, "MAGENTA", ""),
    (Color.CYAN, "CYAN", ""),
    (Color.WHITE, "WHITE", Color.BG_BLACK),
]

for fg, name, bg in colors:
    print(f"{bg}{fg}▓▓▓▓▓▓▓▓▓▓{Color.RESET} {name:15} {fg}████████████████{Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}BRIGHT COLORS{Color.RESET}")
print("=" * 70)

bright_colors = [
    (Color.BRIGHT_BLACK, "BRIGHT BLACK"),
    (Color.BRIGHT_RED, "BRIGHT RED"),
    (Color.BRIGHT_GREEN, "BRIGHT GREEN"),
    (Color.BRIGHT_YELLOW, "BRIGHT YELLOW"),
    (Color.BRIGHT_BLUE, "BRIGHT BLUE"),
    (Color.BRIGHT_MAGENTA, "BRIGHT MAGENTA"),
    (Color.BRIGHT_CYAN, "BRIGHT CYAN"),
    (Color.BRIGHT_WHITE, "BRIGHT WHITE"),
]

for fg, name in bright_colors:
    print(f"{fg}▓▓▓▓▓▓▓▓▓▓{Color.RESET} {name:15} {fg}████████████████{Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}TEXT STYLES{Color.RESET}")
print("=" * 70)

print(f"{Color.BOLD}Bold text{Color.RESET}")
print(f"{Color.DIM}Dim text{Color.RESET}")
print(f"{Color.ITALIC}Italic text{Color.RESET}")
print(f"{Color.UNDERLINE}Underlined text{Color.RESET}")
print(f"{Color.REVERSE}Reversed text{Color.RESET}")
print(f"{Color.STRIKETHROUGH}Strikethrough text{Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}COMBINED STYLES{Color.RESET}")
print("=" * 70)

print(f"{Color.BOLD}{Color.RED}Bold Red{Color.RESET}")
print(f"{Color.ITALIC}{Color.CYAN}Italic Cyan{Color.RESET}")
print(f"{Color.UNDERLINE}{Color.GREEN}Underlined Green{Color.RESET}")
print(f"{Color.BOLD}{Color.UNDERLINE}{Color.MAGENTA}Bold Underlined Magenta{Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}BACKGROUND COLORS{Color.RESET}")
print("=" * 70)

print(f"{Color.BG_RED}{Color.WHITE} White on Red {Color.RESET}")
print(f"{Color.BG_GREEN}{Color.BLACK} Black on Green {Color.RESET}")
print(f"{Color.BG_BLUE}{Color.YELLOW} Yellow on Blue {Color.RESET}")
print(f"{Color.BG_MAGENTA}{Color.WHITE} White on Magenta {Color.RESET}")
print(f"{Color.BG_CYAN}{Color.BLACK} Black on Cyan {Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}24-BIT RGB COLORS (if supported){Color.RESET}")
print("=" * 70)

# Rainbow gradient
print(rgb(255, 0, 0, "█") + rgb(255, 64, 0, "█") + rgb(255, 128, 0, "█") +
      rgb(255, 192, 0, "█") + rgb(255, 255, 0, "█") + rgb(192, 255, 0, "█") +
      rgb(128, 255, 0, "█") + rgb(64, 255, 0, "█") + rgb(0, 255, 0, "█") +
      rgb(0, 255, 128, "█") + rgb(0, 255, 255, "█") + rgb(0, 128, 255, "█") +
      rgb(0, 64, 255, "█") + rgb(0, 0, 255, "█") + rgb(64, 0, 255, "█") +
      rgb(128, 0, 255, "█") + rgb(192, 0, 255, "█") + rgb(255, 0, 255, "█") +
      " RAINBOW")

# Pastel colors
print(rgb(255, 182, 193, "█████") + " Light Pink")
print(rgb(255, 218, 185, "█████") + " Peach Puff")
print(rgb(221, 160, 221, "█████") + " Plum")
print(rgb(176, 224, 230, "█████") + " Powder Blue")
print(rgb(152, 251, 152, "█████") + " Pale Green")

print("\n" + "=" * 70)
print(f"{Color.BOLD}COLORED ASCII ART{Color.RESET}")
print("=" * 70)

# Fire effect
fire = f"""
{Color.BRIGHT_YELLOW}      *  {Color.BRIGHT_RED}*{Color.YELLOW}  *{Color.RESET}
{Color.BRIGHT_YELLOW}   *{Color.BRIGHT_RED}  /\\{Color.YELLOW}  /\\{Color.BRIGHT_YELLOW}  *{Color.RESET}
{Color.BRIGHT_RED}    /  \\/  \\{Color.RESET}
{Color.RED}   /        \\{Color.RESET}
{Color.RED}  /___{Color.YELLOW}▓▓{Color.RED}____\\{Color.RESET}
"""
print(fire)

# Wave effect
wave = f"{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.CYAN}～{Color.BLUE}～{Color.RESET}"
print(wave * 3)

# Forest
forest = f"{Color.GREEN}▲{Color.BRIGHT_GREEN}▲{Color.GREEN}▲{Color.RESET} {Color.BRIGHT_GREEN}▲{Color.GREEN}▲{Color.BRIGHT_GREEN}▲{Color.RESET} {Color.GREEN}▲{Color.BRIGHT_GREEN}▲{Color.GREEN}▲{Color.RESET}"
print(forest)

print("\n" + "=" * 70)
print(f"{Color.BOLD}ULTRA-DENSE COLORED SYMBOLS{Color.RESET}")
print("=" * 70)

# Combining density with color
print(f"{Color.RED}█▓▒░{Color.YELLOW}█▓▒░{Color.GREEN}█▓▒░{Color.CYAN}█▓▒░{Color.BLUE}█▓▒░{Color.MAGENTA}█▓▒░{Color.RESET}")
print(f"{Color.BRIGHT_RED}⣿⣿{Color.BRIGHT_YELLOW}⣿⣿{Color.BRIGHT_GREEN}⣿⣿{Color.BRIGHT_CYAN}⣿⣿{Color.BRIGHT_BLUE}⣿⣿{Color.BRIGHT_MAGENTA}⣿⣿{Color.RESET}")
print(f"{Color.RED}╔{Color.YELLOW}═{Color.GREEN}╗{Color.CYAN}╔{Color.BLUE}═{Color.MAGENTA}╗{Color.RED}╔{Color.YELLOW}═{Color.GREEN}╗{Color.CYAN}╔{Color.BLUE}═{Color.MAGENTA}╗{Color.RESET}")

print("\n" + "=" * 70)
print(f"{Color.BOLD}256 COLOR PALETTE SAMPLE{Color.RESET}")
print("=" * 70)

# 256 color mode (partial display)
for i in range(16, 256, 6):
    print(f'\033[38;5;{i}m▓▓{Color.RESET}', end='')
    if (i - 16) % 36 == 0:
        print()

print("\n")

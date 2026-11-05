"""
Charts of the four stop-word lists: how big each list is and what kinds of
words it contains (grouped from the comment headings in each file).

Run:  python visualise.py      (needs matplotlib)
Writes figures/list_sizes.png, figures/list_composition.png and
figures/composition_heatmap.png
"""

import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

HERE = Path(__file__).parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

LANGUAGES = ["hindi", "bengali", "gujarati", "tamil"]
GROUPS = ["Pronouns", "Postpositions", "Verbs and auxiliaries", "Conjunctions",
          "Question words", "Quantifiers", "Other"]
COLOURS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#6250d6", "#c9c8c3"]
INK, INK_2 = "#1b1f2a", "#5b6275"
BLUE = LinearSegmentedColormap.from_list("blue", ["#f4f8fd", "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
plt.rcParams.update({"font.family": "Helvetica", "text.color": INK, "axes.labelcolor": INK_2,
                     "xtick.color": INK, "ytick.color": INK, "figure.facecolor": "white"})


def group_of(heading):
    h = heading.lower()
    if "pronoun" in h or "possessive" in h or "demonstrative" in h:
        return "Pronouns"
    if "postposition" in h:
        return "Postpositions"
    if "verb" in h:
        return "Verbs and auxiliaries"
    if "conjunction" in h or "quotative" in h:
        return "Conjunctions"
    if "interrogative" in h or "relative" in h:
        return "Question words"
    if "quantifier" in h:
        return "Quantifiers"
    return "Other"


def composition(language):
    """Count the distinct words of a list under each group."""
    source = (HERE / f"{language}_stopwords.py").read_text(encoding="utf-8")
    body = source[source.index(f"{language}_stopwords = ["):]
    body = body[:body.index("\n]")]
    seen, counts, heading = set(), dict.fromkeys(GROUPS, 0), "Other"
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("#"):
            heading = line.lstrip("# ")
            continue
        for word in re.findall(r'"([^"]+)"', line):
            if word not in seen:
                seen.add(word)
                counts[group_of(heading)] += 1
    return counts


data = {lang: composition(lang) for lang in LANGUAGES}
names = [l.title() for l in LANGUAGES]

# 1. List sizes
fig, ax = plt.subplots(figsize=(7, 3.2))
sizes = [sum(data[l].values()) for l in LANGUAGES]
bars = ax.barh(names[::-1], sizes[::-1], color="#2a78d6", height=0.55)
for bar, v in zip(bars, sizes[::-1]):
    ax.text(v + 3, bar.get_y() + bar.get_height() / 2, str(v), va="center", fontsize=11)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#c9c8c3")
ax.tick_params(left=False)
ax.set_xlim(0, max(sizes) * 1.15)
ax.set_title("Number of stop words in each list", loc="left", fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(FIG / "list_sizes.png", dpi=200)
plt.close(fig)

# 2. Composition pies
fig, axes = plt.subplots(1, 4, figsize=(13, 4.2))
for ax, lang, name in zip(axes, LANGUAGES, names):
    values = [data[lang][g] for g in GROUPS]
    ax.pie(values, colors=COLOURS, startangle=90, counterclock=False,
           wedgeprops={"edgecolor": "white", "linewidth": 2},
           autopct=lambda p: f"{p:.0f}%" if p >= 7 else "", pctdistance=0.72,
           textprops={"fontsize": 9, "color": INK})
    ax.set_title(f"{name}\n{sum(values)} words", fontsize=11)
fig.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=c) for c in COLOURS], labels=GROUPS,
           loc="lower center", ncol=7, frameon=False, fontsize=10)
fig.suptitle("What each list is made of", fontsize=13, fontweight="bold", x=0.02, ha="left")
fig.tight_layout(rect=(0, 0.08, 1, 0.94))
fig.savefig(FIG / "list_composition.png", dpi=200)
plt.close(fig)

# 3. Heatmap: language x group (number of words)
M = np.array([[data[l][g] for g in GROUPS] for l in LANGUAGES])
fig, ax = plt.subplots(figsize=(9.5, 3.3))
ax.imshow(M, cmap=BLUE, vmin=0, vmax=M.max(), aspect="auto")
ax.set_xticks(range(len(GROUPS)), [g.replace(" and ", " and\n").replace(" words", "\nwords") for g in GROUPS])
ax.set_yticks(range(len(names)), names)
ax.set_xticks(np.arange(-.5, len(GROUPS), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(names), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="both", length=0)
for s in ax.spines.values():
    s.set_visible(False)
for i in range(len(names)):
    for j in range(len(GROUPS)):
        ax.text(j, i, M[i, j], ha="center", va="center", fontsize=11,
                color="white" if M[i, j] > 0.55 * M.max() else INK)
ax.set_title("Number of words in each category, per list", loc="left", fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(FIG / "composition_heatmap.png", dpi=200)
plt.close(fig)

for lang in LANGUAGES:
    print(lang, data[lang])

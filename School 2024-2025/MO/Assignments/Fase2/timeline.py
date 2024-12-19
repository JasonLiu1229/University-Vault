from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Events data
events = [
    (datetime(1930, 7, 19), "Oprichting RTT\nStart van Belgische telecommunicatie"),
    (datetime(1992, 1, 1), "Privatisering\nRTT wordt Belgacom"),
    (datetime(1994, 7, 1), "Lancering Proximusnetwerk\nBegin mobiele revolutie"),
    (datetime(1996, 1, 1), "Verkoop aandelen\nInternationaal consortium"),
    (datetime(1997, 1, 1), "Oprichting BICS\nOvername Skynet"),
    (datetime(2004, 3, 22), "Beursgang Belgacom"),
    (datetime(2006, 1, 1), "Volledige eigendom\nProximus door Belgacom"),
    (datetime(2010, 1, 1), "Partnerships\nUitbreiding entertainment"),
    (datetime(2012, 1, 1), "Lancering 4G-netwerk"),
    (datetime(2014, 9, 1), "Rebranding naar Proximus"),
    (datetime(2015, 4, 15), "Naamswijziging\nProximus NV"),
    (datetime(2016, 1, 1), "Start 'Fiber for Belgium'"),
    (datetime(2020, 1, 1), "Lancering 5G-netwerk\nFiberpartnerschap"),
    (datetime(2021, 1, 1), "Overname Mobile Vikings")
]

# Prepare the timeline data
dates = [event[0] for event in events]
descriptions = [event[1] for event in events]

# Dynamic levels to prevent overlapping annotations
levels = [2, 4, 2, -4, -2, 3, 1, -3, -1, 3.5, 2, -4, -2, 4, 2]
current_level = 0
spacing = 0.4  # Space between levels

# The figure and the axes
fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
ax.set(title="Proximus Timeline")

# Plot the timeline
for i, (date, description) in enumerate(events):
    level = levels[i]

    # Draw a vertical line for the event
    ax.vlines(date, 0, level, color="tab:blue", linewidth=2)

    # Mark the event point
    ax.plot(date, 0, "o", color="tab:blue")

    # Annotate the event
    ax.annotate(description, xy=(date, level),
                xytext=(0, 10 if level > 0 else -10), textcoords="offset points",
                ha="center", va="bottom" if level > 0 else "top",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.7),
                fontsize=9, color="black")

# Formatting the timeline
ax.axhline(0, color="black", linewidth=0.5)
ax.yaxis.set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.margins(y=0.3)
plt.savefig('timeline.png', dpi=300, bbox_inches='tight')

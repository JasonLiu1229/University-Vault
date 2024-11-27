import matplotlib.pyplot as plt
import pandas as pd
from math import pi

df = pd.DataFrame({
    'group': ['Proximus', 'Telenet'],
    'Naleving van regelgeving':                                         [9, 4],
    'Stabiele en betrouwbare infrastructuur':                           [8.5, 6],
    'Cybersecurity en databescherming':                                 [8.5, 7],
    'Toegang tot 5G- en toekomstige netwerken':                         [8.5, 8.75],
    'Beschikbaarheid en efficiëntie van leveranciers':                  [8.5, 7],
    'Klantgerichte klantenservice en ondersteuning':                    [7, 7],
    'Groene en duurzame praktijken':                                    [9.5, 9],
    'Innovatie in pakketten en dienstenaanbod':                         [7.5, 7],
    'Snel en flexibel inspelen op nieuwe technologieën':                [8, 8.5],
    'Samenwerkingen met technologie- en socialemediabedrijven':         [8.5, 8.5],
    'Snelheid van netwerk en klantconnectiviteit':                      [9, 8],
})

categories = list(df)[1:]
N = len(categories)

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='grey', size=8)

ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=7)
plt.ylim(0, 10)  # Corrected the ylim to match the maximum data value

# Plot each group on the radar chart
for i in range(len(df)):
    values = df.loc[i].drop('group').values.flatten().tolist()
    values += values[:1]
    
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=df['group'][i])
    ax.fill(angles, values, alpha=0.1)

plt.legend(loc='upper right', bbox_to_anchor=(0, 0))

plt.savefig('radar_chart.png', dpi=300, bbox_inches='tight')

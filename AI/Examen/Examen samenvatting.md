> Samenvatting van AI van lecture 1 - 10
# Lecture 1 Search
![[Pasted image 20240120181210.png]]
## Intro
### Agent that plan ahead
![[Pasted image 20240120191630.png]]
#### Reflex agents
+ Acties worden bepaald door zijn observaties.
+ Kan eventueel een geheugen hebben van de momentele status van de wereld.
+ Het bepaald zijn acties zonder de consequences in rekening te houden.
+ **Ziet de wereld hoe het is.**
#### Planning agents
+ Vraagt zich af, "Wat als?".
+ Bepaalt zijn acties op basis van hypothesis, dus kijkt naar zijn consequences van zijn acties.
+ Moet een model bekijken of hoe de wereld kan zijn indien het bepaalde acties neem.
+ Het moet een goal hebben. (Testbaar)
+ **Ziet hoe de wereld kan zijn.**
### Search problems
#### Basis van search problems
+ State space
+ Successor function met zijn acties en de kost van zijn acties.
+ Een start state en goal state.
Een oplossing van search problem, is een reeks van acties die genomen wordt van start state om de goal state te bereiken.
#### State space 
Een state space is onze model dat we willen voorstellen. Het bevat verschillende componenten: de verschillende states, acties die het kan uitvoeren, successor functies en zijn goal state(s).
##### State space graphs
![[Pasted image 20240120234902.png]]
Dit is een wiskunde representatie van het zoek probleem. 
+ Nodes zijn abstracte configuraties van de wereld.
+ Arcs zijn de verschillende successors (resultaten van verschillende acties).
+ Goal test is een set van alle goal nodes.
Elke mogelijke state in de state space, komt enkel maar 1x voor.
Meestal is dit niet mogelijk, memory overhead. Maar het is goed concept. (Kan handig zijn voor kleiner problemen)
##### State space search Tree
 ![[Pasted image 20240120234832.png]]
 Het is een boom representatie van de state space.
+ Beeld meer een "what if?" model uit. 
+ De root is de start state.
+ De kinderen zijn dan de successors die mogelijk zijn.
+ Nodes zijn dan eigenlijk de verschillende plans om een bepaalde state te bekomen.
+ **Meeste problemen zijn niet representeerbaar in een boommodel.**
##### Graphs vs Search trees
![[Pasted image 20240120235418.png]]
Een graph met een loop kan resulteren tot een boom dat oneindig door gaat.
#### Searching with a search trede
![[Pasted image 20240120235622.png]]
###### Pseudocode
![[Pasted image 20240120235702.png]]
Enkele belangrijke puntjes
+ Fringe
+ Expansion
+ Exploration strategy
![[Pasted image 20240120235945.png]]
## Uninformed search
### Search probleem properties
Enkele properties dat het moet nagaan.
+ Complete: Guaranteed to find a solution if one exists? 
+ Optimal: Guaranteed to find the least cost path? 
+ Time complexity? 
+ Space complexity?
### DFS (Depth-First-Search)
> Bekijk wat de bodem ons eerst resulteert en kijk daarna zijn naasten.
> Onze fringe is een LIFO stack.
![[Pasted image 20240121000025.png]]
#### Properties
![[Pasted image 20240121001440.png]]
Op welke nodes breidt DFS uit?
+ Neemt een linkse noden.
+ Kan de hele boom aflopen.
+ Indien de hoogte van de boom finite is, dan duurt het $O(b^m)$. 

Hoeveel ruimte neemt de fringe op?
+ Heeft enkel siblings op zijn pad naar de root, dus $O(bm)$.

Is het compleet?
+ Indien m = infinite, dan kan de boom cyclussen hebben. Dit resulteert in geen oplossing omdat het infinite kan blijven runnen.

Is het optimaal?
+ Nee, want het kiest de "Links mogelijk oplossing", zonder enige gedachten aan de diepte of de kost.
### BFS (Breath-First-Search)
> Kijk wat elke laag ons resulteert.
> Onze fringe is een FIFO queue.
![[Pasted image 20240121001858.png]]
#### Properties
![[Pasted image 20240121002808.png]]
Op welke nodes breidt BFS uit?
+ Kijk naar alle nodes boven de hoogste oplossing in de boom.
+ Laat de diepte van de hoogste oplossing s zijn.
+ Dan duurt de search $O(b^s)$.

Hoeveel ruimte neemt de fringe op?
+ Indien we heel de laatste laag mee tellen (laag van de hoogste oplossing), dan $O(b^s)$.

Is het compleet?
+ s moet finite zijn als een oplossing bestaat, dus ja.

Is het optimaal?
+ Enkel als de kost 1 zijn tussen de paden.
### DFS vs BFS
DFS zou beter resultaten opleveren indien onze goal state diep links in de boom plaats vindt. BFS resulteert algemeen betere resultaten indien s > m, dus de diepte van goal state is hoger dan diepte van de boom.
### Iterative deepening
Idee: Combineer voordelen van beide, dus we incrementen de diepte dat we DFS runnen hele tijd met 1.
+ DFS op diepte 1, check of er oplossingen zijn, indien niet dan ...
+ DFS op diepte 2, ...
+ ...
Het is een goed idee maar nog niet perfect.
### Uniform Cost Search
> Wat als onze paden geen kost hebben van 1, maar een willekeurige kost. DFS zou misschien ons resulteren in de kortste pad maar niet de meest kost vriendelijke pad.\
> Onze fringe is een priority queue.
![[Pasted image 20240121003933.png]]
#### Properties
![[Pasted image 20240121004504.png]]
Op welke nodes breidt UCS uit?
+ Kijkt naar alle nodes met een kost minder dan de momentele goedkoopste kost.
+ Als de oplossing een kost heeft van C* en de bogen een kost van minstens $\epsilon$, dan is de "effective depth" ongeveer C*/$\epsilon$.
+ Heeft een tijdscomplexiteit van $O(b^{C*/\epsilon})$.

Hoeveel ruimte neemt de fringe op?
+ $O(b^{C*/\epsilon})$ ongeveer.

Is het compleet?
+ Indien de best oplossing een finite set is en de minimum arc cost is positief, dan ja.

Is het optimaal?
+ Ja, zie bewijs in A*.
#### Issues
+ Kijkt naar elke mogelijke "richting".
+ Heeft geen informatie in verband met de goal state zijn locatie.
## Informed search
### Heuristics
+ Heuristics dienen om een estimatie te maken, hoe dicht de goal state is vergeleken zijn huidige locatie.
+ Ze zijn gemaakt voor specifieke zoek problemen.
+ Voorbeelden: Manhatten distance, Euclidean distance.
![[Pasted image 20240121141900.png]]
### Greedy Search
> Kijk naar de node die het dicht bij de goal state is.
![[Pasted image 20240121141921.png]]

Algemene gevallen:
+ Best-first, brengt rechtstreeks naar de goal. 
![[Pasted image 20240121142723.png]]
Worst case:
+ Dit kan resulteren in een "badly-guided DFS". Ofwel lange paden met grote kost.
![[Pasted image 20240121142733.png]]
### A* Search
> Een combinatie van UCS en Greedy, waarbij we de paden sorteren op kost en gebruik maken van heuristics om de kortste pad te nemen.
![[Pasted image 20240121142826.png]]
#### Combining UCS en Greedy
We maken gebruik van twee functies:
+ Uniform-cost orders by path cost, ofwel *backward cost g(n)*.
+ greedy orders by goal proximity, ofwel *forward cost h(n)*.

A* search orders by the sum:
+ f(n) = g(n) + h(n)
![[Pasted image 20240121143547.png]] ![[Pasted image 20240121143626.png]]

Wanneer moet A* eindigen?
+ We eindigen A* search indien we de goal state dequeue van de priority queue. Dit is omdat indien we een goal state enqueue, kunnen er nog andere paden zijn die leiden tot een betere pad.

Is A* optimaal?
+ Nee, indien we een slechte heuristics hebben.
+ Actual bad goal cost < estimated good goal cost.
+ We willen dat de estimatie kleiner is dan de werkelijke waardes.
#### Admissible Heuristics
![[Pasted image 20240121144424.png]]
Een heuristic h is admissible als:
+ $0 \le h(n) \le h^*(n)$. Waarbij $h^*(n)$ is de true cost van de dicht bij zijnde goal.
Een admissible heuristic bedenken is de belangrijkste stap om A* te implementeren.
#### Optimality 
![[Pasted image 20240121145519.png]]
Stel:
+ A is een optimale node
+ B is een suboptimale node
+ h is admissible
Dan:
+ A zou de fringe exiten voor B
Bewijs:
![[Pasted image 20240121145704.png]]
+ Stel B is op de fringe.
+ Stel de voorganger van A is n, die ook op de fringe zit.
+ Dan: n zal eerder uitbreiden dan B
	+ f(n) is less or equal to f(A)
		+ Definitie van f-cost admissibility van h, h = 0 als we kijken naar een goal state.
			+ $f(n) = g(n) + h(n)$
			+ $f(n) \le g(n)$
			+ $g(A) = f(A)$
	+ f(A) is less than f(B)
		+ B is suboptimal, h = 0 at a goal.
			+ $g(A) \lt g(B)$
			+ $f(A) \lt f(B)$
	+ n expands before B
		+ $f(n) \le f(A) \lt f(B)$
+ Alle voogangers v
# Lecture 2
# Lecture 3
# Lecture 4
# Lecture 5
# Lecture 6
# Lecture 7
# Lecture 8
# Lecture 9
# Lecture 10

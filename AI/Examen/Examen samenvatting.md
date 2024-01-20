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
# Lecture 2
# Lecture 3
# Lecture 4
# Lecture 5
# Lecture 6
# Lecture 7
# Lecture 8
# Lecture 9
# Lecture 10

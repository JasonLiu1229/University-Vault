> Samenvatting van AI van lecture 1 - 10
> https://github.com/mebusy/notes/tree/master/dev_notes voor extra info van andere student
> In het begin nederlands vanaf lecture heb ik opgegeven en is het gwn engels.
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

Onze estimatie van heuristic moet kleiner zijn dan onze werkelijke kost. Indien onze heuristic dichter naar onze werkelijke kost komt, hoe beter onze estimatie. Dit komt meestal met nadeel, dat onze heuristic complexer wordt om te berekenen.
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
+ Alle voorgangers van A zullen eerder expanden dan B
+ A zou dan uiteindelijk eerder expanden dan B
+ A* search is dan optimaal
#### Properties
![[Pasted image 20240121152213.png]]
UCS zou uniform expanden, terwijl A* meer zou expanden richting de goal.
![[Pasted image 20240121152312.png]]
### Semi-Lattice of heuristics
#### Trivial heuristics, Dominance
+ **Dominance: $h_a \ge h_c$ if**
	+ $\forall n : h_a(n) \ge h_c(n)$
	+ Dus voor alle waardes n, is heuristic a beter dan heuristic c.
+ **Heuristic vormen een Semi-Lattice:**
	+ Max van de admissible heuristics is admissible
		+ $h(n) = max(h_a(n), h_b(n))$
			![[Pasted image 20240121153348.png]]
+ **Triviale heuristics**
	+ Bodem van de lattice is de zero heuristic
	+ Top of lattice is de exact heuristic
### A* Graph search
Indien we loops hebben on onze state graph, dit kan leiden in infinite search.
- Idea: never expand a state twice
- How to implement:
	- Tree search + set of expanded states (“closed set”)
	- Expand the search tree node-by-node, but…
	    - Before expanding a node, check to make sure its state has never been expanded before
	    - If you have, skip it, if you haven't, call the successor function and then add it to closed set.
- Important: **store the closed set as a set**, not a list
- Can graph search wreck completeness? Why/why not?
	- No. It's parts of the Search Tree.
- How about optimality?
	- Unfortunately close list will introduce another problem
	- Admissible heuristic with tree search is optimal but graph search no guarantees.

Er kunnen fouten lopen, indien we in de eerste iteratie een slechte keuzen maken, zullen we de altijd fouten keuzes maken daarna. Dit is omdat we werken met een closed set, en indien een slechte heuristic ons de foute pad leidt, dan kan het zijn dat een node al doorlopen is die leidt tot een betere pad.
#### Consistency of heuristics
![[Pasted image 20240121154210.png]]
**Main idea: estimated heuristic costs ≤ actual costs**
+ Admissibility: heuristic cost $\le$ actual cost to goal
	+ h(A) ≤ actual cost from A to G
+ Consistency: heuristic “arc” cost ≤ actual cost for each arc
	+ h(A) – h(C) ≤ cost(A to C)
**Consequences van consistency**
+ The f value along a path never decreases
	+ h(A) ≤ cost(A to C) + h(C)
+ A* graph search is optimal
#### Optimality graph search
- **Sketch: consider what A* does with a consistent heuristic:**
    - Fact 1: In tree search, A* expands nodes in increasing total f value (f-contours)
    - Fact 2: For every state s, nodes that reach _**s**_ optimally are expanded before nodes that reach _**s**_ suboptimally
    - Result: A* graph search is optimal
	![[Pasted image 20240121155400.png]]
- **Consider what A* does:**
    - Expands nodes in increasing total f value (f-contours)
    - Reminder: f(n) = g(n) + h(n) = cost to n + heuristic
    - Proof idea: the optimal goal(s) have the lowest f value, so it must get expanded first
- **Bewijs via contradictie:**
    - New possible problem: some n on path to G* isn’t in queue when we need it, because some worse n’ for the same state dequeued and expanded first (disaster!)
    - Take the highest such n in tree
    - Let p be the ancestor of n that was on the queue when n’ was popped
    - f(p) < f(n) because of consistency
    - f(n) < f(n’) because n’ is suboptimal
    - p would have been expanded before n’
    - Contradiction!
    ![[Pasted image 20240121155920.png]]
### Optimality
- Tree search:
    - A* is optimal if heuristic is admissible
    - UCS is a special case (h = 0)
- Graph search:
    - A* optimal if heuristic is consistent
    - UCS optimal (h = 0 is consistent)
- Consistency implies admissibility
- In general, most natural admissible heuristics tend to be consistent, especially if from relaxed problem.
---
# Lecture 2
![[Pasted image 20240121160255.png]]
> Start part one.
## What is search for?
- Assumptions about the world:
    - a single agent
    - deterministic actions
    - fully observed state
        - you KNOW the configuration that you start in
        - and then you plan about exactly how the world will evolve
    - discrete state space

- Planning: sequences of actions
    - The path to the goal is the important thing
    - Paths have various costs, depths
    - Heuristics give problem-specific guidance

- Identification: assignments to variables
    - The goal itself is important, **not the path**
    - All paths at the same depth (for some formulations)
    - CSPs are specialized for identification problems
## CSP (Constraint Satisfaction Problems)
## Constraint Graphs
![[Pasted image 20240121163739.png]]
- Standard search problems
	- State is een "Black box": arbitraire data structuur.
	- Goal test kan ener welke functie zijn over states.
	- Successor functie kan ook ener welke functie zijn.

- CSP:
	- Het is een speciale subset van zoekproblemen
	- Een state is gedefinieerd door **variabelen X**, met waardes van **een domein D**.
	- Goal test is een **set van constraints**, die specificeren welke combinaties toegelaten zijn voor een subset van de variabelen.

- Allows useful general-purpose algorithms with more power than standard search algorithms.
## Constraint graph
![[Pasted image 20240121164434.png]]
- Binary CSP:
    - Each constraint relates (at most) two variables
- Binary constraint graph:
    - Nodes are variables, arcs show constraints
- General-purpose CSP algorithms use the graph structure to speed up search.
    - E.g., Tasmania is an independent subproblem!
## Varieties of CSPs and Constraints
![[Pasted image 20240121160708.png]]
### CSPs
- Discrete variables
	- Finite domains
		- Indien we size d mogelijkheden hebben in het domein, dan hebben we $O(d^n)$ mogelijke complete assignments.
		- E.g., Boolean CSPs, including Boolean satisfiability (NP- complete)
	- Infinite domains (integers, strings, etc.)
		- E.g., job scheduling, variables are start/end times for each job
		- Linear constraints solvable, nonlinear undecidable
	![[Pasted image 20240121170549.png]]

- Continuous variables
	- E.g., start/end times for Hubble Telescope observations
	- Linear constraints solvable in polynomial time by LP methods
	![[Pasted image 20240121170622.png]]
### Constraints
- Varieties of Constraints
	- Unary constraints
		- Involve a single variable (equivalent met reducing domains)
		- SA ≠ green
	- Binary constraint
		- Involves pairs of variables
		- SA ≠ WA
	- Higher-order constraints
		- Involves 3 or more variables
			- e.g., cryptarithmetic column constraints

- Preferences
	- E.g., red is better than green
	- Often representable by a cost for each variable assignment
	- Gives constrained optimization problems
	- (We’ll ignore these until we get to Bayes’ nets
## Standard Search Formulation
- Standard search formulation of CSPs
- States defined by the values assigned so far (partial assignments)
    - Initial state:
        - The empty assignment, {}
    - Successor function:
        - Assign a value to an _**unassigned**_ variable
    - Goal test:
        - The current assignment is complete and satisfies all constraints
- We’ll start with the straightforward, naïve approach, then improve it

- What would BFS do ?
    - Will expand all levels
- What would DFS do ?
    - Going to look everywhere where they aren't first.
- What problems does naïve search have?
	- It is inefficient. 
## Backtracking Search
- Backtracking search is the basic _**uninformed**_ algorithm for solving CSPs
- Idea 1: One variable at a time
    - Variable assignments are commutative, so fix ordering
    - I.e., \[WA = red then NT = green] same as \[NT = green then WA = red]
    - Only need to consider assignments to a single variable at each step
- Idea 2: Check constraints as you go
    - I.e. consider only values which do not conflict previous assignments
    - Might have to do some computation to check the constraints
    - “Incremental goal test”
- Depth-first search with these two improvements is called backtracking search (not the best name)
### Pseudocode
![[Pasted image 20240121184302.png]]
- Backtracking = DFS + variable-ordering + fail-on-violation
- What are the choice points?
	- Het kiest zijn variables op basis wat hij nog niet geprobeerd heeft.
### Improving backtracking
- General-purpose ideas give huge gains in speed
- Ordering:
    - Which variable should be assigned next? 
    - In what order should its values be tried? 
- Filtering:
    - Can we detect inevitable failure early?
- Structure:
    - Can we exploit the problem structure?
## Filtering
> Keep track of domains for unassigned variables and cross off bad options
![[Pasted image 20240121184602.png]]
### Forward checking
-  Cross off values that violate a constraint when added to the existing assignment.
	![[Pasted image 20240121185434.png]]
- If we assigned red to WA , we should remove red choice from NT , SA.
- So that basic idea when I assigned something I look at its _**neighbors**_ in the graph and cross things off, that's called forward checking. So the neighbors of WA would lose red.
- Forward checking doesn't check interactions between unassigned variables just checks interactions between assigned variables and their neighbors. Anything further is thinking too hard for forward checking.
### Constraint Propagation
- Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:
	![[Pasted image 20240121184915.png]]
	- Hier zien we duidelijk dat SA en NT alleen als opties blauw hebben, dit zal leiden tot een fout oplossing.
- Constraint propagation: reason from constraint to constraint,
	- Constraint propagation is the process of communicating the domain reduction of a decision variable to all of the constraints that are stated over this variable.
## Consistency of A single arc
- So far we talked about checking an assignment against its neighbors, here we were talking out checking between two unassigned variables.
 - An arc X → Y is consistent iff for every x in the tail there is some y in the head which could be assigned without violating a constraint
 - Example:
	 ![[Pasted image 20240121185628.png]]
	 - Here WA is assigned. The NT is not assigned, but I can still look at the 2 of them and check if this arc is consistent. So let's do it, we check everything in the tail. So we look at the NT and we say, is there anything in you remaining domain which would have no continuation into the head? 
	 - So we say, well, if I assigned you blue, it would be ok. Green ? it would be ok. Red ? not ok. So red is something in the tail for which there is no assignments in the head which doesn't cause a constraint violation. So this arc is not constraint.
	- We can however, make it consistent. We can remove things from the tail, the red in NT.
	- So now we can check other consistencies, let's try Q->WA. These two are not actually connected by a constraint, so it should be easy to check. This is arc is already consistent.
- How can you remember this?
	- Remember, the constraints are like rules, and these algorithms are like police. They're going to go and enforce the rules. And you can imagine this arc is going to get pulled over by your algorithm, which is the CSP police. And what do they do when they pull the arc over? Right they pop open the trunk and they look for anything that's illegal. They are going to take anything bad out.
	- All these algorithms have the same shape. You pull over an arc, you fish around in its trunk and cross the bad thing off. That's enforcing the consistency of a single arc.
		![[Pasted image 20240121190306.png]]
- Forward checking: Enforcing consistency of arcs pointing to each new assignment
### Arc Consistency of an Entire CSP
- A simple form of propagation makes sure **all** arcs are consistent:
- Example:
	![[Pasted image 20240121190442.png]]
	- WA and Q have been assigned , red and green. NT, NSW, SA had their domain reduced by some previous pruning.
	- I can go visit arcs. First we check V->NSW. We notice they are neighbors. All right, this is the first time we're checking the consistency of an arc that doesn't point to an assignment. So I go through and I check the tail V, blue is find, red is fine, green is fine too.
	- Let's look SA->NSW. SA and NSW are adjacent, so I'm going to look at SA. What is in the tail? Blue, it is fine.
	- BUT, let's check the arc in the other direction. So now I look at NSW, is red ok? Yes. Is blue ok? NO. So we erase blue from NSW. Not it's consistent.
	- There's a tricky case. We just check V->NSW. We just declared it consistent, but that was on the basis of having blue and red available in the head at NSW. And one of those is gone, so the consistency may no longer hold. 
	- So I have to go back to V, and I have to check V->NSW again. Red now is no longer ok. Erasing red from V. 
	- So any time you do a delete of a value from a domain, every arc pointing into it needs to be rechecked.
	- So I keep doing this. The whole reason to do this is actually a completely different arc, SA->NT, neither of which is assigned. You noticed that you have to delete the blue from SA, which results in an empty domain, and an empty domain means a detected failure, which means backtracking.
- _**Remember: Delete from the tail!**_
- Important: If X loses a value, neighbors of X need to be rechecked!
- Arc consistency **detects failure earlier** than forward checking
- Can be run as a preprocessor, or more commonly after each assignment
- What's the downside of enforceing arc consistency ?
    - Runtime is bad.
    - So there's a trade-off between doing more filtering and just making the core search run faster.
    - In general, this is a very powerful method.
#### Pseudocode
![[Pasted image 20240121191154.png]]
- Runtime: O(n 2d 3), can be reduced to O(n 2d 2)\
- … but detecting all possible future problems is NP-hard – why?
	- The reason is that it essentially requires checking all possible assignments of values to variables to ensure they do not violate any constraints. This is computationally expensive as the number of possible assignments is exponential in the number of variables and the size of their domains.
### Limitations of Arc Consistency
- After enforcing arc consistency:
    - Can have one solution left
    - Can have multiple solutions left
    - Can have no solutions left
- Arc consistency still runs inside a backtracking search!
- The reason why our consistency in this bottom case wasn't sufficient to discover the inevitable failures because it's only checked in pairs. While it could be consistent in pairs, it's not consistent if we look in groups of 3.
	![[Pasted image 20240121191801.png]]
## Ordering
![[Pasted image 20240121161305.png]]
### Minimum remaining values (MRV)
- Variable Ordering: Minimum remaining values (MRV):
    - Choose the variable with the fewest legal left values in its domain
- Why min rather than max?
    - "Fail-fast" ordering
    - Also called "most constrained variable"
- **Hardest variable**
### Least constraining value (LCV)
- Value Ordering: Least Constraining Value
    - Given a choice of variable, choose the least constraining value
    - I.e., the one that rules out the fewest values in the remaining variables
    - Note that it may take some computation to determine this! (E.g., rerunning filtering)
- To choose which value is the least-constraining value, enforce arc consistency for each value (on a scratch piece of paper).
    - For each value, count the total number of values remaining over all variables.
- **Easiest value**
    - We want the one that has the least impact on the rest of the graph
- Why least rather than most?
    - Because it's a CSP, and in CSP, you have to do every variable. Sooner or later, you have to do it. You don't have to do every value.
    - So you might as well do the hard variables first, but if you're picking values, you want to pick the ones that are likely to work out, and maybe you don't even have to try the hard ones.
- Combining these ordering ideas makes 1000 queens feasible

> Start part 2
## K-Consistency
- Increasing degrees of consistency
    - 1-Consistency (Node Consistency): Each single node’s domain has a value which meets that node’s unary constraints
        - Every node's domain has at least one value that meets that node's constraints
        - basically just means you enforce unary constraints
    - 2-Consistency (Arc Consistency): For each pair of nodes, any consistent assignment to one can be extended to the other
    - K-Consistency: For each k nodes, any consistent assignment to k-1 can be extended to the kth node.
        - Arc-consistency says, if you can get one assigned, you can get 2 assigned
        - K-consistency says , if you can get k-1 assigned, then you can get k assigned. It's sort of mathematically a little weird, because it assumes that you can get to k-1, but who says you actually can? There is a stronger notion called strong k-consistency.
- Higher k more expensive to compute
- (You need to know the k=2 case: arc consistency)
### Strong K-Consistency
- Strong k-consistency: also k-1, k-2, … 1 consistent
- Claim: **strong n-consistency means we can solve without backtracking**!
- Why?
    - Choose any assignment to any variable
    - Choose a new variable
    - By 2-consistency, there is a choice consistent with the first
    - Choose a new variable
    - By 3-consistency, there is a choice consistent with the first 2
    - …
- Lots of middle ground between arc consistency and n-consistency! (e.g. k=3, called path consistency)
## Structure
![[Pasted image 20240121195559.png]]
Sometimes you look at a CSP that you're trying to solve and you see it has some special graph structure and based on that graph structure there will be some technique available to you that allows you to solve it in a particularly efficient way and we're going to see a couple examples.

So for example if your CSP involved this giant criminal robot network you might think you should go after that guy in the center. That would be an example of exploiting a structure.
### Problem
	![[Pasted image 20240121195903.png]]
- Extreme case: independent subproblems
    - Example: Tasmania (T) and mainland do not interact (see figure)
- Independent subproblems are identifiable as connected components of constraint graph
- Suppose a graph of n variables can be broken into subproblems of only c variables:
    - Worst-case solution cost is $O((n/c)(d^c))$, linear in n
    - E.g., n = 80, d = 2, c =20
    - 2⁸⁰ = 4 billion years at 10 million nodes/sec
    - (4)(2²⁰) = 0.4 seconds at 10 million nodes/sec
### Tree-structured CSPs
	![[Pasted image 20240121200237.png]]
- It is a theorem that if the constraint graph has no loops then the CSP can be solved in time that is linear in the size of graph and quadratic in the size of domains. That's so much better than general CSPs worst exponential.

- Theorem: if the constraint graph has no loops, the CSP can be solved in O(n·d²) time
    - Compare to general CSPs, where worst-case time is O(dⁿ)
- This property also applies to probabilistic reasoning (later):
    - An example of the relation between syntactic restrictions and the complexity of reasoning

- Algorithm for solving a tree-structured CSPs:
	- Order: Choose a root variable, order variables so that parents precede children.
	![[Pasted image 20240121200539.png]]
	- Remove backward: For i := n to 2, apply RemoveInconsistent(Parent(Xᵢ),Xᵢ)
		- Once you've ordered it, we do a backwards path.
		- We start at F, and we go leftward. And for each node in this pass, we are going to make the arc which pointing to that node consistent.
	- Assign forward: For i = 1 : n, assign X i consistently with Parent(Xᵢ)

- Runtime O(n·d²)
	- The “Remove backward” step takes O(d²) time for each of the n nodes in the tree (since each arc can be made consistent in O(d²) time), and the “Assign forward” step takes O(d) time for each node. 
	- Since we have n nodes, this n(d² + d), so O(n·d²)

- **Claim 1:** After backward pass, all root-to-leaf arcs are consistent
- **Proof:** Each X→Y was made consistent at one point and Y’s domain could not have been reduced thereafter (because Y’s children were processed before Y)
	![[Pasted image 20240121201209.png]]
- **Claim 2:** If root-to-leaf arcs are consistent, forward assignment will not backtrack 
- **Proof:** Induction on position
- Why doesn’t this algorithm work with cycles in the constraint graph?
	- The tree-structured CSP algorithm assumes a tree-like structure with no cycles. It orders variables so parents precede children and enforces arc consistency in one pass. If there are cycles, these assumptions fail, making the algorithm ineffective. For graphs with cycles, other algorithms like backtracking or local search are used.
- Note: we’ll see this basic idea again with Bayes’ nets
### Improving Structure
	![[Pasted image 20240121201845.png]]
So we can use this great algorithm on tree-structured CSP, but CSP is probably not tree-structured either. So we need some way of taking graphs which are not in these wonderful configurations, but or maybe closer.
#### Nearly Tree-Structured CSPs
	![[Pasted image 20240121202153.png]]
- We are going to assign a value to it . Once we've assigned a value to it and we imagine that that value we assigned to SA is fixed. The rest of the arcs connected to SA can now be "forgotten". (Conditioning)
- Conditioning: instantiate a variable, prune its neighbors' domains
#### Cutset Conditioning
#### Tree Decomposition*
## Iterative Improvement
![[Pasted image 20240121192947.png]]
## Performance of Min-Conflicts
## Local search
### Hill climbing
### Simulated Annealing
### Genetic Algorithms
---
# Lecture 3
---
# Lecture 4
---
# Lecture 5
---
# Lecture 6
---
# Lecture 7
---
# Lecture 8
---
# Lecture 9
---
# Lecture 10
---

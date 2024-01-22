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
# Lecture 2 CSP
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
- Cutset conditioning: instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree.
- Cutset size c gives runtime O( (dc ) (n-c) d2 ), very fast for small c
#### Cutset Conditioning
	![[Pasted image 20240121202506.png]]
- Finding smallest cut-set is np-hard !
#### Tree Decomposition*
Tree Decomposition is another approach :
- Idea: create a tree-structured graph of mega-variables
- Each mega-variable encodes part of the original CSP
- Subproblems overlap to ensure consistent solutions
	![[Pasted image 20240121202644.png]]
## Iterative Improvement
![[Pasted image 20240121192947.png]]
### For CSPs
- Iterative Algorithms for CSPs is our first example of a local search.
- Local search methods typically work with **“complete”** states, i.e., all variables assigned
- To apply to CSPs:
    1. Algorithm starts by assigning some value to each of the variables
        - Ignoring the constraints when doing so
    2. Take an assignment with unsatisfied constraints
    3. Operators reassign variable values
		![[Pasted image 20240121202952.png]]
    - No fringe! Live on the edge.
        - There is no backup plan, like the queue in search problem.
- Algorithm: While not solved, while at least one constraint is violated, repeat:
    - Variable selection:
        - randomly select any conflicted variable
    - Value selection: min-conflicts heuristic:
        - Choose a value that violates the fewest constraints (among all possible selections of values in its domain)
        - I.e., hill climb with h(n) = total number of violated constraints
- Questions
    - Do you risk introducing a new conflict? Yes
    - Can this thing run forever? Yes
    - Will it give you an optimal solution if there are waits? No.
    - Do you have any guarantee whatever? No
    - **BUT** it's very fast very often.
### Performance of Min-Conflicts
- Given random initial state, can solve n-queens in almost constant time for arbitrary n with high probability (e.g., n = 10,000,000)!
- The same appears to be true for any randomly-generated CSP except in a narrow range of the ratio.
	![[Pasted image 20240121204807.png]]
- Looking at the graph, having allot of constraints and minimum constraints are both great. This is because having allot of constraints will make it easier to find the solution, while having as little as possible gives us more freedom.
- As u can see, there is a critical ratio, where the amount of constraints / amount of variables result in a high CPU time.
## Summary: CSPs
- CSPs are a special kind of search problem:
    - States are partial assignments
    - Goal test defined by constraints
- Basic solution: backtracking search
- Speed-ups:
    - Ordering
    - Filtering
    - Structure
- _**Iterative min-conflicts is often effective in practice**_
    - though, you have almost no guarantees.
## Local search
	![[Pasted image 20240121205239.png]]]
- Tree search keeps unexplored alternatives on the fringe (ensures completeness)
- Local search: improve a single option until you can’t make it better (no fringe!)
    - In local search you don't have the safety net. You got one position that you are currently at and you're trying to hill climb in some way.
- New successor function: local changes
	- You have a new idea of a successor function. The successor function now does not take a plan and extend the plan, instead it takes a complete assignment of some kind and modifies it. Your successor function is more about modification than about extension.
	![[Pasted image 20240121205521.png]]
- Generally much faster and more memory efficient (but incomplete and suboptimal)
### Hill climbing
- Simple, general idea:
    - Start wherever
    - Repeat: move to the best neighboring state
    - If no neighbors better than current, quit
- What’s bad about this approach?
    - Complete ? No.
    - Optimal ? No.
    - may reach local maximum.
- What’s good about it?
    - you can start anywhere you can do the best you can and there are a wide range of problems in the real world where kind of any solution will work, and you'd like to make it as good as possible and you know you can't get to the optimal solution.
	![[Pasted image 20240121210004.png]]
### Simulated Annealing
- Idea: Escape local maxima by allowing downhill moves  But make them rarer as time goes on
	![[Pasted image 20240121210046.png]]
- Theoretical guarantee: 
	- Stationary distribution: ![[Pasted image 20240121210256.png]]
	- If T decreased slowly enough, will converge to optimal state!
- Is this an interesting guarantee?
	- So, while SA increases the likelihood of finding the global maximum compared to hill climbing, it does not provide an absolute guarantee. It does, however, offer a good balance between exploration and exploitation, making it a valuable tool in optimization problems.
- Sounds like magic, but reality is reality: 
	- The more downhill steps you need to escape a local optimum, the less likely you are to ever make them all in a row.
	- People think hard about ridge operators which let you jump around the space in better way.
## Genetic Algorithms
Genetic algorithms are kind of local search in this case not one hypothesis but a bunch of hypothesis and rather than just locally improving all of them, it is just mutation.

You keep the best hypotheses at each step. In addition to just keeping the best one, you find pairs and you do cross-over, you made them (2 robots -> big robot )
	![[Pasted image 20240121210817.png]]
	![[Pasted image 20240121210830.png]]
- Genetic algorithms use a natural selection metaphor
    - Keep best N hypotheses at each step (selection) based on a fitness function
    - Also have pairwise crossover operators, with optional mutation to give variety
- Possibly the most misunderstood, misapplied (and even maligned) technique around
### Example
![[Pasted image 20240121210942.png]]
I have 2 pretty good n-queen solutions. Neither is actually a solution. They both have a small number of conflicts.

So I'm going to slice my board down the middle, and I'm going to take part of a and part of b, and slam them together.

Why does this make sense ?

This is an example of not just nudging your thing locally, but just taking entirely different ways of traversing the space.

---
# Lecture 3 Adversarial Search
## Types of games
- Many different kinds of games

- Axes
    - Deterministic or stochastic?
    - One, two, or more players?
    - Zero sum?
    - Perfect information (can you see the state)?

We will talk about zero sum and deterministic games. They are games of perfect information.

Think about how this is different from search.

In search I gave you the search problem, and what you gave me back is a plan or path it is a sequences of actions that executed and it was guaranteed to succeed.

That's not going to work here because we don't control our opponent. So we can't just give a plan that guarantes to succeed. What we need to do is we need a function which tells us in any given state what to do. That is the **policy** in the game case it's often called strategy.
### Deterministic Games
- Many possible formalizations, one is:
    - States: S (start at s₀)
    - Players: P={1...N} (usually take turns)
        - Defines which player has the move in a state.
    - Actions: A (may depend on player / state)
        - Returns the set of legal moves in a state.
    - Transition Function: SxA → S
        - The result of a move depending on the given state.
    - Terminal Test: S →{t,f}
        - Which is true when the game is over and false otherwise.
        - States where the game has ended are called _**terminal states**_ .
    - Terminal Utilities: SxP → R
        - Every outcome of the game will be scored.
        - Defines the final numeric value for a game that ends in terminal state _**s**_ for a player _**p**_
        - This tell us for an end-state how much it is worth to each of the players.
        - In chess, the outcome is a win, draw, or loss, with values +1, 0, or -1
- Solution for a player is a **policy**: S → A
    - the solution to a game like this is a policy which map states to actions.
### Zero-Sum Games
|Zero-Sum Games|General Games|
|---|---|
|Agents have opposite utilities (values on outcomes)|Agents have independent utilities (values on outcomes)|
|Lets us think of a single value that one maximizes and the other minimizes|Cooperation, indifference, competition, and more are all possible|
|Adversarial, pure competition|More later on non-zero-sum games|
## Adversarial Search
	![[Pasted image 20240121230436.png]]
So instead of just taking actions with no consideration to the opponent, we will now make decisions based on what our opponent might or might not do.

So for instance, if we look at the example of Pacman, we might need to consider what the ghost will do in case we take this direction of movement.
### Single-Agent Trees
	![[Pasted image 20240121230814.png]]
So when we look at a single agent, we can see that different movement leads to different outcomes of values. 

What we want is the value 8, so for our agent we want the best possible outcome, and in this case it is the maximum.
	![[Pasted image 20240121231055.png]]
### Adversarial Game trees
	![[Pasted image 20240121231123.png]]
But what if we have more than one agent, this we will be a tad bit complexer, because now we can't just move to our pellet just recklessly. 

And how do we decide on how the opponent should move. So if our values are based on our movement, than the best possible move for the opponent is when the value of the state for us is the worst. So in other words the minimum of the states.
#### Minimax values
	![[Pasted image 20240121231454.png]]
Here we can see a combination of us making a move and then the opponent making a move.
### Example Tic-Tac-Toe Game
	![[Pasted image 20240121231603.png]]
### Adversarial Search (Minimax)
- Deterministic, zero-sum games:
    - Tic-tac-toe, chess, checkers
    - One player maximizes result
    - The other minimizes result

- Minimax search:
    - A state-space search tree
    - Players alternate turns
    - Compute each node’s minimax value: the best achievable utility against a rational (optimal) adversary

	![[Pasted image 20240121231656.png]]
#### Pseudocode
```python
def value(state):
    if the state is a terminal state: return the state’s utility
    if the next agent is MAX: return max-value(state)
    if the next agent is MIN: return min-value(state)
```
	![[Pasted image 20240121231739.png]]
#### Properties
	![[Pasted image 20240121232214.png]]
If you play against a perfect player you want to use minimax but if you are not playing against a player move random then minimax is going to be overly pessimistic. And so, if just periodically they were to make a mistake, it's worth going the right way ( 9-100 ). So now we're doing some probability calculation really. It's like what's the chances that they might make a mistake.
#### Efficiency
- How efficient is minimax?
    - Just like (exhaustive) DFS
    - Time: O(bᵐ)
    - Space: O(bm)

- Example: For chess, b≈35, m≈100
    - Exact solution is completely infeasible
    - But, do we need to explore the whole tree?
## Game Tree Pruning
	![[Pasted image 20240121232650.png]]
We will do some pruning because not all values are relevant in case we already found the minimum or maximum of the layer. So calculating different branches is not needed anymore.
### Example
	![[Pasted image 20240121232840.png]]
For the second branch (2-4-6), we need to look at the minimum of these values. We can already see that 2 is the minimum and branch 4 and 6, don't need to be explored further.
	![[Pasted image 20240121232953.png]]
### Alpha-Beta Pruning
- General configuration (MIN version)
	- We’re computing the MIN-VALUE at some node n
	- We’re looping over n’s children
	- n’s estimate of the children's min is dropping
	- Who cares about n’s value? MAX
	- Let 'a' be the best value that MAX can get at any choice point along the current path from the root
	- If n becomes worse than a, MAX will avoid it, so we can stop considering n’s other children (it’s already bad enough that it won’t be played)
	![[Pasted image 20240121233227.png]]

- MAX version is symmetric
#### Pseudocode
- α: MAX’s best option on path to root
- β: MIN’s best option on path to root

```python
def max-value(state, α, β):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor, α, β))
        # top min-value not care what remains, if v > β
        if v > β return v  # must not prune on equality
        # update global max value
        α = max(α, v)
    return v
```

```python
def min-value(state , α, β):
    initialize v = +∞
    for each successor of state:
        v = min(v, value(successor, α, β))
        # top max-value not care what remains, if v < α
        if v < α return v # must not prune on equality
        # update global min value
        β = min(β, v)
    return v
```
#### Properties
- This pruning has no effect on minimax value computed for the root!

- Values of intermediate nodes might be wrong
	- Important: children of the root may have the wrong value
	- So the most naïve version won’t let you do action selection

- Good child ordering improves effectiveness of pruning

- With “perfect ordering”:
	- Time complexity drops to O(bm/2)
	- Doubles solvable depth!
	- Full search of, e.g. chess, is still hopeless…

- This is a simple example of **metareasoning** (computing about what to compute)

	![[Pasted image 20240121233443.png]]
## Resource Limits
	![[Pasted image 20240121232515.png]]
- Problem: In realistic games, cannot search to leaves!
- Solution: Depth-limited search
    - Instead, search only to a limited depth in the tree
    - Replace terminal utilities with an evaluation function for non-terminal positions
- Example:
    - Suppose we have 100 seconds, can explore 10K nodes / sec
    - So can check 1M nodes per move
    - α-β reaches about depth 8 – decent chess program
- Guarantee of optimal play is _**gone**_
- More plies makes a BIG difference
- Use iterative deepening for an anytime algorithm
	![[Pasted image 20240121234253.png]]
For a chess game, we can't possibly search the whole game tree. Essentially we've got resource limits in this case time. That tell us we can only look forward so far into the tree before the exponential growth of the tree gets this.

So we can only search just some limited depth from the tree. Now the problem is we get to the end of our search we don't have terminal utilities because we are not actually at the end of the game.

So we need to replace the terminal utilities in the minimax algorithm with what's called evaluation function, which takes a non-terminal position and gives us some estimate of what the terminal utility under that tree would be under minimax plan.
## Why Pacman Starves
	![[Pasted image 20240121234443.png]]
- A danger of replanning agents! 
	- He knows his score will go up by eating the dot now (west, east) 
	- He knows his score will go up just as much by eating the dot later (east, west) 
	- There are no point-scoring opportunities after eating the dot (within the horizon, two here) 
	- Therefore, waiting seems just as good as eating: he may go east, then back west in the next round of replanning!
## Evaluation Functions 
	![[Pasted image 20240121234613.png]]
A function takes a non-terminal state and return some number, just like the heuristic value in A* search.

In this case we want that number to return the actual minimax value of that position. That is not going to happen. In practice what people do is, they try to come up with some function which on average is positive when the minimax value is positive, is negative when the minimax value is negative. 
- Evaluation functions score non-terminals in depth-limited search
	![[Pasted image 20240121234952.png]]
- Ideal function: returns the actual minimax value of the position
- In practice: typically weighted linear sum of features:
    - $Eval(s) = w_1f_1(s) + w_2f_2(s) + \cdots + w_nf_n(s)$
    - eg. f₁(s)=(number white queens – number black queens), etc.
## Depth Matters
	![[Pasted image 20240121235240.png]]
- Evaluation functions are always imperfect
- The deeper in the tree the evaluation function is buried, the less the quality of the evaluation function matters
- An important example of the trade-off between complexity of features and complexity of computation
## Synergies between Evaluation Function and Alpha-Beta?
- Alpha-Beta: amount of pruning depends on expansion ordering
    - Evaluation function can provide guidance to expand most promising nodes first ( which later makes it more likely there is already a good alternative on the path to the root )
	    - somewhat similar to role of A* heuristic , CSPs filtering
- Alpha-Beta: (similar for roles of min-max swapped)
    - Value at a min-node will only keep going down
    - Once value of min-node lower than better option for max along path to root, can prune
    - Hence: If evaluation function provides upper-bound on value at min-node, and upper-bound already lower than better option for max along path to root THEN can prune.
## Uncertain Outcomes
	![[Pasted image 20240121235641.png]]
### Worst Case vs Average Case
	![[Pasted image 20240121235725.png]]
- Idea for today:
    - Uncertain outcomes controlled by chance, not an adversary!
## Expectimax Search
- Why wouldn’t we know what the result of an action will be?
    - Explicit randomness: rolling dice
    - Unpredictable opponents: the ghosts respond randomly
    - Actions can fail: when moving a robot, wheels might slip
- Values should now reflect average-case (expectimax) outcomes, not worst-case (minimax) outcomes
- Expectimax search: compute the average score under optimal play
    - Max nodes as in minimax search
    - Chance nodes are like min nodes but the outcome is uncertain
    - Calculate their expected utilities
    - I.e. take weighted average (expectation) of children
- Later, we’ll learn how to formalize the underlying uncertain-result problems as **Markov Decision Processes**
	![[Pasted image 20240121235824.png]]
### Pseudocode
```python
def value(state):
    if the state is a terminal state: return the state’s utility
    if the next agent is MAX: 
        return max-value(state)
    if the next agent is EXP: 
        return exp-value(state)
```

```python
def max-value(state):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor))
    return v
```

```python
def exp-value(state):
    initialize v = 0
    for each successor of state:
        p = probability(successor)
        v += p * value(successor)
    return v
```
	![[Pasted image 20240122000017.png]]
	v = (1/2) (8) + (1/3) (24) + (1/6) (-12) = 10
### Expectimax Pruning?
Expectimax can not apply pruning. This is because we make use of the weighted average of every node, so every node is involved.
### Depth-Limited Expectimax
![[Pasted image 20240122000234.png]]
Computing the full expectimax is computationally heavy, so we can limit it on the amount of layers we compute it on.
## Probabilities
### Reminder: Probabilities
	![[Pasted image 20240122000418.png]]
- A **random variable** represents an event whose outcome is unknown
- A **probability distribution** is an assignment of weights to outcomes

- Example: Traffic on freeway 
	- Random variable: T = whether there’s traffic 
	- Outcomes: T in {none, light, heavy} 
	- Distribution: P(T=none) = 0.25, P(T=light) = 0.50, P(T=heavy) = 0.25
	![[Pasted image 20240122000525.png]]

- Some laws of probability (more later): 
	- Probabilities are always non-negative 
	- Probabilities over all possible outcomes sum to one

- As we get more evidence, probabilities may change: 
	- P(T=heavy) = 0.25, P(T=heavy | Hour=8am) = 0.60 
	- We’ll talk about methods for reasoning and updating probabilities later
### Reminder: Expectations
- The expected value of a function of a random variable is the average, weighted by the probability distribution over outcomes.
	![[Pasted image 20240122000757.png]]
- Example: How long to get to an airport?
	![[Pasted image 20240122000842.png]]
### What probabilities to use?
- In expectimax search, we have a probabilistic model of how the opponent (or environment) will behave in any state
    - Model could be a simple uniform distribution (roll a die)
    - Model could be sophisticated and require a great deal of computation
    - We have a chance node for any outcome out of our control: opponent or environment
    - The model might say that adversarial actions are likely!
- For now, assume each chance node magically comes along with probabilities that specify the distribution over its outcomes
	![[Pasted image 20240122001000.png]]
One important thing to remember is that just because we assign probabilities that reflect our believes to the outcome, that does not mean that the thing on the other side of flipping a coin.

If I think there is a 20% chance that the ghost go to left , it doesn't mean that the ghost has a random number generator. It just means that given my model which may be a simplification that's the best I can say given my evidence.
### Quiz: Informed Probabilities
- Let’s say you know that your opponent is actually running a depth 2 minimax, using the result 80% of the time, and moving randomly otherwise
- Question: What tree search should you use?
- Answer: Expectimax!
    - To figure out EACH chance node’s probabilities, you have to run a simulation of your opponent
    - This kind of thing gets very slow very quickly
    - Even worse if you have to simulate your opponent simulating you…
    - … except for minimax, which has the nice property that it all collapses into one game tree

In general expectimax is the more general search procedures. You should always in principle use expectimax
## Modelling Assumptions
	![[Pasted image 20240122001500.png]]
### The Dangers of Optimism and Pessimism
|Dangerous Optimism|Dangerous Pessimism|
|:--|--:|
|Assuming chance when the world is adversarial.  |Assuming the worst case when it’s not likely.|
|![[Pasted image 20240122001540.png]] |![[Pasted image 20240122001608.png]] |
### Assumptions vs. Reality
	![[Pasted image 20240122001718.png]]
- Pacman used depth 4 search with an eval function that avoids trouble
- Ghost used depth 2 search with an eval function that seeks Pacman
## Other Game Types
	![[Pasted image 20240122001826.png]]
### Mixed Layer Types
- E.g. Backgammon
- Expectiminimax
    - Environment is an extra “random agent” player that moves after each min/max agent
    - Each node computes the appropriate combination of its children
	![[Pasted image 20240122001857.png]]
### Multi-Agent Utilities
- What if the game is not zero-sum, or has multiple players?
- Generalization of minimax:
    - Terminals have utility tuples
    - Node values are also utility tuples
    - Each player maximizes its own component
    - Can give rise to cooperation and competition dynamically…
	![[Pasted image 20240122002039.png]]
Each player has its own value of terminal node, and will optimize for their own outcome. Minimax , we kind of have that too. The maximizer had the number that we were showing, and the minimizer had the negative of that number. So there were actually 2 numbers sitting there, but it was the negative of each other, so we only showed one. Minimax is a special case of this where we just collapse those 2 opposite numbers into one number that we display.

The leaf utilities are now written as pairs (UA , UB, UC ). In this generalized setting, A seeks to maximize UA, the first component, while B seeks to maximize UB , the second component.

In above example, the leftmost green node should be: _**(1,6,6)**_

Different things can emerge here, though these numbers are not just complementary to each other. In the left sub tree, blue prefer to 6, can they make that happen? What will green do ? Green will choose the (1,6,6), which will happen that blue also gets 6 and gets what they want. So what we have here is actually a collaboration between blue and green.

---
# Lecture 4 Bayes' Nets
> Bayes' Nets, also known as graphical models, which are a technique for building probabilistic models over large numbers of random variables, in a way that is efficient to specify and efficient to reason over.
>
>The development of AI stop in 80s because the difficulty of uncertainty. You can not compute such a large joint probability table with thousands variable.
>
>Bayes' Nets wil give us a way to deal with distributions of our large sets of random variable in a meaningful way

	![[Pasted image 20240122002334.png]]
## Probabilistic Models
- Models describe how (a portion of) the world works
- **Models are always simplifications**
    - May not account for every variable
    - May not account for all interactions between variables
    - “All models are wrong; but some are useful.”  – George E. P. Box
- What do we do with probabilistic models?
    - We (or our agents) need to reason about unknown variables, given evidence
    - Example: explanation (diagnostic reasoning)
    - Example: prediction (causal reasoning)
    - Example: value of information
## Independence
	![[Pasted image 20240122123030.png]]
- Two variables are independent if:
	- $\forall x,y : P(x,y) = P(x)P(y)$.
	- This says that their joint distribution factors into a product two simpler distributions.
	- Another form:
		- $\forall x,y : P(x|y) = P(x)$
		- This implies: the probability of x knowing y, is the probability of x. So knowing y doesn't change what the probability is over x.
	- We write this as:
		- $X \mathrel{\unicode{x2AEB}} Y$ 
- Independence is a simplifying modelling assumption
	- Empirical joint distributions: at best “close” to independent
### Conditional Independence
	![[Pasted image 20240122123814.png]]
- P(Toothache, Cavity, Catch)
- If I have a cavity, the probability that the probe catches in it doesn't depend on whether I have a toothache: 
	- P(+catch | +toothache, +cavity) = P(+catch | +cavity)
- The same independence holds if I don’t have a cavity:
	- P(+catch | +toothache, -cavity) = P(+catch| -cavity)
- Catch is conditionally independent of Toothache given Cavity: 
	- P(Catch | Toothache, Cavity) = P(Catch | Cavity)
- Equivalent statements: 
	- P(Toothache | Catch , Cavity) = P(Toothache | Cavity) 
	- P(Toothache, Catch | Cavity) = P(Toothache | Cavity) P(Catch | Cavity) 
	- One can be derived from the other easily

- Unconditional (absolute) independence very rare (why?)
	- Unconditional independence is rare because most systems are complex with interrelated events. Conditional independence is more common because it allows for the possibility of relationships among events under certain conditions. It’s important to note that independence does not imply conditional independence, and vice versa.
- Conditional independence is our most basic and robust form of knowledge about uncertain environments.
- X is conditionally independent of Y given Z: $X \mathrel{\unicode{x2AEB}} Y  | Z$.
	- if and only if: 
		- $\forall x, y, z : P(x,y|z) = P(x|z) P(y|z)$
	- or, equivalent, if and only if:
		- $\forall x, y, z : P(x|z, y) = P(x|z)$
#### Examples
- What about this domain:
	- Traffic 
	- Umbrella 
	- Raining
	![[Pasted image 20240122125529.png]]
We can see clearly from the graphic that rain causes both traffic and umbrellas. Therefore, traffic must be conditionally independent from umbrellas given that it's raining. More intuitively speaking, once we know it's raining the probability that there is traffic does not depend on whether people are walking around with umbrellas.

- What about this domain:
	- Fire
	- Smoke
	- Alarm
	![[Pasted image 20240122125602.png]]
In this, we see that fire causes smoke which triggers the alarm. We can say that the alarm going off is conditionally independent of the fire given that there is smoke. In other words, if we know that there is smoke, whether or not that the smoke came from the fire does not affect the probability that the alarm will go off.
#### Chain rule
- Chain rule: $P(X_1, X_2, \cdots , X_n) = P(X_1)P(X_2 | X_1)P(X_3|X_2, X_1) \cdots$
- Trivial decomposition:
	- $P(Traffic, Rain, Umbrella) = P(Rain)P(Traffic|Rain)P(Umbrella|Rain,Traffic)$
- With assumption of conditional independence:
	- $P(Traffic, Rain, Umbrella) = P(Rain)P(Traffic|Rain)P(Umbrella|Rain)$
- Bayes’nets / graphical models help us express conditional independence assumptions
##### Example
	![[Pasted image 20240122130223.png]]![[Pasted image 20240122130304.png]]
In this case ,there are just 2 locations for the ghost , top or bottom.
So you could have a measurement on each of these squares so each of them could give you a red measurement or not a red measurement, so those are 2 random variables. The ghost's location is another random variable , whether it is being in the top .
- Each sensor depends only on where the ghost is
- That means, the two sensors are conditionally independent, given the ghost position
	- T: Top square is red:
    - B: Bottom square is red:
    - G: Ghost is in the top
- Givens:
    - P(+g) = 0.5
    - P(-g) = 0.5
    - P(+t | +g) = 0.8
    - P(+t | -g) = 0.4
    - P(+b | +g) = 0.4
    - P(+b | -g) = 0.8
- In general it is not enough to specify a full joint distribution
- But if we're willing to assume the 2 sensor are independent given where the ghost is , then this is enough.
    - P(G,B,T) = P(G)P(T|G)P(B|G)
	![[Pasted image 20240122130624.png]]
## Bayes' Nets: Big Picture
	![[Pasted image 20240122130653.png]]
It's a new way of representing joint distributions. It's very closely related to the chain rule.

We've always talked about discrete random variables, and then a distribution can be a table. If you have continuous random variables then the way to represent the distribution is commonly done using a probability density function, which effectively encodes how much probability mass is associated with each interval if it's a 1D distribution, or each volume in space was probability of landing in a certain volume of space. It turns out if you had continuous random variables you can still use Bayes Nets, and the conditional distributions that you'd be working with would then be conditional distributions that are densities rather than the discrete distributions.

- Two problems with using full joint distribution tables as our probabilistic models:
    - Unless there are only a few variables, the joint is WAY too big to represent explicitly
    - Hard to learn (estimate) anything empirically about more than a few variables at a time
- **Bayes’ nets:** a technique for describing complex joint distributions (models) using simple, local distributions (conditional probabilities)
    - More properly called **graphical models**
    - We describe how variables locally interact
    - Local interactions chain together to give global, indirect interactions
    - For about 10 min, we’ll be vague about how these interactions are specified
    ![[Pasted image 20240122130957.png]]
### Examples
#### Insurance
	![[Pasted image 20240122131026.png]]
- 27 variables
    - assuming they are binary
- 2²⁷ ≈ 134M entries
- Difficult to estimate the relationships between all variables
#### Car
	![[Pasted image 20240122131035.png]]
### Graphical Model Notation
- Nodes: variables (with domains)
	- Can be assigned (observed) or unassigned (unobserved)
    - Often the ones that are assigned we shade in with gray
- Arcs: interactions
    - Similar to CSP constraints
    - Indicate “direct influence” between variables
    - Formally: encode conditional independence (more later)
- For now: imagine that arrows mean direct causation (in general, they don’t!)
    - it's often true, but it doesn't have to be true.
	![[Pasted image 20240122132228.png]]
#### Examples
##### Coin flips
- N independent coin flips
	![[Pasted image 20240122132353.png]]![[Pasted image 20240122132359.png]]
- No interactions between variables: **absolute independence**
##### Traffic
- Variables:
    - R: It rains
    - T: There is traffic
- Model 1: independence 
	![[Pasted image 20240122132523.png]]
- Model 2: rain causes traffic
    ![[Pasted image 20240122132533.png]]
- In general model 2 is better, because we have an relationship. Relationships help with knowing what impact a certain variable has on an other variable.
##### Traffic 2
- Variables
    - T: Traffic
    - R: It rains
    - L: Low pressure
    - D: Roof drips
    - B: Ballgame
    - C: Cavity
	![[Pasted image 20240122132720.png]]
	![[Pasted image 20240122133013.png]]
A model is a representation of some thought a person has depending on the variables, so a different model could be valid depending on the reasoning.
## Bayes' Net Semantics
	![[Pasted image 20240122133134.png]]
For a given Bayes' Net, what does it mean? What joint probability distribution does it encode? How do we know that?

- A set of nodes, one per variable X
- A directed, acyclic graph
- A conditional distribution for each node
	![[Pasted image 20240122133221.png]]
	- A collection of distributions over X, one for each combination of parents’ values
	    - $P(X|a_1,\cdots,a_n)$
	- CPT: conditional probability table
	- Description of a noisy “causal” process
	    - E.g. if it rains, then there's 90% probability of traffic, if it doesn't rain, there's a 30% probability of traffic.
	    - This is not part of the definition
- **A Bayes net = Topology (graph) + Local Conditional Probabilities**.
	- A graph, plus all the little local conditional probabilities that live inside the node
### Probabilities in BNs
- Bayes’ nets _**implicitly**_ encode joint distributions
    - As a product of local conditional distributions
    - To see what probability a BN gives to a full assignment, multiply all the relevant conditionals together:
        - $P(x_1, x_2, \cdots , x_n) = \prod_{i=1}^n P(x_i|parents(X_i))$
    - Example
        ![[Pasted image 20240122133555.png]]
        -  P(+cavity, +catch, -toothache) = P(+cavity)·P(-toothache|+cavity)·P(+catch|+cavity)
- Why are we guaranteed that setting $P(x_1, x_2, \cdots , x_n) = \prod_{i=1}^n P(x_i|parents(X_i))$ results in a proper joint distribution?
	- Chain rule (valid for all distributions):  $P(x_1, x_2, \cdots , x_n) = \prod_{i=1}^n P(x_i|x_1, \cdots , x_{i-1})$ 
	- Assume conditional independences: $P(x_i, \cdots , x_{i-1}) = P(x_i|parents(X_i))$ 
		- Then consequence: $P(x_1, x_2, \cdots , x_n) = \prod_{i=1}^n P(x_i|parents(X_i))$
- Not every BN can represent every joint distribution
	- The topology enforces certain conditional independencies
#### Examples
##### Alarm Network
	![[Pasted image 20240122134759.png]]
##### Traffic
	![[Pasted image 20240122134822.png]]
##### Reverse Traffic
	![[Pasted image 20240122134843.png]]
This network here, which does not match the causal process, encodes the exact same joint distribution over those variables as the previous one. Now you might like the previous one better and there's a lot of advantages to drawing these things causally, but mathematically, it is just an expansion of the chain rule.
### Causality?
- When Bayes’ nets reflect the true causal patterns:
	- Often simpler (nodes have fewer parents)
		- OFTEN we choose them to be causal, and the reason we choose to be causal is that you'll end up with fewer parents.
	- Often easier to think about
	- Often easier to elicit from experts
		- $P(Traffic|Rain)$ is easy to get rather than $P(Rain|Traffic)$
	![[Pasted image 20240122135458.png]]

- BNs need not actually be causal
	- Sometimes no causal net exists over the domain (especially if variables are missing)
	- E.g. consider the variables Traffic and Drips
		- you don't care about Raining any more
		- T→D may be a reasonable choice, also D→R may be a reasonable choice. but both of them are not causal.
	- End up with arrows that reflect correlation, not causation

- What do the arrows really mean?
	- Topology may happen to encode causal structure
	- **Topology really encodes conditional independence**
		- $P(x_i, \cdots , x_{i-1}) = P(x_i|parents(X_i))$ 
## Bayes' Nets
- So far: how a Bayes’ net encodes a joint distribution
- Next: how to answer queries about that distribution
    - Today:
        - First assembled BNs using an intuitive notion of conditional independence as causality
        - Then saw that key property is conditional independence
    - Main goal: answer queries about conditional independence and influence
- After that: how to answer numerical queries (inference)
	![[Pasted image 20240122135445.png]]

> Start of part two Bayes' Nets: Independence

## Size of a Bayes' Net
- How big is a joint distribution over N Boolean variables?
	- $2^N$
- How big is an N-node net if nodes have up to k parents?
	- $O(N * 2^{k+1})$
- Both give you the power to calculate
	- $P(X_1, X_2, \cdots, X_n)$
- BNs: Huge space savings!
- Also easier to elicit local CPTs
- Also faster to answer queries (coming)
## D-separation: Outline
- Study independence properties for triples
- Analyse complex cases in terms of member triples
- D-separation: a condition / algorithm for answering such queries
### Causal Chains
- This configuration is a "causal chain"
	![[Pasted image 20240122153611.png]]
- $P(x, y, z) = P(x)P(y|x)P(z|y)$

- Guaranteed X independent of Z ? **NO**
	- One example set of CPTs for which X is not independent of Z is sufficient to show this independence is not guaranteed.
	- Example:
		- Low pressure causes rain causes traffic, high pressure causes no rain causes no traffic.
		- In numbers:
			- $P( +y | +x ) = 1, P( -y | - x ) = 1$
			- $P( +z | +y ) = 1, P( -z | -y ) = 1$

- Guaranteed X independent of Z given Y?
	- $P(z|x,y) = \dfrac{P(x,y,z)}{P(x,y)}$
	- $= \dfrac{P(x)P(y|x)P(z|y)}{P(x)P(y|x)}$
	- $= P(z|y)$
	- So **YES**

- **Evidence along the chain "blocks" the influence**
### Common Cause
- This configuration is a "common cause"
	![[Pasted image 20240122155932.png]]
- $P(x, y, z) = P(y)P(x|y)P(z|y)$

- Guaranteed X independent of Z ? **NO**
	- One example set of CPTs for which X is not independent of Z is sufficient to show this independence is not guaranteed.
	- Example:
		- Project due causes both forums busy and lab full
		- In numbers:
			- $P( +x | +y ) = 1, P( -x | -y ) = 1$,
			- $P( +z | +y ) = 1, P( -z | -y ) = 1$

- Guaranteed X and Z independent given Y?
	-  $P(z|x,y) = \dfrac{P(x,y,z)}{P(x,y)}$
	- $= \dfrac{P(y)P(x|y)P(z|y)}{P(y)P(x|y)}$
	- $= P(z|y)$
	- So **YES**

- **Observing the cause blocks influence between effects.**
### Common Effect
- Last configuration: two causes of one effect (v-structures)
	![[Pasted image 20240122160334.png]]

- Are X and Y independent?
	- **YES**: the ballgame and the rain cause traffic, but they are not correlated
		- $P(X,Y,Z) = P(X)P(Y)P(Z∣X,Y)$
		- and $P(X,Y | Z) = \dfrac{P(X,Y,Z)}{P(Z)}$
		- Then if we combine them, $P(X,Y | Z) = \dfrac{P(X)P(Y)P(Z ∣ X,Y)}{P(Z)}$
		- Z is conditionally independent of X and Y so $P(Z ∣ X,Y) = P(Z)$
		- So $P(X,Y | Z) = \dfrac{P(X)P(Y)P(Z)}{P(Z)} = P(X)P(Z)$

- Are X and Y independent given Z?
	- **NO**: seeing traffic puts the rain and the ballgame in competition as explanation.

- **This is backwards from the other cases**
	- Observing an effect **activates** influence between possible causes.
## The General Case
	![[Pasted image 20240122161443.png]]
- General question: in a given BN, are two variables independent (given evidence)?
- Solution: analyse the graph
- Any complex example can be broken into repetitions of the three canonical cases
	![[Pasted image 20240122161525.png]]
### Reachability
- Recipe: shade evidence nodes, look for paths in the resulting graph
- Attempt 1: if two nodes are connected by an undirected path not blocked by a shaded node, they are conditionally independent
- Almost works, but not quite
	- Where does it break?
		- Answer: the v-structure at T doesn’t count as a link in a path unless “active
	![[Pasted image 20240122161636.png]]
### Active / Inactive Paths
- Question: Are X and Y conditionally independent given evidence variables {Z}? 
	- Yes, if X and Y "d-separated" by Z 
	- Consider all (undirected) paths from X to Y 
	- No active paths = independence!

- A path is active if each triple is active:
	- Causal chain A -> B -> C where B is unobserved (either direction)
	- Common cause A <- B -> C where B is unobserved 
	- Common effect (aka v-structure) A -> B <- C where B or one of its *descendants* is observed

- All it takes to block a path is a single inactive segment
	![[Pasted image 20240122162025.png]]
### D-Separation
- Query: $X_i \mathrel{\unicode{x2AEB}} X_j | \{X_{k1}, \cdots, X_{kn}\}$?
- Check all (undirected!) paths between $X_i$ and $X_j$
	- If one or more active, then independence not guaranteed
		- $X_i \not\!\perp\!\!\!\perp X_j | \{X_{k1}, \cdots, X_{kn}\}$
	- Otherwise (i.e. if all paths are inactive), then independence is guaranteed
		- $X_i \mathrel{\unicode{x2AEB}} X_j | \{X_{k1}, \cdots, X_{kn}\}$
	![[Pasted image 20240122162628.png]]
#### Example
	![[Pasted image 20240122162915.png]]
### Structure Implications
	![[Pasted image 20240122163040.png]]
- Given a Bayes net structure, can run d- separation algorithm to build a complete list of conditional independences that are necessarily true of the form
	- $X_i \mathrel{\unicode{x2AEB}} X_j | \{X_{k1}, \cdots, X_{kn}\}$
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

# Upper-Bound-for-Sorting-Permutations-UsingTransposition-Tree

## Abstract
Transforming permutations with several operations has been extensively studied where a transposition tree is one such operation. Such transformations have applications in genetics and interconnection networks. In genomic studies, a permutation models a genome. Likewise, in computer interconnection networks it denotes a node. A transposition tree T = (VT , ET ) is a spanning tree over its vertices. In literature, Sn denotes the symmetric group formed by n symbols. A move of T on a permutation π ∈ Sn corresponds to any of e ∈ ET . If e = (i, j), then applying e to π swaps the symbols in positions i and j. The number of moves that suffice to sort any permutation in Sn with a given T is an upper bound for T. A precise upper bound equals the diameter of the corresponding Cayley graph Γ, i.e. diam(Γ). Jerrum showed that, in general, it is intractable to compute the diameter if the number of generators is at least two. Thus, computing a tighter upper bound is of both theoretical ad practical interest. We propose algorithms to identify upper bounds and exact upper bounds for sorting permutations with various classes of trees.


<img width="515" alt="Screenshot 2023-07-18 at 10 44 31 AM" src="https://github.com/Arunodhai/Upper-Bound-for-Sorting-Permutations-UsingTransposition-Tree/assets/60264218/f6507f49-31b2-41b4-94d1-9ed8ee4db25e">
<img width="516" alt="Screenshot 2023-07-18 at 10 44 49 AM" src="https://github.com/Arunodhai/Upper-Bound-for-Sorting-Permutations-UsingTransposition-Tree/assets/60264218/0ae72656-2501-4f15-a985-0afa45f79538">

## Result and Analysis
<img width="445" alt="Screenshot 2023-07-18 at 10 43 49 AM" src="https://github.com/Arunodhai/Upper-Bound-for-Sorting-Permutations-UsingTransposition-Tree/assets/60264218/e5b1fd1c-81de-41a9-90c2-5ca5dc080a50">

## Conclusion
We compared the upper bound values for all full binary trees of sizes up to n = 255. It was theoretically demonstrated that δ* is actually tighter than δ’, β, and γ for a full binary tree. We implemented the algorithms and practically proved that δ* is indeed tighter than δ’, β, and γ for a full binary tree. The execution results are shown in Table 1.

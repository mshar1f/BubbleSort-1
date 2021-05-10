# Takes in a list
# Loops over the list, in the first pass it swaps adjacent indexes and checks if theyre unordered.
# If theyre unordered it swaps them. This continues until it does n passes
 # Improved version. it swaps until list is sorted.

lst = [48,
32,
40,	
13,
78,
99,	
23,	
26,	
75,	
16,
27,	
29,	
41,	
42,	
27,
74,	
55,	
6,	
15,	
26,
9,	
95,	
32,	
19,	
36,
68,	
58,	
80,	
80,	
43,
100,	
100,	
20,	
49,	
53,
51,	
91,	
82,	
7,	
96,
6,	
47,	
64,	
49,	
18,
8,	
1,	
29,	
46,	
3,
25,	
54,	
57,	
24,	
22,
54,	
30,	
28,	
3,	
59,
85,	
1,	
7,	
99,	
60,
27,	
72,	
90,	
31,	
90,
100,	
24,	
50,	
16,	
41,
12,	
33,	
15,	
68,	
90,
87,	
98,	
42,	
21,	
73,
72,	
46,	
1,	
13,	
75,
19,	
11,	
40,	
61,	
19,
91,	
84,	
14,	50,	99,]

# Slow version 

def bubblesort_first(lst):
    for x in range(len(lst)-2):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst
from time import perf_counter
start = perf_counter()
print(bubblesort_first(lst))
end = perf_counter()
print(end-start)



def bubble_sort_improved(lst):

        noSwap = True
        wh
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                noSwap= False
        if noSwap == True:
            return lst
    return lst
start = perf_counter()
print(bubble_sort_improved(lst))
end = perf_counter()
print(end-start)
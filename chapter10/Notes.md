# Algo and complexity

- *"The goal of this chapter is to help you develop some general intuitions about how to approach questions of efficiency"*

- *"The key to efficiency is a good algorithm, not clever coding tricks"*

- *"Keep in mind that the most efficient algorithm is not always the algorithm of choice. A program that does everything in the most efficient possible way is often needlessly difficult to understand. It is often a good strategy to start by solving the problem at hand in the most straightforward manner possible, instrument it to find any computational bottlenecks, and then look for ways to improve the computational complexity of those parts of the program contributing to the bottlenecks"*

## Serach Algorithms

- *" search algorithm is a method for finding an item or group of items with specific properties within a collection of items. We refer to the collection of items as a **search space**. The search space might be something concrete, such as a set of electronic medical records, or something abstract, such as the set of all integers. A large number of problems that occur in practice can be formulated as search problems*"

### Linear search

- Case study: search an item within a list
  - The search is linear only if each operation inside the loop can be done in constant time
  - The time complexity of linear search is `O(n)`, where n is the length of the list. This means that the algorithm will take on average n comparisons to find the target element, if the element is equally likely to be found in any position in the list.

### Binary search

Binary search is a search algorithm that works on sorted lists. It works by repeatedly dividing the search space in half and then searching the smaller half. This process continues until the target value is found or until the search space is empty.

- Case study: search an item within a list
- A priori knowledges or hypotheses: we know the order in which items are sorted

- The time complexity of binary search is `O(log(n))`, where n is the length of the list. This means that the algorithm will take on average log n comparisons to find the target element, if the element is equally likely to be found in any position in the list.

- Binary search is a very efficient algorithm for finding an element in a sorted list. It is often used in conjunction with other algorithms, such as sorting algorithms, to make them more efficient.

## Sorting

- Most Python (soring) implementations runs in roughly `O(n*log(n))` time, where n is the length of the list (e.g., L.sort(), sorted(L), ...)

### Selection sort (notes from bard + gpt)

- Selection sort is a simple comparison-based sorting algorithm. It works by dividing the input list into two parts: the sorted part on the left and the unsorted part on the right. The algorithm repeatedly selects the smallest (or largest, depending on the sorting order) element from the unsorted part and moves it to the end of the sorted part

  - This algorithm works by first finding the smallest element in the list and swapping it with the element at the beginning of the list. Then, the algorithm repeats this process, finding the smallest element in the remaining unsorted portion of the list and swapping it with the element at the next position in the sorted list. This process continues until the entire list is sorted.

- The time complexity of selection sort is `O(n^2)`, where n is the length of the list. This is because the algorithm has to scan the entire list n times, and it has to make n - 1 comparisons each time.
  - => the alogorithme became very slow when n increases

### Merge sort

- It is a `divide and conquer` algorithm and was invented by `JOhn Von NeuMann` in 1945
- It  works by recursively dividing the list into two halves, sorting each half, and then merging the two sorted halves back together
- It has a time complexity of `O(n * log(n))`
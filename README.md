# Graph-colouring-Map-Reduce

## Project Description
In this project, we implemented graph coloring algorithm of Luby using Map-Reduce.

For this, first we learnt about the graph colouring algorithm of Luby. We searched alot, but couldnt actually find a graph colouring algorithm of luby, but instead found an algorithm of Luby to find the MIS of a graph. We used this algorithm to colour the graph.

This algorithm of luby is hard to explain over text, but basically it itterates over a graph multple times and constructs the MIS of the graph. 

What we did was use this algorithm to find the MIS of the graph, colour the nodes in this MIS with one colour, and then repeat on the graph without the nodes from the MIS. We kept doing the above, colouring the nodes everytime me make a new MIS, until no nodes were left.

## Code

### Mapper
This would take the input graph, do the algorithm to colour all the nodes, and would basically send each MIS to the reducer.

### Reducer
The reducer would take the MIS and organise it and spit it out.

## Examples
In the inputs directory, you can see inputs, along with images of the graphs they repesent.

The following is the input format

First line - contains the names of nodes (can be any unique string for each node) sperated by spaces.  For example - 
```
1 2 3 4 5
```
here, we have five nodes called 1,2,3,4,5.

The following lines contain two strings seperated by spaces, they represent the edge between the two nodes that are denoted by the strings
For example-
```
1 2
3 4
5 1
```
In our graph, there is an edge between the nodes **1 and 2**, **3 and 4**, and **1 and 5**.

The output will be of the following format
each line is of the form `index : <list of nodes>`.
each line is essentially a list of nodes that should be coloured the same colour.

for example, for the above input the output would be
```
1 : 2,5,3
2 : 1,4
```

## To run
Modify the run.sh provided with the paths to your input, your output, where you put the mapper and reducer, and run it. 
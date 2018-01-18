---
title: DBTheory Of Functional Dependency
date: 2018-01-18 11:21:44
tags: DBTheory
---
## DBTheory of Functional Dependency
### Definition of Functional Dependency
A functional dependency(FD) on a relation R is a statement of the form "If two tuples of R agree on all of the attributes A1,A2,...,An (ie. the tuples has the same values in their respective components for each of these attributes), then they must also agree on all of another list of attributes B1,B2,...,Bm"

If we can be sure every instance of a relation R will be one in which a given FD is true, then we say that R satisfies the FD. It is important to remenber that when we say that R satisfies an FD f, we are asserting a constraint on R, not just saying something about one particular instance of R.
<!--more-->

## Exercises for Section 3.1
### Exercise 3.1.1
Consider a relation about people in the United States, including their name, Social Security number, street address, city, state, ZIP code, area code, and phone number(7 digits). What FD's would you expect to hold? What are the keys for the relation? To answer this question, you need to know something about the way these numbers are assigned. For instance, can an area code straddle two states? can a ZIP code straddle two area codes? Can two people have the same Social Security number? Can they have the same address or phone number?

### Exercise 3.1.2
Consider a relation representing the present position of molecules in a closed container. The attributes are an ID for the molecule, the x, y, and z coordinates of the molecule, and its velocity in the x,y,and z dimensions. What FD's would you expect to hold? What are the keys?

### !! Exercise 3.1.3
Suppose R is a relation with attributes A1,A2,...,An. As a function of n, tell how many superkeys R has, if:
a) The only key is A1.
b) The only keys are A1 and A2.
c) The only keys are {A1,A2} and {A3,A4}
d) The only keys are {A1,A2} and {A1,A3}

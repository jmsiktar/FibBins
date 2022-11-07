# FibBins
This project is for simulations for studying compositions comprised of Fibonacci numbers and other general positive linear recurrence sequences (PLRS); 
there are currently three files. A description of each one is as follows.

PLRSFibs.py: compares the values of two different PLRS, where the inputs are the coefficients of the two sequences

countComps.py: counts the number of compositions of n, as well as the number of compositions of n using only [a subset of] the Fibonacci numbers; 
these calculations are used as tools to verify theoretical results, namely that the number of Fibonacci compositions of n where a certain number
of Fibonacci summands cannot be used can be bounded from above by standard compositions of n that don't use some small natural numbers

fibBins.py: use bisection methods to approximate roots of power series; since the power series of interest in the accompanying paper have infinitely 
many terms and are only considered on the interval (0, 1), we truncate all but the first finitely many terms of the power series, which in this case
have roots close to those of the original power series! The Lucas numbers and Fibonacci numbers appear explicitly in certain helper functions to serve
as litmus tests for how the algorithms are expected to work for general PLRS

###Accompanying preprint: https://arxiv.org/abs/2110.14478

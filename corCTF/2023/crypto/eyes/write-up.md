###Challenge: eyes
####Category: crypto
####Description: can you see it?

For this chall, I first analyzed main.sage. There were my obersvations:

1. A prime number p was picked that was 2 bits longer than the flag. It is then user to create a finite field
2. 3 matrix structures are constructed.
	a. A is an square upper traingular matrix (1024 x 1024) made of rendomized elements in the finite field.
	b. B is a column vector (1024 x 1) also made of randomized elements of the finite field.
	c. C is a scalar (1 x 1) that has only one value: the flag.
3. 2 functions are constructed:
	a. conv performs the operation x'*A*x + B'*x + C, and it returns a scalar value. (Note: ' denotes a transpose, and x represents an input vector.)
	b. fn converts the binary representation of an input number into a 1204 x 1 column vector by padding it with 0's to the left and reversing the order fo the bits.
4. For numbers one through seven, they are placed into fn() and then the resulting numbers form fn() get passed into conv(). The outputs of conv() are then output.

The first step in finding my solution was figuring out what numbers in the A and B matrix were used to produce the seven numbers in the array in out.txt. I manually worked out equations using variables. Here are the equations I cooked up (F.Y.I. I denoted R as a column vector containing the array elements in out.txt):
> R<sub>1</sub> = A<sub>11</sub> + B<sub>1</sub> + C
> R<sub>2</sub> = A<sub>22</sub> + B<sub>2</sub> + C
> R<sub>3</sub> = A<sub>11</sub> + A<sub>12</sub> + A<sub>22</sub> + B<sub>1</sub> + B<sub>2</sub> + C
> R<sub>4</sub> = A<sub>33</sub> + B<sub>3</sub> + C
> R<sub>5</sub> = A<sub>11</sub> + A<sub>13</sub> + A<sub>33</sub> + B<sub>1</sub> + B<sub>3</sub> + C
> R<sub>6</sub> = A<sub>22</sub> + A<sub>23</sub> + A<sub>33</sub> + B<sub>2</sub> + B<sub>3</sub> + C
> R<sub>7</sub> = A<sub>11</sub> + A<sub>12</sub> + A<sub>22</sub> + A<sub>13</sub> + A<sub>23</sub> + A<sub>33</sub> + B<sub>1</sub> + B<sub>2</sub> + B<sub>3</sub> + C

From there, I translated these system of equations into an augmented matrix, with the coefficients of all the unknows on one side and the entries of R on the other side. I ran ```rref()``` on it using Sagemath, and I found a row where there was one free variable, took the last entry of that row, and subtracted it by the provided prime in out.txt file to get the flag.

####Flag: corctf{mind your ones and zeroes because zero squared is zero and one squared is one}

## Euclidean Algorithm Example

The Euclidean algorithm is used to find the greatest common divisor (GCD) of two integers.

```
Find GCD of 274 and 63

    1) 274 = 4 * 63 + 22
    2) 63  = 2 * 22 + 19
    3) 22  = 1 * 19 + 3
    4) 19  = 6 * 3  + 1
    5) 3   = 3 * 1  + 0

GCD of 274 and 63 is 1

```

## Extended Euclidean Algorithm

The extended Euclidean algorithm is used to solve the following problem, known as the 'linear Diophantine equation':

```
Given two integers, a and b, find the values x and y such that:

    GCD(a, b) = ax + by

```

Example:

```
Find x and y such that

    GCD(a, b) = ax + by

for values a = 274 and b = 63 we have
    
    GCD(a, b) = ax + by
    GCD(274, 63) = 274x + 63y
    1 = 274x + 63y              // GCD is 1

Start with equation (4), the rearrange so '1' is on the left hand side (LHS)
    
    19  = 6 * 3  + 1            // Equation 4
    1 = 19 - 6 * 3

Rearrange equation (3) so we can sub the value in '3' into equation (4)

    22 = 1 * 19 + 3            // Equation 3
    3 = 22 - 19

Substitute eq (3) into eq (4)

    1 = 19 - 6 * 3              // Equation 4, after we rearranged it
    1 = 19 - 6 * (22 - 19)      // Sub in '3' from the last step
    1 = 7 * 19 - 6 * 22         // Simplify, keeping '19' and '22' for the next step

Rearrange equation (2) so we can sub the value '19' in to (3)

    63  = 2 * 22 + 19           // Equation 2
    19 - 63 - 2 * 22

Substitute eq (2) into eq (3)

    1 = 7 * 19 - 6 * 22
    1 = 7 * (63 - 2 * 22) - 6 * 22          
    1 = 7 * 63 - 14 * 22 - 6 * 22
    1 = 7 * 63 - 20 * 22

Rearrange equation (1) so we can sub the value 22 into (2)

    274 = 4 * 63 + 22           // Equation 1
    22 = 274 - 4 * 63

Substitute eq (1) into eq (2)

    1 = 7 * 63 - 20 * 22
    1 = 7 * 63 - 20 * (274 - 4 * 63)
    1 = 7 * 63 - 20 * 274 + 80 * 63
    1 = 87 * 63 - 20 * 274

Our answer for the extended Euclidean algorithm is

    1 = 87 * 63 - 20 * 274
    1 = 274x + 63y

    x = -20
    y = 87

We can verify our answer (ALWAYS DO THIS STEP - ALWAYS)

    1 = 87 * 63 - 20 * 274
    1 = 5481 - 5480
    1 = 1
```
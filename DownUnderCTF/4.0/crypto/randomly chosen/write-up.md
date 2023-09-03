###Challenge: randomly chosen

####Category: crypto

####Description: Can you recover the flag from this random jumble of characters?

####Author: joseph

Looking into the source code to generate the output, it looks like there may be no way to solve the challenge, at least to some CTF beginners:

```python
import random

random.seed(random.randrange(0, 1337))
flag = open('./flag.txt', 'r').read().strip()
out = ''.join(random.choices(flag, k=len(flag)*5))
print(out)
```

Essentially, the plaintext that is the flag is randomized into different positions on a 305-character string. How can we piece the flag back together? Well, the first step is to realize that the randomization of the positions of the characters in the ciphertext can actually be predicted. Why? Well, the Python module random, given a particular seed, will generate a specific sequence of randomized choices. In other words, we can predict the order in which the flag characters are arranged in the ciphertext as long as we know the seed. From there, we can make observations as to where the flag characters can be mapped onto their positions in the ciphertext.

For me, the main struggle was how to find the seed. The way I found it was to iteratively run through a list of potential candidates for the seed and whittle down the list until one option remains. To whittle down the list, at each iteration of candidates to go through, I checked to see if a certain character in a resulting test string, when a given string is run through the randomization, shows up in the same position as it does in the ciphertext. The test string was modeled to be similar to the flag format, with 305 // 5 = 61 characters in length. From there, it was a matter of figuring out how to code the mapping of the ciphertext characters back to order of which the flag characters are.

####Flag: DUCTF{is_r4nd0mn3ss_d3t3rm1n1st1c?_cba67ea78f19bcaefd9068f1a}

Solved by giggsterpuku

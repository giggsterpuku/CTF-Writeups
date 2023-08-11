###Challenge: cbc

####Category: crypto

####Description: who on earth is putting CLASSICAL BORING CRYPTOGRAPHY in my ctf

To first understand what I was going to see in the ciphertext, I looked into the cbc.py encryption script to see what how the ciphertext is made. The encrytion was implemented as what seems to be a combination of the Vignere Cipher and CBC (*C*ipher *B*lock *C*haining). If you want to look at a reference for what CBC is check [here](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation), and if you want one for Vigenere cipher check [here](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

To break it down, here are two main functions that I think are key to understanding what I mean. First examine the add_key() function:

```python
def add_key(key, block):
    ct_idxs = [(k_a + pt_a) % len(alphabet) for k_a, pt_a in zip([alphabet.index(k) for k in key], [alphabet.index(pt) for pt in block])]
    return "".join([alphabet[idx] for idx in ct_idxs])
```

Here, the key is used like that of the Vigenere cipher. Each character of the key supplied corresponds to a Caesar cipher shift to the corresponding character in the plaintext that shares the same position in their respective strings. Now, this is implemented in a broader picture in the cbc() function:

```python
def cbc(key, plaintext):
    klen = len(key)
    plaintext = pad(klen, plaintext)
    iv = random_alphastring(klen)
    blocks = [plaintext[i:i+klen] for i in range(0, len(plaintext), klen)]
    prev_block = iv
    ciphertext = ""
    for block in blocks:
        block = add_key(prev_block, block)
        prev_block = add_key(key, block)
        ciphertext += prev_block
    return iv, ciphertext
```

Essentially, this function implements the CBC scheme. Typically a XOR cipher is implemented at each step of the encryption process to sort of fuse the Initiation Vector (IV) or key with each block of string in the plaintext to further encrypt the plaintext as a whole. However, it seems like the Vignere cipher does that instead. Thus, the decryption process should have steps to decrypt the ciphertext by way of Vignere cipher. I was trying to figure out a way to recover the key, and reflecting on my solution process for the eyes challenge, I though I could use some linear algebra to get the key. For example, let's say I have each block in the ciphertext and addition in this case is the application of the Vignere encryption process. I can model the ciphertext like so:


> ctBlock1 = iv + ptBlock1 + key
> ctBlock2 = ctBlock1 + ptBlock2 + key = *iv + ptBlock1 + key* + ptBlock2 + key
> ctBlock3 = ctBlock2 + ptBlock3 + key = *iv + ptBlock1 + key + ptBlock2 + key* + ptBlock3 + key

... And so on and so forth. I thought that I could treat each ptBlock as an unknown and the key as well and plug them in a design matrix and find its row reduced echelon form to get each key. However, when put into a script, I realized the design matrix was flawed, as its reduced row echelon form revealed that the matrix contains linearly dependent column vector, which makes finding the key very hard at this point. After getting time to review this challenge after the CTF, I found a much easier way to solve the challenge with the help of some discussion in the CTF Discord server:

1. Remove the effects of the IV from the each block by decrypting each block in the Vigenere scheme using the IV as the key.
2. Remove each block's effects of the previous block (except for the first block in the ciphertext) using the same scheme. Each block would them end up in the following form: **newBlockN = ptBlockN + key**.
3. At that point, it's a matter of deciphering the ciphertext using Vignere's cipher on the newly made string of blocks. Since I do not know the key, I can try to get an autosolver to find it by examining different key combinations and their respective resulting plaintexts. I used [this site](https://www.boxentriq.com/code-breaking/vigenere-cipher) that the other CTF players used to solve this challenge. Examining it, I found a plaintext that looked readable and used a block of it to decrypt a block in the same position in the original ciphertext to recover the key. I then designed a decryption scheme similar to CBC but used the Vigenere decryption process for decrypting each block in the ciphertext. From there, I got the plaintext with the flag in it.

####Flag: corctf{ATLEASTITSNOTAGENERICROTTHIRTEENCHALLENGEIGUESS}

Reviewed by giggsterpuku

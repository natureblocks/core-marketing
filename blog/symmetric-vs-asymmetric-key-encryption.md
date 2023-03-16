# What is the difference between Symmetric and Asymmetric-Key Encryption?
## Have you ever wondered how your data is kept safe when it is transmitted over the internet? In this blog post, we explore the fundamental concepts behind symmetric and asymmetric-key encryption, shedding light on the key differences between the two and how they are used to secure online communications.
### Author Fullname
#### Dec 12, 2022
##### cryptocurrency
## What is a cryptographic key?

All [cryptography](https://natureblocks.com/blog/what-is-cryptography) requires a key because **keys create and crack the code of cryptographic communications**. A key can be as simple as a random number or as complex as an entire algorithm. ‍

> You can think of the relationship between keys and encrypted data as the relationship between a legend and a map. Without the legend, it is nearly impossible to understand what the symbols on a map represent. Likewise, it is almost impossible to encrypt and decrypt information without a key.

In key encryption, the terms symmetric and asymmetric refer to the keys that senders and receivers use to encrypt and decrypt information. In symmetric systems, both sender and receiver use the same key. In asymmetric systems, the sender and receiver each have a unique key input. Both systems have pros and cons.

## What is symmetric-key encryption?

In symmetric-key or single-key encryption, the transmission and reception of encrypted messages require two parties first to share a random number known as a key. Symmetric-key algorithms produce bits in fixed lengths, called block ciphers. Block ciphers contain the secret key that both the sender and receiver use. Senders use the secret key to encrypt the information they are sending, and receivers use the secret key to decrypt the information they are receiving.

## Where is symmetric-key encryption used?

Numerous companies and the U.S. government use Symmetric-key block ciphers such as the Advanced Encryption Standard (AES). AES was announced by the National Institute of Standards and Technology (NIST) in 2001 as a Federal Information Processing Standard (FIPS 197) and replaced the Data Encryption Standard (DES) that was introduced in 1977. In June 2003, AES was fully approved by the U.S. government and continues to be the standard of data encryption today.

## What are the downfalls of symmetric-key encryption?

The problem with symmetric-key or single-key encryption is that sharing a key before communication limits encryption to only messages sent between parties who have previous access to the key. Two parties who have never met cannot agree on a shared key in secrecy without other parties potentially having access to this key, which could negate the security of the encryption. ‍

> This nuance does not affect entities such as large enterprises and the U.S. government because they can easily communicate privately to agree on a key. However, anyone looking to communicate anonymously or without knowing the other party cannot achieve confidentiality with the single-key system.

## What is asymmetric-key encryption?

Asymmetric-key or public-key encryption solves this problem by allowing the sender and receiver to each have a unique key input. Instead of breaking the confidentiality by sharing these individual key inputs with each other, the two communicating parties use mathematical equations to verify each other's specific key input. Public-key encryption allows sender and receiver to use their separate inputs to derive a shared key anonymously without ever knowing each other's key inputs. Senders and receivers can then use this key to encrypt and decrypt any data they want to communicate.

## Where is asymmetric-key encryption used?

Many different internet services use asymmetric-key encryption algorithms. For example, the first cryptocurrency, Bitcoin, introduced the Elliptic Curve Digital Signature Algorithm (ECDSA) for transactions, and it requires asymmetric-key encryption to function. All cryptocurrencies use similar algorithms with asymmetric keys to allow for anonymous encrypted transactions to be recorded to the [blockchain](https://natureblocks.com/blog/what-is-blockchain).

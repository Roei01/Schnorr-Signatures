Schnorr Signature Demo – README
This demonstration script shows the flow of generating a private key, creating a signature for a user-provided message, and verifying that signature manually. It uses small, insecure parameters (p=23, q=11, g=2), purely for educational purposes.

1. Features

Key Generation: Randomly picks a private key x and computes the public key y = g^x mod p.
Message Signing: Prompts the user for a message, creates a Schnorr signature (r, s) using a random nonce k.
Manual Verification: Displays the real public key, then asks the user to enter a public key. If they enter the correct y, the signature is valid; otherwise, it fails.


2. How to Run
Make sure you have Python (version 3.6+).
Save the file as, for example, schnorr_demo.py.
In a terminal, navigate to the file’s directory and run:
python schnorr_demo.py

Follow the on-screen prompts:
Type a message.
The script shows (r, s) (your signature) and the real y (public key).
Enter y back in correctly to see a valid signature, or a different number to see an invalid signature.


3. Example Session
(Your actual numbers may differ because of random generation.)
==========================================
  Schnorr Signature Demonstration (Demo)
==========================================

[Step 1] Global Parameters (p, q, g)
  p = 23 (prime)
  q = 11 (subgroup order)
  g = 2 (generator)

[Step 2] Generating Keys (Private & Public)
  Private key (x) = 7   (keep it secret!)
  Public key (y)  = 13

[Step 3] Enter a message to sign:
Message: Hello Schnorr

[Step 4] Creating the Signature (r, s)
  ... (shows k, r, e, s)
  Signature: (r, s) = (15, 9)

Enter y correctly to see a valid verification, or something else to fail.

The REAL public key (y) is: 13
Enter the public key for verification: 13

[Step 6] Verifying the signature with the provided public key...
Result: The signature is VALID.

4. Important Notes
Small Parameters: The numbers (p=23, q=11, g=2) demonstrate the concept only. Real security requires large primes or elliptic curves.
Nonce k: Each signature uses a fresh k; reusing the same k can reveal the private key.
Production Use: For real-world systems, rely on professionally audited libraries (e.g., OpenSSL, libsodium) and standard elliptic curves.

Schnorr Signature Demo – README
This Schnorr Signature Demonstration shows the basic flow of generating a private key, creating a signature for a message, and verifying that signature. Please note that the parameters used here (p=23, q=11, g=2) are extremely small and not secure in real-world scenarios. Their only purpose is to illustrate the math behind the Schnorr scheme.

Features
Key Generation

Generates a private key (x) randomly.
Derives the corresponding public key (y = g^x mod p).
Signing

Prompts the user for a message.
Creates a Schnorr signature (r, s).
Uses a random nonce k each time you sign.
Verification (Manual Entry)

The script shows the real public key but lets you enter a public key of your choice.
If you enter the correct y, the signature verifies; if you enter something else, it fails.
How to Run
Install Python (3.6+ recommended).
Save this file as, for example, schnorr_demo.py.
In a terminal or command prompt, navigate to where schnorr_demo.py is located.
Run:
bash
Copy
Edit
python schnorr_demo.py
Follow the prompts:
Enter a message.
A signature (r, s) will be created.
The script will display the real public key and then ask you to provide a public key for verification.
Type the same public key to see a valid result, or something else to make it fail.

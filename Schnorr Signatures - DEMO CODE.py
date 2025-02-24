import secrets
import hashlib

def hash_function(data: bytes) -> int:
    """
    A simple SHA-256 hash function that returns an integer.
    """
    return int(hashlib.sha256(data).hexdigest(), 16)

def run_schnorr_demo():
    """
    Schnorr Signature Demonstration (small/insecure parameters):
      1. Generate private key (x) and public key (y).
      2. Sign a user-provided message (producing r, s).
      3. Ask the user for a public key to test verification
         (correct => valid, incorrect => invalid).
    """

    print("==========================================")
    print("  Schnorr Signature Demonstration (Demo)")
    print("==========================================\n")

    p = 23
    q = 11
    g = 2

    print("[Step 1] Global Parameters (p, q, g)")
    print(f"  p = {p} (prime)")
    print(f"  q = {q} (subgroup order)")
    print(f"  g = {g} (generator of subgroup order q)\n")

    # 2. Generate a private key (x) and a public key (y)
    print("[Step 2] Generating Keys (Private & Public)")
    x = secrets.randbelow(q - 1) + 1  # Private key in [1..q-1]
    y = pow(g, x, p)                  # Public key = g^x mod p
    print(f"  Private key (x) = {x}   (keep it secret!)")
    print(f"  Public key (y)  = {y}\n")

    # 3. Ask the user for a message to sign
    print("[Step 3] Enter a message to sign:")
    user_message = input("Message: ")
    message_bytes = user_message.encode("utf-8")

    # 4. Create the signature (r, s)
    print("\n[Step 4] Creating the Signature (r, s)")
    # (a) Choose a random nonce 'k' in [1..q-1]
    k = secrets.randbelow(q - 1) + 1
    # (b) Calculate r = g^k mod p
    r = pow(g, k, p)
    # (c) Compute e = H(r || message) mod q
    r_bytes = r.to_bytes((r.bit_length() + 7) // 8, 'big')
    e_full = hash_function(r_bytes + message_bytes)
    e = e_full % q
    # (d) Compute s = (k + x*e) mod q
    s = (k + x * e) % q

    print(f"  Random nonce (k) = {k}")
    print(f"  r = g^k mod p = {r}")
    print(f"  e = SHA-256(r || message) mod q = {e}")
    print(f"  s = (k + x*e) mod q = {s}")
    print(f"\n  Signature: (r, s) = ({r}, {s})\n")

    print("\nEnter y correctly to see a valid verification, or something else to fail.\n")
    print(f"The REAL public key (y) is: {y}")

    # Let the user manually enter the public key to check
    entered_y_str = input("Enter the public key for verification: ")
    try:
        y_verifier = int(entered_y_str)
    except ValueError:
        print("\nError: Invalid integer input.")
        return

    print("\n[Step 6] Verifying the signature with the provided public key...\n")
    # Recompute e' = H(r || message) mod q
    r_bytes_recv = r.to_bytes((r.bit_length() + 7) // 8, 'big')
    e_prime_full = hash_function(r_bytes_recv + message_bytes)
    e_prime = e_prime_full % q

    # Check the Schnorr equation: g^s == r * (y^e') mod p ?
    left_side = pow(g, s, p)
    right_side = (r * pow(y_verifier, e_prime, p)) % p

    if left_side == right_side:
        print("Result: The signature is VALID.")
    else:
        print("Result: The signature is INVALID.")

if __name__ == '__main__':
    run_schnorr_demo()

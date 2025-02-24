<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Schnorr Signature Demo – README</title>
  <!-- Minimal styling using basic tags only -->
</head>
<body>

<h1>Schnorr Signature Demo – README</h1>
<p>
  This demonstration script shows the flow of generating a private key, creating a
  signature for a user-provided message, and verifying that signature manually.
  It uses <em>small, insecure parameters</em> (<code>p=23</code>, <code>q=11</code>,
  <code>g=2</code>), purely for <strong>educational</strong> purposes. Real-world
  systems require much larger primes or elliptic curves.
</p>

<hr/>

<h2>Features</h2>
<ul>
  <li>
    <strong>Key Generation:</strong> Randomly picks a private key <code>x</code> and computes
    the public key <code>y = g^x mod p</code>.
  </li>
  <li>
    <strong>Message Signing:</strong> Prompts the user for a message, creates a Schnorr signature
    <code>(r, s)</code> using a random nonce <code>k</code>.
  </li>
  <li>
    <strong>Manual Verification:</strong> Displays the real public key, then asks the user to
    enter a public key. If they enter the correct <code>y</code>, the signature is valid;
    otherwise, it fails.
  </li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Make sure you have Python 3.6+ installed.</li>
  <li>Save the file as <code>schnorr_demo.py</code>.</li>
  <li>In a terminal, navigate to that file’s directory.</li>
  <li>Run:
    <pre>python schnorr_demo.py</pre>
  </li>
  <li>Follow the on-screen prompts:
    <ul>
      <li>Type a message.</li>
      <li>The script shows <code>(r, s)</code> (your signature) and the real public key <code>y</code>.</li>
      <li>Enter <code>y</code> to see a valid signature, or a different number for an invalid one.</li>
    </ul>
  </li>
</ol>

<h2>Example Session</h2>
<p>Your actual numbers will differ because of randomness:</p>
<pre>
==========================================
  Schnorr Signature Demonstration (Demo)
==========================================

[Step 1] Global Parameters (p, q, g)
  p = 23 (prime)
  q = 11 (subgroup order)
  g = 2 (generator)

[Step 2] Generating Keys (Private & Public)
  Private key (x) = 7 (keep it secret!)
  Public key (y)  = 13

[Step 3] Enter a message to sign:
Message: Hello Schnorr

[Step 4] Creating the Signature (r, s)
  ... (shows k, r, e, s)
  Signature: (r, s) = (15, 9)

Enter y correctly to see a valid verification, or something else to fail.

The REAL public key (y) is: 13
Enter the public key for verification: 13

[Step 5] Verifying the signature with the provided public key...
Result: The signature is VALID.
</pre>

<h2>Important Notes</h2>
<ul>
  <li><strong>Small Parameters:</strong> <code>p=23</code>, <code>q=11</code>, <code>g=2</code> are for
    demonstration only. Real security requires large primes or elliptic curves.</li>
  <li><strong>Nonce <code>k</code>:</strong> Each signature uses a new <code>k</code>; reusing the same <code>k</code> could
    reveal the private key.</li>
  <li><strong>Production Use:</strong> For real deployments, rely on audited libraries (e.g.,
    <code>OpenSSL</code>, <code>libsodium</code>) and standard elliptic curves.</li>
</ul>

</body>
</html>

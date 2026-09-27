# CipherCorp

CipherCorp is an offline-first live demonstration of how public-key cryptography operates inside real application flows. It is not an educational simulation or a collection of isolated math exercises. Each workspace follows a concrete action from the client, across the network, into a backend, verifier, or validator.

## Open it locally

Open [cipher-corp/index.html](./cipher-corp/index.html) directly in a browser. The root [index.html](./index.html) is a small launcher.

No build step, server, network connection, or library is required.

## Deploy to Vercel

This is a static site and needs no build command, install command, environment variables, or serverless functions.

### Vercel dashboard

1. Import this project folder into Vercel.
2. Leave the framework preset as **Other**.
3. Leave Build Command and Install Command empty.
4. Deploy.

The included [vercel.json](./vercel.json) routes the domain root directly to the CipherCorp workspace and also supports `/cipher-corp`.

### Vercel CLI

From the project root:

```bash
npx vercel
```

For a production deployment:

```bash
npx vercel --prod
```

## Live application demonstrations

- **Diffie-Hellman:** create a session-key request and watch two clients derive the same secret without sending it across the network.
- **DSA:** enter a release message, sign it in the release client, send the public payload, and watch the receiving service verify the exact message.
- **ECDSA:** enter a transaction, create the wallet signature, broadcast the public transaction data, and watch a validator reproduce the curve-point proof.

Each action begins a deliberately paced autonomous procedure. The client, network payload, backend stage, and current calculation are shown together. Values are recalculated locally with native `BigInt`, and invariant checks report when a displayed result is inconsistent.

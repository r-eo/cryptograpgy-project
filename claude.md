# Claude Code Build Prompt: "CipherCorp" — Learn DH, DSA & ECDSA by Doing

Copy everything below into Claude Code as your task prompt.

---

## The Idea

Build **CipherCorp**, a single-page interactive web app that teaches **Diffie–Hellman Key Exchange**, **DSA**, and **ECDSA** through one connected story instead of three disconnected demos:

> CipherCorp is a startup that needs to (1) let two employees agree on a secret key over an insecure network, and (2) digitally sign official documents/software updates so people can trust they're authentic and untampered. The app walks the user through solving both problems live, with real (small-number) math computed on screen at every step, then lets a live audience play a couple of quick games that only make sense once they've seen how the math works.

Build it as a **single self-contained HTML file** (inline CSS + JS, no build step, no backend, works fully offline except for one optional confetti CDN script). Use **BigInt** for all math — no cutting corners with floats. All crypto must be implemented **from scratch** (modular exponentiation, modular inverse via extended Euclidean algorithm, manual elliptic curve point addition/doubling) for full transparency — no crypto libraries, since the entire point is to *show the math*, not hide it behind a black box.

---

## Structure

### 0. Landing / Story Screen
- CipherCorp branding, a one-paragraph plain-English framing of the two problems being solved ("how do two people agree on a secret when everyone can hear them talking?" / "how do you prove a message really came from you and wasn't altered?").
- Three big nav cards: **Diffie–Hellman**, **DSA**, **ECDSA**. Each shows a one-line "what problem this solves" tag.
- A toggle in the header: **🧸 Toy Numbers** (tiny numbers, fully human-followable) vs **💪 Realistic Scale** (bigger BigInt values, same steps, showing this is the same math used for real). Default to Toy Numbers.

### 1. Diffie–Hellman Module — "Two employees, one secret, over a tapped line"
Frame it as two CipherCorp employees, **Asha** and **Bilal**, who must agree on a shared secret key while a nosy intern **Eve** watches every message they send.

Stepwise walkthrough (each step its own card, Next/Prev/Play controls, current formula shown alongside plain-English narration):
1. Public setup: prime `p` and generator `g` are agreed publicly (shown to Eve too — she gets to "see" these).
2. Asha secretly picks private number `a`; Bilal secretly picks private number `b` (shown only on their respective side of a split screen — Eve's side stays blank here).
3. Asha computes `A = g^a mod p`; Bilal computes `B = g^b mod p` — show the modular exponentiation expanding step by step (e.g. square-and-multiply trace), not just the final number.
4. Asha and Bilal exchange `A` and `B` publicly — animate these values flying across to Eve's panel too, to make visible that Eve now knows `p, g, A, B` but *not* `a`, `b`.
5. Asha computes `s = B^a mod p`; Bilal computes `s = A^b mod p`. Show both computations side by side landing on the same number.
6. Reveal: Eve's panel tries the same computation with what she has and is visibly stuck (show why: she'd need to solve a discrete log, and briefly explain what that hard problem is in one sentence, no proofs).

### 2. DSA Module — "Prove this update really came from CipherCorp"
Frame it as CipherCorp shipping a software update and needing to prove it's authentic.

Stepwise walkthrough:
1. Domain parameters `p`, `q`, `g` generated/shown.
2. Key generation: private key `x`, public key `y = g^x mod p`.
3. Signing the update's message hash `H(m)`: pick random `k`, compute `r = (g^k mod p) mod q`, then `s = k⁻¹(H(m) + x·r) mod q` — show the modular inverse computed via extended Euclidean algorithm step by step, not just asserted.
4. Output signature `(r, s)` attached to the message.
5. Verification (run as a separate "recipient" panel that only has the public key + message + signature): compute `w = s⁻¹ mod q`, `u1 = H(m)·w mod q`, `u2 = r·w mod q`, `v = (g^u1 · y^u2 mod p) mod q`, then check `v == r`.
6. A "tamper" button that flips one bit of the message and reruns verification live, showing it now fails — make this visually dramatic (red flash, clear "SIGNATURE INVALID" state).

### 3. ECDSA Module — "Same idea, smaller keys, curvier math"
Use a genuine **toy elliptic curve** over a small prime field (e.g. `y² = x³ + ax + b mod p` with `p` around 97–229) so every point can be plotted and point addition drawn as actual geometry.

Stepwise walkthrough:
1. Show the curve equation and all valid points on it plotted on a canvas/SVG grid (the classic "dots scattered across a field" look for curves mod p — explain in one line why it doesn't look like the smooth curve people expect, since we're working mod p).
2. Base point `G` chosen, its order `n` shown.
3. Key generation: private key `d`, public key `Q = d·G`. Animate this as repeated point-doubling/addition (the actual double-and-add algorithm), tracing the line-through-two-points → reflect construction on the plotted curve at each step.
4. Signing: pick random `k`, compute `R = k·G`, take `r = R.x mod n`, compute `s = k⁻¹(H(m) + d·r) mod n`.
5. Verification: compute `u1 = H(m)·w mod n`, `u2 = r·w mod n` where `w = s⁻¹ mod n`, then plot the point `u1·G + u2·Q` live and check its x-coordinate mod n matches `r`.
6. Side-by-side comparison card at the end: "DSA vs ECDSA — same idea, why ECDSA gets away with much smaller numbers for the same security" (one short paragraph + a size comparison bar chart, no deep math).

Each module's step cards must show: the **narration** (plain English), the **formula** being applied, the **actual live-computed numbers**, and a **"why this step matters"** one-liner. Include a persistent glossary drawer (tap a bolded term like "modular inverse", "generator", "discrete log", "elliptic curve point addition" anywhere in the app to get a plain-English tooltip).

---

## The Fun Part: Audience Participation (make this genuinely nice, not gimmicky)

Add a **"🎮 Play Along"** tab, meant to be used live with a room of people (or solo). Two short, friendly games, each under 2 minutes:

### Game 1 — "Guess the Secret Handshake" (after the DH module)
- The presenter's screen shows `p`, `g`, `A`, and `B` (everything Eve can see) live.
- Anyone in the audience can type in a guess for the shared secret `s` using a simple number pad UI.
- No penalty for wrong guesses, no timers, no pressure — frame it warmly: *"Go ahead, take a guess — even Eve is stuck, so don't worry if you are too!"*
- When the real answer is revealed, show a friendly distribution of everyone's guesses (bar chart) and gently celebrate anyone who happened to land on it, with confetti and a "nice guess!" message — but the actual point of the game, stated on screen, is realizing *why* guessing is so hard even with every public number in front of you.

### Game 2 — "Signature Detective" (after the ECDSA/DSA modules)
- Show a message and **three candidate signatures**: one genuine, two subtly tampered.
- Audience votes which one is real by tapping a card (A / B / C) — a simple live tally bar updates as votes come in.
- After voting closes, run the actual verification algorithm on all three, live, one at a time, with clear ✅ / ❌ reveals and a short explanation of *why* each fake one fails.
- End with encouraging copy regardless of the group's score — e.g. *"However the room voted, you now know something most software users never think about: how your computer checks this automatically, every single time."*

Both games should feel like a warm, low-stakes classroom activity — bright colors, big friendly buttons, no leaderboard-shaming, no correct/incorrect audience labeling beyond light celebratory feedback. Keep language encouraging throughout (e.g., "nice try", "good instinct", "here's the fun part").

---

## Design & UX requirements
- Clean, modern, slightly playful visual identity for "CipherCorp" (pick a simple color palette and consistent type scale — do not use generic default Bootstrap styling).
- Step-through controls (Prev / Next / Autoplay with adjustable speed) on every module.
- Split-panel visuals wherever there are two+ parties (Asha/Bilal/Eve, Signer/Verifier) so the audience can see who knows what at every step.
- Mobile-friendly layout since audience members will likely join Game 1/2 on phones.
- All computation happens client-side in the browser; no server, no data leaves the device.

## Deliverables
- One `index.html` (or a small `/cipher-corp` folder if you split CSS/JS out — keep it minimal either way).
- A short `README.md` explaining how to open it (just open the HTML file / serve locally) and a one-paragraph summary of what's inside each module.
- Inline code comments in the crypto functions explaining each mathematical step, since this doubles as a learning resource for anyone who reads the source too.

## Acceptance checklist (verify before calling it done)
- [ ] All three algorithms use real, correct math (no fake/simulated numbers) — verify DH shared secrets match, DSA/ECDSA signatures verify correctly and fail correctly when tampered.
- [ ] Every step of every algorithm is shown individually with narration + formula + live numbers, not just an end result.
- [ ] Toy Numbers mode is fully hand-verifiable (small enough that a curious person could redo the arithmetic on paper).
- [ ] Both Play Along games work without any setup beyond opening the page, feel warm and encouraging, and tie back to a real concept from the modules.
- [ ] Works fully offline after first load, no crypto libraries used.
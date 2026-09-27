import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = pptx.Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # White and Sanguine Color Palette
    BG_WHITE = RGBColor(248, 249, 250)         # #F8F9FA
    CARD_WHITE = RGBColor(255, 255, 255)       # #FFFFFF
    CARD_BORDER = RGBColor(226, 232, 240)      # #E2E8F0
    TEXT_MAIN = RGBColor(15, 23, 42)           # #0F172A
    TEXT_MUTED = RGBColor(71, 85, 105)         # #475569
    TEXT_WHITE = RGBColor(255, 255, 255)       # #FFFFFF

    SANGUINE_PRIMARY = RGBColor(155, 27, 48)   # #9B1B30 Classical Sanguine
    SANGUINE_DEEP = RGBColor(116, 18, 34)      # #741222 Deep Blood Red
    SANGUINE_BRIGHT = RGBColor(197, 34, 51)    # #C52233 Vivid Accent
    SANGUINE_TINT = RGBColor(253, 242, 244)    # #FDF2F4 Soft Sanguine Wash
    BORDER_SANGUINE = RGBColor(214, 140, 152)  # #D68C98
    GREEN_SUCCESS = RGBColor(21, 128, 61)      # #15803D

    def add_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_WHITE
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text):
        # Category ribbon / badge
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = SANGUINE_PRIMARY

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.75))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN

    def add_bento_card(slide, left, top, width, height, fill_color=CARD_WHITE, border_color=CARD_BORDER, border_width=1.5):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (WHITE & SANGUINE BENTO DESIGN)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_slide_background(s1)

    # Accent decorative bento card
    c1 = add_bento_card(s1, Inches(1.2), Inches(1.2), Inches(10.933), Inches(5.1), CARD_WHITE, SANGUINE_PRIMARY, border_width=2.5)

    tb = s1.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.7), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "REAL-WORLD CRYPTOGRAPHY IN PRODUCTION"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = SANGUINE_PRIMARY
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = "Modern Public-Key Algorithms"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_MAIN
    p1.space_after = Pt(6)

    p2 = tf.add_paragraph()
    p2.text = "Diffie–Hellman (DH)  •  DSA  •  ECDSA"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = SANGUINE_DEEP
    p2.space_after = Pt(18)

    p3 = tf.add_paragraph()
    p3.text = "A simple and informative breakdown of real-life production applications (Signal E2EE, Linux OS Signing, and Blockchain Wallets) with step-by-step algorithms and simple worked examples."
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: PRODUCTION APPLICATIONS MAPPING
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_background(s2)
    add_header(s2, "Mapping the Algorithms to Real-Life Applications", "System Architecture")

    apps = [
        ("Diffie–Hellman (DH)",
         "Real-World Application: E2EE Messaging & TLS Handshakes",
         "Used in Signal, WhatsApp, and TLS 1.3 to establish forward-secret symmetric keys between two phones across an insecure Wi-Fi / cellular network without transmitting the secret.",
         SANGUINE_TINT, SANGUINE_PRIMARY),

        ("Digital Signature Algorithm (DSA)",
         "Real-World Application: OS Kernel & Package Integrity",
         "Used in Linux Debian (apt) and Red Hat (rpm) package signing to verify that operating system updates and kernel modules originate from verified release engineers and have not been tampered with.",
         CARD_WHITE, CARD_BORDER),

        ("Elliptic Curve DSA (ECDSA)",
         "Real-World Application: Blockchain & Crypto Wallets",
         "Used in Bitcoin, Ethereum, and Apple Pay to digitally authorize financial transactions using curve secp256k1, delivering 128-bit security with 256-bit keys (an 8x size reduction).",
         CARD_WHITE, CARD_BORDER)
    ]

    card_w = Inches(3.7)
    gap = Inches(0.3)
    left_start = Inches(0.8)

    for i, (algo, app_title, app_desc, f_col, b_col) in enumerate(apps):
        c_left = left_start + i * (card_w + gap)
        add_bento_card(s2, c_left, Inches(1.7), card_w, Inches(5.1), f_col, b_col)

        tb = s2.shapes.add_textbox(c_left + Inches(0.25), Inches(1.95), card_w - Inches(0.5), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = algo
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = SANGUINE_DEEP
        p.space_after = Pt(10)

        p2 = tf.add_paragraph()
        p2.text = app_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_after = Pt(12)

        p3 = tf.add_paragraph()
        p3.text = app_desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: DIFFIE-HELLMAN REAL-WORLD MECHANISM
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_background(s3)
    add_header(s3, "Diffie–Hellman: How End-to-End Chat Negotiates a Secret", "Application 1: Signal & WhatsApp")

    add_bento_card(s3, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), SANGUINE_TINT, SANGUINE_PRIMARY)
    tb = s3.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "The Hostile Wire Problem"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    dh_points_left = [
        ("The Environment: ", "Alice (Client Phone) and Bob (Server) communicate through untrusted Wi-Fi routers and public ISP switches where an attacker (Eve) can read every single transmitted packet."),
        ("The Goal: ", "Derive a shared symmetric key 's' that only Alice and Bob know, without ever transmitting 's' across the network."),
        ("The Trapdoor Mechanism: ", "Computing modular exponentiation A = g^a mod p is instantaneous. But reversing it—extracting private exponent 'a' given public A, g, and p—is the intractable Discrete Logarithm Problem.")
    ]
    for b_txt, n_txt in dh_points_left:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    add_bento_card(s3, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1))
    tb = s3.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "From Handshake to Chat Encryption"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_after = Pt(10)

    dh_points_right = [
        ("1. Handshake Phase: ", "Alice sends public key A; Bob sends public key B. Eve observes both A and B in flight."),
        ("2. Independent Derivation: ", "Alice calculates s = B^a mod p. Bob calculates s = A^b mod p. Both land on identical secret s = g^(ab) mod p."),
        ("3. Activation of Symmetric Cipher: ", "The derived integer 's' is fed into a symmetric stream/block cipher (e.g., AES-GCM)."),
        ("4. Message Transmission: ", "Alice encrypts her message ('Deploy patch at 0300'). The ciphertext crosses the wire. Eve sees unreadable hex, while Bob uses 's' to decrypt.")
    ]
    for b_txt, n_txt in dh_points_right:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_DEEP
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: DIFFIE-HELLMAN ALGORITHM SPECIFICATION
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_background(s4)
    add_header(s4, "Diffie–Hellman: Mathematical Algorithm Specification", "Algorithm Details")

    dh_steps = [
        ("1. Public Setup", "Choose prime modulus 'p' and generator 'g' (primitive root modulo p).\nBoth are public to all participants.", CARD_WHITE, CARD_BORDER),
        ("2. Private Nonces", "Alice picks secret random exponent a ∈ [2, p - 2].\nBob picks secret random exponent b ∈ [2, p - 2].", SANGUINE_TINT, SANGUINE_PRIMARY),
        ("3. Public Keys", "Alice computes: A = g^a mod p\nBob computes: B = g^b mod p\n(via square-and-multiply).", CARD_WHITE, CARD_BORDER),
        ("4. Exchange", "Alice sends A to Bob.\nBob sends B to Alice.\nEve intercepts p, g, A, and B.", CARD_WHITE, CARD_BORDER),
        ("5. Shared Secret", "Alice computes: s = B^a mod p\nBob computes: s = A^b mod p\ns_Alice = s_Bob = g^(ab) mod p!", SANGUINE_TINT, SANGUINE_PRIMARY)
    ]

    card_w = Inches(2.25)
    gap = Inches(0.12)
    left_start = Inches(0.8)

    for i, (title, body, f_col, b_col) in enumerate(dh_steps):
        c_left = left_start + i * (card_w + gap)
        add_bento_card(s4, c_left, Inches(1.7), card_w, Inches(5.1), f_col, b_col)

        tb = s4.shapes.add_textbox(c_left + Inches(0.15), Inches(1.9), card_w - Inches(0.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = SANGUINE_DEEP
        p.space_after = Pt(10)

        p2 = tf.add_paragraph()
        p2.text = body
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 5: DSA REAL-WORLD MECHANISM (OS SIGNING)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_background(s5)
    add_header(s5, "DSA: How Linux OS Packages & Firmware Are Verified", "Application 2: Linux & Debian APT")

    add_bento_card(s5, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1))
    tb = s5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "The Package Tampering Threat"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    dsa_points_left = [
        ("The Environment: ", "Linux distribution mirrors distribute multi-gigabyte kernel binaries (e.g. linux-image-6.8.0-generic.deb). Mirrors can be untrusted or compromised."),
        ("The Need: ", "The operating system installer ('apt-get' or 'rpm') must mathematically prove the package was produced by Canonical/Debian and not a single bit was modified in transit."),
        ("The Signature Pair (r, s): ", "The signing authority hashes the file to H(m), binds it to their private key x and a per-message ephemeral nonce k, producing the compact tuple (r, s).")
    ]
    for b_txt, n_txt in dsa_points_left:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_MAIN
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    add_bento_card(s5, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), SANGUINE_TINT, SANGUINE_PRIMARY)
    tb = s5.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Client Sandbox Verification"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    dsa_points_right = [
        ("1. Hash Computation: ", "Client computer independently hashes the received debian archive to calculate H(m)."),
        ("2. Verification Weights: ", "Client computes w = s^(-1) mod q using the Extended Euclidean Algorithm, then weights u1 = H(m)·w and u2 = r·w mod q."),
        ("3. The Test (v == r): ", "Client evaluates v = ((g^u1 · y^u2) mod p) mod q. If v matches r, the kernel code is authentic!"),
        ("4. Tamper Defense: ", "If an attacker modifies even one byte of the binary, H(m') changes completely, causing v ≠ r. The installer throws 'BADSIG' and aborts installation.")
    ]
    for b_txt, n_txt in dsa_points_right:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 6: DSA ALGORITHM SPECIFICATION
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_background(s6)
    add_header(s6, "DSA: Mathematical Algorithm Specification", "Algorithm Details")

    stages_dsa = [
        ("Stage 1: Keygen",
         "1. Primes p and q where q | (p - 1).\n"
         "2. Generator g = h^((p-1)/q) mod p > 1.\n"
         "3. Private key: x ∈ [1, q - 1].\n"
         "4. Public key: y = g^x mod p.\n\n"
         "Public: (p, q, g, y)\nPrivate: x", CARD_WHITE, CARD_BORDER),

        ("Stage 2: Signing H(m)",
         "1. Hash message: H(m).\n"
         "2. Ephemeral nonce: k ∈ [1, q - 1].\n"
         "3. r = (g^k mod p) mod q.\n"
         "4. Invert k via EEA: k^(-1) mod q.\n"
         "5. s = k^(-1) · (H(m) + x · r) mod q.\n\n"
         "Signature output: (r, s)", SANGUINE_TINT, SANGUINE_PRIMARY),

        ("Stage 3: Verification",
         "1. Check 0 < r < q and 0 < s < q.\n"
         "2. Compute w = s^(-1) mod q.\n"
         "3. u1 = H(m) · w mod q.\n"
         "4. u2 = r · w mod q.\n"
         "5. v = ((g^u1 · y^u2) mod p) mod q.\n"
         "6. Verify: v == r.", CARD_WHITE, CARD_BORDER)
    ]

    card_w = Inches(3.7)
    gap = Inches(0.3)
    left_start = Inches(0.8)

    for i, (title, body, f_col, b_col) in enumerate(stages_dsa):
        c_left = left_start + i * (card_w + gap)
        add_bento_card(s6, c_left, Inches(1.7), card_w, Inches(5.1), f_col, b_col)

        tb = s6.shapes.add_textbox(c_left + Inches(0.2), Inches(1.9), card_w - Inches(0.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = SANGUINE_DEEP
        p.space_after = Pt(12)

        p2 = tf.add_paragraph()
        p2.text = body
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 7: ECDSA REAL-WORLD MECHANISM (BLOCKCHAIN WALLETS)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_background(s7)
    add_header(s7, "ECDSA: How Blockchain Wallets Authorize Transactions", "Application 3: Bitcoin & Ethereum")

    add_bento_card(s7, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), SANGUINE_TINT, SANGUINE_PRIMARY)
    tb = s7.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Decentralized Ledger Security"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    ecdsa_points_left = [
        ("The Environment: ", "Decentralized blockchain networks (Bitcoin, Ethereum) where anonymous peers validate transactions without a central bank."),
        ("Wallet Authorization: ", "A wallet owner holds a private scalar 'd'. When transferring funds, the transaction payload ('Send 2.5 BTC to Alice') is signed on the elliptic curve."),
        ("Why Curves Won: ", "A 2048-bit DSA key required for standard security is replaced by a 256-bit elliptic curve point. Transactions stay tiny, saving network gas and blockchain storage.")
    ]
    for b_txt, n_txt in ecdsa_points_left:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    add_bento_card(s7, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1))
    tb = s7.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Point Addition & Consensus Check"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_after = Pt(10)

    ecdsa_points_right = [
        ("1. Double-and-Add Keygen: ", "Public address is derived as Q = d·G, performing geometric point additions along the curve."),
        ("2. Nonce Point R = k·G: ", "Hardware wallet picks random ephemeral k, computing curve point R. Takes r = R.x mod n."),
        ("3. Signature s: ", "Computes s = k^(-1) · (e + d·r) mod n, binding transaction hash e and private key d."),
        ("4. Consensus Node Verification: ", "Validators verify P = u1·G + u2·Q. If P.x mod n == r, the transaction is verified and mined into the blockchain ledger.")
    ]
    for b_txt, n_txt in ecdsa_points_right:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_DEEP
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 8: ECDSA ALGORITHM SPECIFICATION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_background(s8)
    add_header(s8, "ECDSA: Mathematical Algorithm Specification", "Algorithm Details")

    stages_ecdsa = [
        ("Stage 1: Keygen",
         "1. Curve y² ≡ x³ + ax + b (mod p).\n"
         "2. Base generator G with order n.\n"
         "3. Private key scalar: d ∈ [1, n - 1].\n"
         "4. Public key point: Q = d · G\n   (via double-and-add).\n\n"
         "Public: (p, a, b, G, n, Q)\nPrivate: d", CARD_WHITE, CARD_BORDER),

        ("Stage 2: Signing e = H(m)",
         "1. Hash message: e = H(m).\n"
         "2. Ephemeral scalar: k ∈ [1, n - 1].\n"
         "3. Curve point: R = k · G = (x_R, y_R).\n"
         "4. r = x_R mod n.\n"
         "5. s = k^(-1) · (e + d · r) mod n.\n\n"
         "Signature output: (r, s)", SANGUINE_TINT, SANGUINE_PRIMARY),

        ("Stage 3: Verification",
         "1. Check 0 < r < n and 0 < s < n.\n"
         "2. Compute w = s^(-1) mod n.\n"
         "3. u1 = e · w mod n.\n"
         "4. u2 = r · w mod n.\n"
         "5. Point: P = u1 · G + u2 · Q = (x_P, y_P).\n"
         "6. Verify: x_P mod n == r.", CARD_WHITE, CARD_BORDER)
    ]

    card_w = Inches(3.7)
    gap = Inches(0.3)
    left_start = Inches(0.8)

    for i, (title, body, f_col, b_col) in enumerate(stages_ecdsa):
        c_left = left_start + i * (card_w + gap)
        add_bento_card(s8, c_left, Inches(1.7), card_w, Inches(5.1), f_col, b_col)

        tb = s8.shapes.add_textbox(c_left + Inches(0.2), Inches(1.9), card_w - Inches(0.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = SANGUINE_DEEP
        p.space_after = Pt(12)

        p2 = tf.add_paragraph()
        p2.text = body
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 9: SIMPLE WORKED EXAMPLE 1 - DIFFIE-HELLMAN
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_background(s9)
    add_header(s9, "Worked Example 1: Diffie–Hellman with Simple Numbers", "Live Numerical Verification")

    add_bento_card(s9, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), CARD_WHITE, SANGUINE_PRIMARY)
    tb = s9.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Hand-Verifiable Arithmetic: p = 23, g = 5, Alice a = 6, Bob b = 15"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    ex1 = [
        ("1. Public Setup: ", "Prime modulus p = 23, Generator g = 5 (a primitive root modulo 23)."),
        ("2. Secret Exponents: ", "Alice secretly chooses a = 6. Bob secretly chooses b = 15."),
        ("3. Public Keys: ", "\n• Alice computes A = g^a mod p = 5^6 mod 23\n  5^2 = 25 ≡ 2; 5^4 = 2^2 = 4; 5^6 = 4 · 2 = 8 mod 23 ➔ A = 8\n• Bob computes B = g^b mod p = 5^15 mod 23\n  5^15 = (5^6)^2 · 5^3 = (8)^2 · 125 = 64 · 10 = 640 = 27 · 23 + 19 ≡ 19 mod 23 ➔ B = 19"),
        ("4. Wire Exchange: ", "Alice sends A = 8; Bob sends B = 19. Eve intercepts p=23, g=5, A=8, B=19."),
        ("5. Shared Secret Calculation: ", "\n• Alice calculates: s = B^a mod p = 19^6 mod 23 ➔ 19 ≡ -4 mod 23 ➔ (-4)^6 = 16^3 = 4096 = 178 · 23 + 2 ≡ 2 mod 23 ➔ s = 2\n• Bob calculates: s = A^b mod p = 8^15 mod 23 ➔ (8^2)^7 · 8 = (18)^7 · 8 ≡ 2 mod 23 ➔ s = 2"),
        ("Result: ", "Both Alice and Bob compute identical symmetric encryption key s = 2!")
    ]
    for b_txt, n_txt in ex1:
        p = tf.add_paragraph()
        p.space_after = Pt(6)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 10: SIMPLE WORKED EXAMPLE 2 - DSA
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_background(s10)
    add_header(s10, "Worked Example 2: DSA with Simple Numbers", "Live Numerical Verification")

    add_bento_card(s10, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), CARD_WHITE, SANGUINE_PRIMARY)
    tb = s10.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Hand-Verifiable Arithmetic: p = 67, q = 11, g = 64, x = 5, k = 7"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    ex2 = [
        ("1. Parameters & Keygen: ", "p = 67, q = 11 (11 divides 66), g = 64 (order 11 mod 67). Private key x = 5.\nPublic key y = g^x mod p = 64^5 mod 67 = 25."),
        ("2. Signing Hash H(m) = 9: ", "\n• Choose nonce k = 7. Compute r = (g^k mod p) mod q = (64^7 mod 67) mod 11 = 24 mod 11 = 2 ➔ r = 2\n• Modular inverse k^(-1) mod q via EEA: 7 · 8 = 56 ≡ 1 mod 11 ➔ k^(-1) = 8\n• s = k^(-1) · (H(m) + x · r) mod q = 8 · (9 + 5 · 2) mod 11 = 8 · 19 mod 11 = 8 · 8 = 64 ≡ 9 mod 11 ➔ s = 9\nSignature output: (r = 2, s = 9)."),
        ("3. Client Verification: ", "\n• Invert s mod q: w = 9^(-1) mod 11 = 5 (since 9 · 5 = 45 ≡ 1 mod 11)\n• u1 = H(m) · w mod q = 9 · 5 = 45 ≡ 1 mod 11 ➔ u1 = 1\n• u2 = r · w mod q = 2 · 5 = 10 mod 11 ➔ u2 = 10\n• v = ((g^u1 · y^u2) mod p) mod q = ((64^1 · 25^10) mod 67) mod 11 = (64 · 58 mod 67) mod 11 = 27 mod 11 = 2 ➔ v = 2"),
        ("Result: ", "v == r (2 == 2) ➔ SIGNATURE AUTHENTIC & VERIFIED!")
    ]
    for b_txt, n_txt in ex2:
        p = tf.add_paragraph()
        p.space_after = Pt(6)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 11: SIMPLE WORKED EXAMPLE 3 - ECDSA
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_slide_background(s11)
    add_header(s11, "Worked Example 3: ECDSA with Simple Numbers", "Live Numerical Verification")

    add_bento_card(s11, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), CARD_WHITE, SANGUINE_PRIMARY)
    tb = s11.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Hand-Verifiable Arithmetic: y² ≡ x³ + x + 1 mod 97, G = (0, 1), n = 97"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(10)

    ex3 = [
        ("1. Curve & Keygen: ", "Curve y² = x³ + x + 1 mod 97. Group order n = 97 (prime). Base G = (0, 1).\nWallet private key d = 7. Public key point Q = 7 · G = (75, 1)."),
        ("2. Signing Hash e = 26: ", "\n• Choose nonce k = 13. Curve point R = k · G = 13 · (0, 1) = (74, 13) ➔ r = 74 mod 97 = 74\n• Modular inverse k^(-1) mod n: 13^(-1) mod 97 = 15 (since 13 · 15 = 195 ≡ 1 mod 97)\n• s = k^(-1) · (e + d · r) mod n = 15 · (26 + 7 · 74) mod 97 = 15 · (26 + 33) = 15 · 59 = 885 ≡ 12 mod 97 ➔ s = 12\nSignature output: (r = 74, s = 12)."),
        ("3. Validator Verification: ", "\n• w = s^(-1) mod n = 12^(-1) mod 97 = 89 (since 12 · 89 = 1068 ≡ 1 mod 97)\n• u1 = e · w mod n = 26 · 89 = 2314 ≡ 83 mod 97\n• u2 = r · w mod n = 74 · 89 = 6586 ≡ 87 mod 97\n• Compute curve point P = u1 · G + u2 · Q = 83 · (0, 1) + 87 · (75, 1) = (74, 18)\n• Verification check: P.x mod n = 74 mod 97 = 74 == r!"),
        ("Result: ", "P.x matches r exactly ➔ TRANSACTION MINED TO LEDGER!")
    ]
    for b_txt, n_txt in ex3:
        p = tf.add_paragraph()
        p.space_after = Pt(6)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 12: COMPARISON TABLE & SUMMARY
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_slide_background(s12)
    add_header(s12, "Summary: The Public-Key Matrix at a Glance", "Review")

    add_bento_card(s12, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1))
    tb = s12.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Key Takeaways from Production Implementations"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SANGUINE_DEEP
    p.space_after = Pt(12)

    summary_bullets = [
        ("Diffie–Hellman (DH): ", "Essential for interactive confidential sessions. Solves the key distribution problem. Forms the basis of TLS 1.3, Signal, and SSH. Hardness based on Discrete Log Problem in modular integer fields."),
        ("Digital Signature Algorithm (DSA): ", "Historic FIPS 186 signature standard for software authenticity and code signing. Proves author identity and message integrity via the (r, s) tuple."),
        ("Elliptic Curve DSA (ECDSA): ", "The modern standard. Replaces integer exponentiation with curve point scalar multiplication. Eliminates sub-exponential index calculus attacks, reducing key lengths from 2048 to 256 bits for equivalent 128-bit security."),
        ("Critical Production Rule: ", "In both DSA and ECDSA, the nonce 'k' must be cryptographically random and NEVER reused. A single duplicate k across two signatures completely reveals the private key!"),
        ("The Core Insight: ", "Public-key cryptography does not hide information by obscuring data; it protects data with asymmetric mathematical trapdoors that require impossible compute to reverse.")
    ]
    for b_txt, n_txt in summary_bullets:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = SANGUINE_PRIMARY
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MAIN

    # Save presentation
    prs.save("RealWorld_Public_Key_Cryptography.pptx")
    prs.save("CipherCorp_Crypto_Algorithms.pptx")
    print("Presentations saved successfully!")

if __name__ == "__main__":
    create_presentation()

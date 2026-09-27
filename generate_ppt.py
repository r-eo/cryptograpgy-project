import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = pptx.Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    BG_DARK = RGBColor(11, 15, 25)        # #0B0F19
    CARD_BG = RGBColor(22, 30, 49)        # #161E31
    CARD_BORDER = RGBColor(37, 51, 82)    # #253352
    TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
    TEXT_DIM = RGBColor(100, 116, 139)    # #64748B
    CYAN = RGBColor(14, 165, 233)         # #0EA5E9
    PURPLE = RGBColor(168, 85, 247)       # #A855F7
    EMERALD = RGBColor(16, 185, 129)      # #10B981
    AMBER = RGBColor(245, 158, 11)        # #F59E0B
    INDIGO = RGBColor(99, 102, 241)       # #6366F1

    def add_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, accent_color=INDIGO):
        # Category Badge
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = accent_color

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_slide_background(s1)

    # Accent decorative box
    card1 = add_card(s1, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), INDIGO)
    card1.fill.fore_color.rgb = RGBColor(17, 24, 39)

    tb = s1.shapes.add_textbox(Inches(2.0), Inches(1.8), Inches(9.333), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "CIPHERCORP • CRYPTOGRAPHY LAB"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = "Public-Key Cryptography Demystified"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Diffie–Hellman (DH)  •  DSA  •  ECDSA"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = INDIGO
    p2.space_after = Pt(20)

    p3 = tf.add_paragraph()
    p3.text = "A simple, clear guide explaining the core algorithms, mathematical foundations, and complete step-by-step worked examples with small numbers."
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: THE TWO FUNDAMENTAL PROBLEMS
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_background(s2)
    add_header(s2, "The Two Fundamental Problems of Modern Cryptography", "Foundations")

    # Card 1: Key Agreement
    add_card(s2, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), CYAN)
    tb = s2.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Problem 1: Confidential Key Agreement"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(12)

    bullets1 = [
        ("The Challenge:", " How can two remote parties (e.g. Alice & Bob) agree on a shared secret key over an untrusted, publicly tapped wire where an eavesdropper (Eve) reads every packet?"),
        ("The Traditional Flaw:", " If you transmit the secret key, Eve intercepts it. If you don't transmit it, how can the other party decipher your messages?"),
        ("The Solution:", " Diffie-Hellman Key Exchange (1976). Both parties combine public parameters with private secrets using asymmetric one-way modular math."),
        ("Key Guarantee:", " An eavesdropper sees all public messages but cannot compute the shared key without solving the Discrete Logarithm Problem.")
    ]
    for bold_txt, norm_txt in bullets1:
        p = tf.add_paragraph()
        p.space_after = Pt(10)
        run1 = p.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        run2 = p.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED

    # Card 2: Digital Signatures
    add_card(s2, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), EMERALD)
    tb = s2.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Problem 2: Authenticity & Message Integrity"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = EMERALD
    p.space_after = Pt(12)

    bullets2 = [
        ("The Challenge:", " When receiving software updates, financial transactions, or contracts, how does a recipient prove who authored the message and guarantee it wasn't modified?"),
        ("The Traditional Flaw:", " Plain messages or checksums (like CRC32) can be modified by an attacker, who recalculates the checksum effortlessly."),
        ("The Solution:", " Digital Signatures (DSA & ECDSA). The signer uses a private key to mathematically bind their identity to the message hash."),
        ("Key Guarantee:", " Anyone with the public key can verify the signature, but nobody without the private key can forge it or alter a single bit.")
    ]
    for bold_txt, norm_txt in bullets2:
        p = tf.add_paragraph()
        p.space_after = Pt(10)
        run1 = p.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        run2 = p.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: DIFFIE-HELLMAN CONCEPT & INTUITION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_background(s3)
    add_header(s3, "Diffie–Hellman: The Concept & Intuition", "Algorithm 1: Key Agreement", CYAN)

    add_card(s3, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), CYAN)
    tb = s3.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "How Does Diffie–Hellman Work Without Transmitting the Secret?"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    dh_concepts = [
        ("1. The Color-Mixing Analogy: ", "Imagine Alice and Bob publicly agree on a common base color (say, Yellow). Alice privately adds secret Red paint to get Orange. Bob privately adds secret Blue paint to get Green. They exchange Orange and Green across the room in front of everyone. Finally, Alice adds her secret Red to Bob's Green, and Bob adds his secret Blue to Alice's Orange. Both arrive at the exact same Brown mixture! An onlooker sees Yellow, Orange, and Green, but cannot separate the mixed paints to deduce the secret colors."),
        ("2. Mathematical One-Way Trapdoor: ", "In mathematics, modular exponentiation acts like paint mixing: computing A = g^a mod p is extremely fast (using square-and-multiply), but reversing it—finding private exponent 'a' given A, g, and p—is computationally intractable. This is the Discrete Logarithm Problem."),
        ("3. The Shared Result: ", "Because powers multiply: (g^b)^a = g^(ab) = (g^a)^b mod p. Both parties compute the identical number g^(ab) mod p independently!"),
        ("4. What the Eavesdropper Sees: ", "Eve observes p, g, A = g^a mod p, and B = g^b mod p. But without private key 'a' or 'b', computing g^(ab) mod p directly from (g^a, g^b) is the Computational Diffie-Hellman (CDH) problem—believed to be as hard as computing discrete logs.")
    ]
    for bold_txt, norm_txt in dh_concepts:
        p = tf.add_paragraph()
        p.space_after = Pt(10)
        r1 = p.add_run()
        r1.text = bold_txt
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = CYAN
        r2 = p.add_run()
        r2.text = norm_txt
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: DIFFIE-HELLMAN MATHEMATICAL ALGORITHM
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_background(s4)
    add_header(s4, "Diffie–Hellman: Step-by-Step Mathematical Algorithm", "Algorithm 1: Specification", CYAN)

    steps_dh = [
        ("Step 1: Public Setup", "Agree publicly on a large prime modulus 'p' and a generator 'g' (primitive root modulo p). Both p and g are known to the whole world.", CYAN),
        ("Step 2: Private Exponent Choice", "Alice chooses private random integer 'a' where 2 ≤ a ≤ p - 2.\nBob chooses private random integer 'b' where 2 ≤ b ≤ p - 2.\nNeither secret is ever transmitted.", INDIGO),
        ("Step 3: Public Key Computation", "Alice computes public value: A = g^a mod p\nBob computes public value: B = g^b mod p\nComputed via binary square-and-multiply in O(log a) steps.", CYAN),
        ("Step 4: Public Exchange", "Alice sends A to Bob over the network.\nBob sends B to Alice over the network.\nEve intercepts p, g, A, and B, but knows neither a nor b.", AMBER),
        ("Step 5: Shared Secret Derivation", "Alice computes: s = B^a mod p\nBob computes: s = A^b mod p\nSince B^a = (g^b)^a = g^(ab) and A^b = (g^a)^b = g^(ab), both secrets match exactly: s_Alice = s_Bob!", EMERALD)
    ]

    card_w = Inches(2.25)
    gap = Inches(0.12)
    left_start = Inches(0.8)

    for i, (st_title, st_desc, col) in enumerate(steps_dh):
        c_left = left_start + i * (card_w + gap)
        add_card(s4, c_left, Inches(1.7), card_w, Inches(5.1), col)

        tb = s4.shapes.add_textbox(c_left + Inches(0.15), Inches(1.9), card_w - Inches(0.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = st_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_after = Pt(10)

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 5: DSA CONCEPT & ANATOMY OF A SIGNATURE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_background(s5)
    add_header(s5, "Digital Signature Algorithm (DSA): Concept & Anatomy", "Algorithm 2: Signatures", PURPLE)

    # Left card: Concept
    add_card(s5, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), PURPLE)
    tb = s5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Why DSA (FIPS 186)?"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = PURPLE
    p.space_after = Pt(12)

    bullets_dsa_c = [
        ("Purpose: ", "Published by NIST in 1991 to provide non-repudiation and tamper-evident signatures for electronic data and software updates."),
        ("Subgroup Efficiency: ", "Unlike plain RSA, DSA works inside a prime-order subgroup of size q dividing p - 1. This keeps signatures small while keeping the prime modulus p large for security."),
        ("Message Hashing: ", "Instead of signing huge files directly, DSA signs a fixed-length cryptographic hash H(m). Even a single bit change in the file yields an entirely different hash."),
        ("Signature Pair: ", "A DSA signature consists of two numbers: (r, s). Both are small integers modulo q.")
    ]
    for b_txt, n_txt in bullets_dsa_c:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # Right card: Anatomy
    add_card(s5, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), INDIGO)
    tb = s5.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Anatomy of the Signature (r, s)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = INDIGO
    p.space_after = Pt(12)

    anatomy_items = [
        ("The 'r' Component (Ephemeral Fingerprint):", "\nr = (g^k mod p) mod q\nComputed by picking a fresh random nonce k for every message. 'r' is the public image of nonce k reduced modulo q."),
        ("The 's' Component (Proof of Secret Key Possession):", "\ns = k^(-1) · (H(m) + x · r) mod q\nBinds the message hash H(m), private key x, and ephemeral nonce k. Calculated using the Extended Euclidean Algorithm for modular inverse k^(-1)."),
        ("CRITICAL RULE — Never Reuse Nonce k:", "\nIf a signer ever signs two distinct messages with the same k, any observer can perform simple modular subtraction and immediately compute the signer's private key x! (Famously caused the Sony PS3 security failure in 2010).")
    ]
    for b_txt, n_txt in anatomy_items:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = AMBER if "CRITICAL" in b_txt else TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 6: DSA MATHEMATICAL ALGORITHM
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_background(s6)
    add_header(s6, "DSA: The 3-Stage Mathematical Algorithm", "Algorithm 2: Specification", PURPLE)

    stages_dsa = [
        ("Stage 1: Domain & Keygen",
         "1. Choose prime p and prime divisor q such that q | (p - 1).\n"
         "2. Choose generator g = h^((p-1)/q) mod p > 1.\n"
         "3. Pick private key x ∈ [1, q - 1].\n"
         "4. Compute public key:\n   y = g^x mod p.\n\n"
         "Public parameters: (p, q, g, y)\nPrivate parameter: x", PURPLE),

        ("Stage 2: Signing H(m)",
         "1. Hash message m to get integer H(m).\n"
         "2. Choose secret random nonce k ∈ [1, q - 1].\n"
         "3. Compute:\n   r = (g^k mod p) mod q.\n   (If r == 0, pick new k).\n"
         "4. Compute modular inverse k^(-1) mod q using Extended Euclidean Algorithm.\n"
         "5. Compute:\n   s = k^(-1) · (H(m) + x · r) mod q.\n\n"
         "Signature output: (r, s)", CYAN),

        ("Stage 3: Verifying (r, s)",
         "Given public key y, message m, and signature (r, s):\n"
         "1. Verify 0 < r < q and 0 < s < q.\n"
         "2. Compute w = s^(-1) mod q.\n"
         "3. Compute u1 = H(m) · w mod q.\n"
         "4. Compute u2 = r · w mod q.\n"
         "5. Compute verification value:\n   v = ((g^u1 · y^u2) mod p) mod q.\n"
         "6. Test: If v == r, signature is VALID!", EMERALD)
    ]

    card_w = Inches(3.7)
    gap = Inches(0.3)
    left_start = Inches(0.8)

    for i, (st_title, st_desc, col) in enumerate(stages_dsa):
        c_left = left_start + i * (card_w + gap)
        add_card(s6, c_left, Inches(1.7), card_w, Inches(5.1), col)

        tb = s6.shapes.add_textbox(c_left + Inches(0.2), Inches(1.9), card_w - Inches(0.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = st_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_after = Pt(12)

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 7: ELLIPTIC CURVE CRYPTOGRAPHY (ECC) GEOMETRY
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_background(s7)
    add_header(s7, "Elliptic Curve Cryptography: Curved Geometry over Finite Fields", "Algorithm 3: ECC", EMERALD)

    add_card(s7, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), EMERALD)
    tb = s7.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "The Curve Equation & Finite Field"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = EMERALD
    p.space_after = Pt(12)

    ecc_pts = [
        ("Weierstrass Curve Equation:", " y² = x³ + ax + b (mod p)\nwhere 4a³ + 27b² ≢ 0 (mod p) ensures no cusps or self-intersections."),
        ("Finite Field Discrete Grid:", " Over real numbers ℝ, the curve is a smooth continuous loop. Over a finite field 𝔽_p, the curve becomes a discrete scatter plot of integer coordinates (x, y) where y² ≡ x³ + ax + b (mod p)."),
        ("Abelian Group Structure:", " All points on the curve plus an abstract 'Point at Infinity' 𝒪 form an algebraic abelian group with well-defined addition: P + Q = R.")
    ]
    for b_txt, n_txt in ecc_pts:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    add_card(s7, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), CYAN)
    tb = s7.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Point Addition & Point Doubling"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(12)

    geom_pts = [
        ("Case 1: Point Addition (P ≠ Q):", "\nDraw a straight line through P(x₁, y₁) and Q(x₂, y₂).\nSlope: λ = (y₂ - y₁) / (x₂ - x₁) mod p\nThe line intersects the curve at a 3rd point R'. Reflect R' across the x-axis to obtain P + Q = (x₃, y₃):\nx₃ = λ² - x₁ - x₂ mod p\ny₃ = λ(x₁ - x₃) - y₁ mod p"),
        ("Case 2: Point Doubling (P == Q):", "\nDraw the tangent line to the curve at point P(x₁, y₁).\nSlope: λ = (3x₁² + a) / (2y₁) mod p\nCalculate x₃, y₃ using the same reflection formulas."),
        ("Scalar Multiplication (k · P):", "\nComputed using the Double-and-Add algorithm (analogous to square-and-multiply) in O(log k) operations.")
    ]
    for b_txt, n_txt in geom_pts:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 8: ECDSA MATHEMATICAL ALGORITHM
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_background(s8)
    add_header(s8, "ECDSA: The Mathematical Algorithm", "Algorithm 3: Specification", EMERALD)

    stages_ecdsa = [
        ("Stage 1: Key Generation",
         "1. Choose elliptic curve E over 𝔽_p with parameters (a, b, p).\n"
         "2. Choose base generator point G(x_G, y_G) with prime order n (where n · G = 𝒪).\n"
         "3. Pick private key integer d ∈ [1, n - 1].\n"
         "4. Compute public key point:\n   Q = d · G\n   (via double-and-add scalar multiplication).\n\n"
         "Public: (p, a, b, G, n, Q)\nPrivate: d", PURPLE),

        ("Stage 2: Signing Hash e = H(m)",
         "1. Compute message hash e = H(m).\n"
         "2. Choose random ephemeral scalar k ∈ [1, n - 1].\n"
         "3. Compute curve point:\n   R = k · G = (x_R, y_R).\n"
         "4. Set r = x_R mod n. (If r == 0, pick new k).\n"
         "5. Compute modular inverse k^(-1) mod n.\n"
         "6. Compute:\n   s = k^(-1) · (e + d · r) mod n.\n\n"
         "Signature output: (r, s)", CYAN),

        ("Stage 3: Verifying (r, s)",
         "Given public key Q, message hash e, signature (r, s):\n"
         "1. Check 0 < r < n and 0 < s < n.\n"
         "2. Compute w = s^(-1) mod n.\n"
         "3. Compute u1 = e · w mod n.\n"
         "4. Compute u2 = r · w mod n.\n"
         "5. Compute curve point:\n   P = u1 · G + u2 · Q = (x_P, y_P).\n"
         "6. Test: If x_P mod n == r, signature is VALID!", EMERALD)
    ]

    card_w = Inches(3.7)
    gap = Inches(0.3)
    left_start = Inches(0.8)

    for i, (st_title, st_desc, col) in enumerate(stages_ecdsa):
        c_left = left_start + i * (card_w + gap)
        add_card(s8, c_left, Inches(1.7), card_w, Inches(5.1), col)

        tb = s8.shapes.add_textbox(c_left + Inches(0.2), Inches(1.9), card_w - Inches(0.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = st_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_after = Pt(12)

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 9: COMPARISON: DSA VS ECDSA
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_background(s9)
    add_header(s9, "Comparison: Why ECDSA Replaced Legacy DSA", "Analysis & Trade-offs", INDIGO)

    add_card(s9, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), INDIGO)
    tb = s9.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(11.1), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Key Size vs Security Level (NIST SP 800-57 Standards)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    comparison_bullets = [
        ("Why does ECDSA achieve equal security with vastly smaller keys? ", "In standard modular integer groups (DSA and RSA), index calculus attacks run in sub-exponential time: L_n[1/3, c]. To defend against sub-exponential algorithms, modulus p must be inflated to 2048 or 3072 bits. In contrast, on generic elliptic curves, no sub-exponential attack is known! The fastest known attack is Pollard's rho, which runs in fully exponential O(√n) time. Therefore, a 256-bit elliptic curve provides the exact same 128-bit security as a 3072-bit DSA key!"),
        ("Key & Signature Size Comparison: ", "\n• 128-bit Security (Current Industry Standard):\n  - Legacy DSA: 3072-bit public key, 512-bit signature\n  - Modern ECDSA (secp256k1 / P-256): 256-bit public key, 512-bit signature (8x to 12x smaller public key!)\n• 256-bit Security (Top Secret / Military Grade):\n  - Legacy DSA: 15,360-bit key (enormous computational overhead)\n  - Modern ECDSA: 521-bit curve (fast, compact, lightweight)"),
        ("Real-World Impact: ", "Smaller keys translate to lower network latency, minimal packet bloat in TLS handshakes, vastly lower memory usage, and longer battery life on smartphones, IoT devices, and hardware wallets (Bitcoin, Ethereum, Apple Pay, Signal).")
    ]
    for b_txt, n_txt in comparison_bullets:
        p = tf.add_paragraph()
        p.space_after = Pt(10)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = CYAN
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 10: WORKED EXAMPLE 1 - DIFFIE-HELLMAN
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_background(s10)
    add_header(s10, "Simple Worked Numerical Example: Diffie–Hellman", "Worked Example 1", CYAN)

    add_card(s10, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), CYAN)
    tb = s10.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Complete Hand-Verifiable Calculation: Prime p = 23, Generator g = 5"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(12)

    ex1_steps = [
        ("Step 1: Public Setup: ", "Alice and Bob publicly choose prime p = 23 and generator g = 5 (5 is a primitive root mod 23)."),
        ("Step 2: Private Exponent Choice: ", "Alice secretly chooses a = 6. Bob secretly chooses b = 15."),
        ("Step 3: Public Keys Computation: ", "\n• Alice calculates: A = g^a mod p = 5^6 mod 23\n  5^1 = 5; 5^2 = 25 ≡ 2; 5^4 = 2^2 = 4; 5^6 = 5^4 · 5^2 = 4 · 2 = 8 mod 23 ➔ A = 8\n• Bob calculates: B = g^b mod p = 5^15 mod 23\n  5^15 = (5^6)^2 · 5^3 = (8)^2 · 125 = 64 · 10 = 640 = 27 · 23 + 19 ≡ 19 mod 23 ➔ B = 19"),
        ("Step 4: Public Exchange: ", "Alice sends A = 8 to Bob. Bob sends B = 19 to Alice. Eve observes p=23, g=5, A=8, B=19."),
        ("Step 5: Shared Secret Derivation: ", "\n• Alice computes: s = B^a mod p = 19^6 mod 23\n  19 ≡ -4 mod 23 ➔ (-4)^6 = 16^3 = (-7)^3 = -343 = -15 · 23 + 2 ≡ 2 mod 23 ➔ s = 2\n• Bob computes: s = A^b mod p = 8^15 mod 23\n  8^2 = 64 ≡ 18 ≡ -5; 8^4 ≡ 25 ≡ 2; 8^8 ≡ 4; 8^15 = 8^8 · 8^4 · 8^2 · 8 = 4 · 2 · 18 · 8 = 1152 = 50 · 23 + 2 ≡ 2 mod 23 ➔ s = 2"),
        ("Outcome: ", "Both Alice and Bob arrived at identical shared secret s = 2! Eve has no easy way to find '2' without computing log_5(8) mod 23.")
    ]
    for b_txt, n_txt in ex1_steps:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 11: WORKED EXAMPLE 2 - DSA
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_slide_background(s11)
    add_header(s11, "Simple Worked Numerical Example: DSA", "Worked Example 2", PURPLE)

    add_card(s11, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), PURPLE)
    tb = s11.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Complete Hand-Verifiable Calculation: p = 67, q = 11, g = 64"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = PURPLE
    p.space_after = Pt(12)

    ex2_steps = [
        ("Parameters & Keygen: ", "p = 67 (prime), q = 11 (divides 67 - 1 = 66), g = 64 (order 11 mod 67 since 64^11 ≡ 1 mod 67).\nPrivate key x = 5. Public key y = g^x mod p = 64^5 mod 67 = 25."),
        ("Signing Message Hash H(m) = 9: ", "\n1. Signer chooses nonce k = 7.\n2. Compute r = (g^k mod p) mod q = (64^7 mod 67) mod 11 = (24) mod 11 = 2 ➔ r = 2.\n3. Compute modular inverse k^(-1) mod q:\n   7 · k^(-1) ≡ 1 mod 11 ➔ k^(-1) = 8 (since 7 · 8 = 56 = 5 · 11 + 1 ≡ 1).\n4. Compute s = k^(-1) · (H(m) + x · r) mod q = 8 · (9 + 5 · 2) mod 11 = 8 · (19) mod 11 = 8 · 8 = 64 ≡ 9 mod 11 ➔ s = 9.\nSignature output: (r = 2, s = 9)."),
        ("Verification Process by Recipient: ", "\n1. Recipient computes w = s^(-1) mod q = 9^(-1) mod 11 = 5 (since 9 · 5 = 45 ≡ 1 mod 11).\n2. Compute u1 = H(m) · w mod q = 9 · 5 = 45 ≡ 1 mod 11 ➔ u1 = 1.\n3. Compute u2 = r · w mod q = 2 · 5 = 10 mod 11 ➔ u2 = 10.\n4. Compute verification value v = ((g^u1 · y^u2) mod p) mod q:\n   g^u1 mod p = 64^1 = 64 mod 67;\n   y^u2 mod p = 25^10 mod 67 = 58 mod 67;\n   g^u1 · y^u2 mod p = 64 · 58 = 3712 = 55 · 67 + 27 ≡ 27 mod 67;\n   v = 27 mod 11 = 2 ➔ v = 2.\n5. Test: v == r (2 == 2) ➔ SIGNATURE VALID!"),
        ("Tamper Test: ", "If an attacker changes H(m) from 9 to 8: u1 becomes 8 · 5 = 40 ≡ 7 mod 11, leading to v = 5 ≠ 2. Signature instantly rejected!")
    ]
    for b_txt, n_txt in ex2_steps:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 12: WORKED EXAMPLE 3 - ECDSA
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_slide_background(s12)
    add_header(s12, "Simple Worked Numerical Example: ECDSA", "Worked Example 3", EMERALD)

    add_card(s12, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), EMERALD)
    tb = s12.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Complete Hand-Verifiable Calculation: y² ≡ x³ + x + 1 mod 97, G = (0, 1), n = 97"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = EMERALD
    p.space_after = Pt(12)

    ex3_steps = [
        ("Domain Setup & Keygen: ", "Curve: y² ≡ x³ + x + 1 (mod 97). Group order n = 97 (prime).\nBase Generator G = (0, 1). Verify G is on curve: 1² = 1; 0³ + 0 + 1 = 1 ≡ 1 mod 97.\nSigner chooses private key d = 7.\nPublic key point Q = 7 · G = (75, 1) (computed via double-and-add point addition)."),
        ("Signing Message Hash e = 26: ", "\n1. Signer picks nonce k = 13.\n2. Computes curve point R = k · G = 13 · (0, 1) = (74, 13).\n3. Set r = R.x mod n = 74 mod 97 ➔ r = 74.\n4. Compute k^(-1) mod n = 13^(-1) mod 97 = 15 (since 13 · 15 = 195 = 2 · 97 + 1 ≡ 1 mod 97).\n5. Compute s = k^(-1) · (e + d · r) mod n = 15 · (26 + 7 · 74) mod 97\n   7 · 74 = 518 ≡ 33 mod 97 ➔ 26 + 33 = 59 ➔ 15 · 59 = 885 = 9 · 97 + 12 ≡ 12 mod 97 ➔ s = 12.\nSignature output: (r = 74, s = 12)."),
        ("Recipient Verification: ", "\n1. Recipient calculates w = s^(-1) mod n = 12^(-1) mod 97 = 89 (since 12 · 89 = 1068 = 11 · 97 + 1 ≡ 1).\n2. u1 = e · w mod n = 26 · 89 = 2314 ≡ 83 mod 97.\n3. u2 = r · w mod n = 74 · 89 = 6586 ≡ 87 mod 97.\n4. Recipient computes curve point P = u1 · G + u2 · Q = 83 · (0, 1) + 87 · (75, 1) = (74, 18).\n5. Test: P.x mod n == r (74 == 74) ➔ SIGNATURE VALID!"),
        ("Geometric Elegance: ", "Notice P.x matches r exactly. The point arithmetic over F_97 replaces modular exponentiation over huge integers.")
    ]
    for b_txt, n_txt in ex3_steps:
        p = tf.add_paragraph()
        p.space_after = Pt(8)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 13: SUMMARY & KEY TAKEAWAYS
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_slide_background(s13)
    add_header(s13, "Summary & Key Takeaways", "Review", INDIGO)

    add_card(s13, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), INDIGO)
    tb = s13.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "The Modern Cryptographic Toolkit at a Glance"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    summary_pts = [
        ("1. Diffie–Hellman (DH): ", "The foundation of interactive secure channels. Enables two parties to negotiate an ephemeral symmetric key over a public network. Used in TLS 1.3, SSH, Signal Protocol, and VPNs."),
        ("2. Digital Signature Algorithm (DSA): ", "The historic standard for non-repudiation and integrity based on discrete logarithms in modular integer subgroups. Established the standard signature structure (r, s)."),
        ("3. Elliptic Curve Digital Signature Algorithm (ECDSA): ", "Transfers discrete logarithm hardness to abelian curve point groups. Eliminates sub-exponential index calculus attacks, reducing required key sizes by up to 88% for identical security. Powers Bitcoin, Ethereum, iOS Secure Enclave, and modern TLS certificates."),
        ("4. Ephemeral Nonce Security: ", "In both DSA and ECDSA, never reuse nonce k. A single collision instantly reveals the signer's private key."),
        ("5. Pure Mathematics in Action: ", "Modular arithmetic, group generators, the Extended Euclidean Algorithm, and elliptic curve geometry provide the impenetrable mathematical shield protecting all digital privacy on earth.")
    ]
    for b_txt, n_txt in summary_pts:
        p = tf.add_paragraph()
        p.space_after = Pt(10)
        r1 = p.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = CYAN
        r2 = p.add_run()
        r2.text = n_txt
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_MUTED

    # Save presentation
    output_filename = "CipherCorp_Crypto_Algorithms.pptx"
    prs.save(output_filename)
    print(f"Presentation saved successfully as '{output_filename}' ({len(prs.slides)} slides)!")

if __name__ == "__main__":
    create_presentation()

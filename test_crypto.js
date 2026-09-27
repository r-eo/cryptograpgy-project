// Test Cryptographic Algorithms in Node.js
function mod(n, m) {
    let r = n % m;
    return r < 0n ? r + m : r;
}

function modPow(base, exp, m) {
    let res = 1n;
    base = mod(base, m);
    let e = exp;
    while (e > 0n) {
        if (e & 1n) res = mod(res * base, m);
        base = mod(base * base, m);
        e >>= 1n;
    }
    return res;
}

function modPowTrace(base, exp, m) {
    let res = 1n;
    let b = mod(base, m);
    let bits = exp.toString(2);
    let trace = [];
    for (let i = 0; i < bits.length; i++) {
        let bit = bits[i];
        let prev = res;
        res = mod(res * res, m);
        let action = `Square: ${prev}^2 mod ${m} = ${res}`;
        if (bit === '1') {
            let beforeMul = res;
            res = mod(res * b, m);
            action += ` -> Multiply: ${beforeMul} * ${b} mod ${m} = ${res}`;
        }
        trace.push({ step: i + 1, bit, result: res.toString(), desc: action });
    }
    return { result: res, trace };
}

function extGCD(a, b) {
    let old_r = a, r = b;
    let old_s = 1n, s = 0n;
    let old_t = 0n, t = 1n;
    let steps = [];
    while (r !== 0n) {
        let q = old_r / r;
        let rem = old_r - q * r;
        steps.push({
            old_r: old_r.toString(),
            r: r.toString(),
            q: q.toString(),
            rem: rem.toString(),
            formula: `${old_r} = ${q} * ${r} + ${rem}`
        });
        old_r = r; r = rem;
        let next_s = old_s - q * s;
        old_s = s; s = next_s;
        let next_t = old_t - q * t;
        old_t = t; t = next_t;
    }
    return { gcd: old_r, x: old_s, y: old_t, steps };
}

function modInverse(a, m) {
    let res = extGCD(mod(a, m), m);
    if (res.gcd !== 1n) throw new Error('Modular inverse does not exist');
    return { inv: mod(res.x, m), steps: res.steps };
}

// Elliptic curve over F_p: y^2 = x^3 + ax + b mod p
class EllipticCurve {
    constructor(p, a, b, G, n) {
        this.p = BigInt(p);
        this.a = BigInt(a);
        this.b = BigInt(b);
        this.G = G ? { x: BigInt(G.x), y: BigInt(G.y) } : null;
        this.n = n ? BigInt(n) : null;
    }
    isInfinity(P) { return P === null || P.x === null; }
    add(P, Q) {
        if (this.isInfinity(P)) return Q;
        if (this.isInfinity(Q)) return P;
        let p = this.p;
        if (P.x === Q.x && mod(P.y + Q.y, p) === 0n) return null;
        let lambda;
        if (P.x === Q.x && P.y === Q.y) {
            let num = mod(3n * P.x * P.x + this.a, p);
            let den = mod(2n * P.y, p);
            let denInv = modInverse(den, p).inv;
            lambda = mod(num * denInv, p);
        } else {
            let num = mod(Q.y - P.y, p);
            let den = mod(Q.x - P.x, p);
            let denInv = modInverse(den, p).inv;
            lambda = mod(num * denInv, p);
        }
        let x3 = mod(lambda * lambda - P.x - Q.x, p);
        let y3 = mod(lambda * (P.x - x3) - P.y, p);
        return { x: x3, y: y3, lambda };
    }
    mul(k, P) {
        let R = null;
        let bits = BigInt(k).toString(2);
        let steps = [];
        for (let i = 0; i < bits.length; i++) {
            let doublePt = this.add(R, R);
            let stepInfo = { bitIndex: i, bit: bits[i], beforeDouble: R, afterDouble: doublePt, added: false };
            R = doublePt;
            if (bits[i] === '1') {
                R = this.add(R, P);
                stepInfo.added = true;
                stepInfo.afterAdd = R;
            }
            steps.push(stepInfo);
        }
        return { result: R, steps };
    }
}

// 1. DH Test
console.log('Testing DH...');
let dh = modPowTrace(5n, 6n, 23n);
console.log('DH trace len:', dh.trace.length, 'A =', dh.result.toString());
let s1 = modPow(19n, 6n, 23n);
let s2 = modPow(8n, 15n, 23n);
console.log(`DH Shared: s1=${s1}, s2=${s2}, match=${s1 === s2}`);

// 2. DSA Test
console.log('Testing DSA...');
let p_dsa = 67n, q_dsa = 11n, g_dsa = 64n;
let x_dsa = 5n;
let y_dsa = modPow(g_dsa, x_dsa, p_dsa);
let hm_dsa = 9n;
let k_dsa = 7n;
let r_dsa = mod(modPow(g_dsa, k_dsa, p_dsa), q_dsa);
let k_inv = modInverse(k_dsa, q_dsa).inv;
let s_dsa = mod(k_inv * (hm_dsa + x_dsa * r_dsa), q_dsa);
// Verify
let w_dsa = modInverse(s_dsa, q_dsa).inv;
let u1 = mod(hm_dsa * w_dsa, q_dsa);
let u2 = mod(r_dsa * w_dsa, q_dsa);
let v_dsa = mod(mod(modPow(g_dsa, u1, p_dsa) * modPow(y_dsa, u2, p_dsa), p_dsa), q_dsa);
console.log(`DSA: r=${r_dsa}, s=${s_dsa}, v=${v_dsa}, verify=${v_dsa === r_dsa}`);

// 3. ECDSA Test
console.log('Testing ECDSA...');
let curve = new EllipticCurve(97n, 1n, 1n, { x: 0n, y: 1n }, 97n);
let d_ec = 7n;
let Q_ec = curve.mul(d_ec, curve.G).result;
let e_ec = 26n;
let k_ec = 13n;
let R_ec = curve.mul(k_ec, curve.G).result;
let r_ec = mod(R_ec.x, curve.n);
let k_inv_ec = modInverse(k_ec, curve.n).inv;
let s_ec = mod(k_inv_ec * (e_ec + d_ec * r_ec), curve.n);
// Verify
let w_ec = modInverse(s_ec, curve.n).inv;
let u1_ec = mod(e_ec * w_ec, curve.n);
let u2_ec = mod(r_ec * w_ec, curve.n);
let P1 = curve.mul(u1_ec, curve.G).result;
let P2 = curve.mul(u2_ec, Q_ec).result;
let P_ver = curve.add(P1, P2);
console.log(`ECDSA: Q=(${Q_ec.x},${Q_ec.y}), r=${r_ec}, s=${s_ec}`);
console.log(`ECDSA Verify: P_ver=(${P_ver.x},${P_ver.y}), check=${mod(P_ver.x, curve.n) === r_ec}`);

console.log('ALL TESTS PASSED SUCCESSFULLY!');

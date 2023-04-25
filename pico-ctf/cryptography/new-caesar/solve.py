import argparse
import string
import sys

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain: str) -> str:
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(enc: str) -> str:
    plain = ""
    for i in range(0, len(enc), 2):
        lhs = ALPHABET.index(enc[i])
        rhs = ALPHABET.index(enc[i + 1])
        plain += chr((lhs << 4) + rhs)
    return plain


def shift(c: chr, k: chr) -> chr:
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshift(c: chr, k: chr) -> chr:
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def encode(plain: str, key: str) -> str:
    assert all(k in ALPHABET for k in key)
    assert len(key) == 1

    b16 = b16_encode(plain)
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
    return enc


def decode(enc: str, key: str) -> str:
    assert all(k in ALPHABET for k in key)
    assert len(key) == 1

    b16 = ""
    for i, c in enumerate(enc):
        b16 += unshift(c, key[i % len(key)])
    plain = b16_decode(b16)
    return plain


def handle_encode(args):
    input_str = sys.stdin.read().strip()
    enc = encode(input_str, args.key)
    sys.stdout.write(enc)


def handle_decode(args):
    input_str = sys.stdin.read().strip()
    plain = decode(input_str, args.key)
    sys.stdout.write(plain)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-k",
        "--key",
        type=str,
        required=True,
        dest="key",
        help="the key used in the cypher",
    )

    subparsers = parser.add_subparsers(required=True)

    parser_encode = subparsers.add_parser("encode")
    parser_encode.set_defaults(func=handle_encode)

    parser_decode = subparsers.add_parser("decode")
    parser_decode.set_defaults(func=handle_decode)

    args = parser.parse_args()
    args.func(args)

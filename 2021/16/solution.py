B = ""
with open("input") as f:
    for letter in f.readline().strip():
        B += bin(int(letter, 16))[2:].zfill(4)


def parse_literal(P):
    sbit = B[P]
    parts = []
    while True:
        parts.append(B[P + 1 : P + 5])
        P += 5

        if sbit == "0":
            break

        sbit = B[P]

    num = int("".join(parts), 2)

    return num, P


def parse_operator(P, t):
    I = B[P]
    P += 1

    length = None
    packets = []
    if I == "0":
        length = int(B[P : P + 15], 2)
        P += 15
        end = length + P

        while P < end:
            P, version, ptype, num = parse_packet(P, 0)
            packets.append(num)
    else:
        subpacks = int(B[P : P + 11], 2)
        P += 11

        for _ in range(subpacks):
            P, version, ptype, num = parse_packet(P, 0)
            packets.append(num)

    num = 0
    if t == 0:
        num = sum(packets)
    elif t == 1:
        num = 1
        for p in packets:
            num *= p
    elif t == 2:
        num = min(packets)
    elif t == 3:
        num = max(packets)
    elif t == 5:
        num = 1 if packets[0] > packets[1] else 0
    elif t == 6:
        num = 1 if packets[0] < packets[1] else 0
    elif t == 7:
        num = 1 if packets[0] == packets[1] else 0

    return num, P


VC = 0


def parse_packet(P, num):
    global VC

    version = int(B[P : P + 3], 2)
    P += 3
    VC += version

    ptype = int(B[P : P + 3], 2)
    P += 3

    if ptype == 4:
        num2, P = parse_literal(P)
    else:
        num2, P = parse_operator(P, ptype)

    num += num2

    return P, version, ptype, num2


print(parse_packet(0, 0))

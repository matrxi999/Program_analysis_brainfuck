import sys

def main():
    tape = [0] * 30000  # Initialize tape
    pointer = 0

    tape[0] = 14
    tape[1] = 45
    tape[3] = 1
    tape[5] = 51
    tape[6] = 57
    tape[9] = 1
    tape[11] = 1
    tape[12] = 4
    tape[16] = 2
    tape[20] = 4
    tape[24] = 4
    tape[28] = 1
    tape[32] = 11
    tape[36] = 4
    tape[40] = 7
    tape[44] = 11
    tape[48] = 12
    tape[52] = 2
    tape[56] = 6
    tape[60] = 11
    tape[64] = 26
    tape[68] = 6
    tape[72] = 31
    tape[76] = 14
    tape[80] = 9
    tape[84] = 3
    tape[88] = 6
    tape[92] = 29
    tape[96] = 29
    tape[100] = 37
    tape[104] = 13
    tape[108] = 20
    tape[112] = 48
    tape[116] = 26
    tape[120] = 36
    tape[124] = 32
    tape[128] = 24
    tape[132] = 38
    tape[136] = 12
    tape[140] = 11
    tape[144] = 67
    tape[148] = 15
    tape[152] = 59
    tape[156] = 19
    tape[160] = 51
    tape[164] = 23
    tape[168] = 43
    tape[172] = 27
    tape[176] = 35
    tape[180] = 31
    tape[184] = 27
    tape[188] = 35
    tape[192] = 19
    tape[196] = 39
    tape[200] = 11
    tape[204] = 43
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[1] = 46
    print(chr(tape[1]), end='')
    tape[0] = 13
    tape[1] = 0
    tape[5] = 49
    tape[11] = 4
    tape[12] = 1
    tape[16] = 1
    tape[20] = 2
    tape[24] = 6
    tape[28] = 7
    tape[32] = 5
    tape[36] = 9
    tape[40] = 13
    tape[44] = 2
    tape[48] = 17
    tape[52] = 13
    tape[56] = 7
    tape[60] = 14
    tape[64] = 10
    tape[68] = 9
    tape[72] = 16
    tape[76] = 33
    tape[80] = 29
    tape[88] = 32
    tape[92] = 26
    tape[96] = 5
    tape[100] = 16
    tape[104] = 27
    tape[108] = 35
    tape[112] = 11
    tape[116] = 49
    tape[120] = 13
    tape[124] = 27
    tape[128] = 6
    tape[132] = 25
    tape[136] = 18
    tape[140] = 5
    tape[144] = 16
    tape[148] = 3
    tape[152] = 69
    tape[156] = 36
    tape[160] = 20
    tape[164] = 43
    tape[168] = 7
    tape[172] = 46
    tape[176] = 2
    tape[180] = 45
    tape[184] = 49
    tape[188] = 86
    tape[192] = 45
    tape[196] = 79
    tape[200] = 54
    tape[204] = 68
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 12
    tape[5] = 52
    tape[11] = 0
    tape[12] = 7
    tape[16] = 3
    tape[20] = 3
    tape[24] = 1
    tape[28] = 3
    tape[32] = 3
    tape[36] = 2
    tape[40] = 4
    tape[44] = 17
    tape[48] = 13
    tape[52] = 19
    tape[60] = 21
    tape[64] = 26
    tape[68] = 11
    tape[72] = 28
    tape[76] = 16
    tape[80] = 8
    tape[88] = 16
    tape[92] = 37
    tape[96] = 21
    tape[100] = 39
    tape[104] = 6
    tape[108] = 12
    tape[112] = 50
    tape[116] = 23
    tape[120] = 11
    tape[124] = 34
    tape[128] = 22
    tape[132] = 17
    tape[136] = 14
    tape[140] = 42
    tape[144] = 51
    tape[148] = 22
    tape[152] = 63
    tape[156] = 22
    tape[160] = 11
    tape[164] = 50
    tape[168] = 62
    tape[172] = 74
    tape[176] = 12
    tape[180] = 15
    tape[184] = 13
    tape[188] = 84
    tape[192] = 3
    tape[196] = 13
    tape[200] = 19
    tape[204] = 1
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 11
    tape[5] = 48
    tape[11] = 7
    tape[12] = 1
    tape[16] = 1
    tape[20] = 2
    tape[24] = 3
    tape[28] = 5
    tape[32] = 7
    tape[40] = 7
    tape[44] = 11
    tape[48] = 7
    tape[52] = 2
    tape[56] = 8
    tape[60] = 2
    tape[64] = 11
    tape[68] = 1
    tape[72] = 18
    tape[76] = 4
    tape[80] = 2
    tape[84] = 23
    tape[88] = 35
    tape[92] = 23
    tape[96] = 33
    tape[100] = 14
    tape[108] = 15
    tape[112] = 31
    tape[116] = 19
    tape[120] = 19
    tape[124] = 47
    tape[128] = 16
    tape[132] = 10
    tape[136] = 38
    tape[140] = 59
    tape[144] = 44
    tape[148] = 60
    tape[152] = 4
    tape[156] = 29
    tape[160] = 26
    tape[164] = 18
    tape[168] = 20
    tape[172] = 45
    tape[176] = 29
    tape[180] = 14
    tape[184] = 34
    tape[188] = 63
    tape[192] = 67
    tape[196] = 75
    tape[200] = 86
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 10
    tape[5] = 55
    tape[11] = 0
    tape[12] = 5
    tape[24] = 4
    tape[28] = 9
    tape[32] = 3
    tape[40] = 5
    tape[44] = 1
    tape[48] = 5
    tape[52] = 13
    tape[56] = 3
    tape[60] = 13
    tape[64] = 21
    tape[68] = 18
    tape[72] = 16
    tape[76] = 31
    tape[80] = 11
    tape[84] = 3
    tape[88] = 7
    tape[92] = 28
    tape[96] = 2
    tape[100] = 42
    tape[104] = 5
    tape[108] = 43
    tape[112] = 45
    tape[116] = 6
    tape[120] = 16
    tape[124] = 36
    tape[128] = 34
    tape[132] = 31
    tape[136] = 53
    tape[140] = 38
    tape[144] = 8
    tape[148] = 10
    tape[152] = 31
    tape[156] = 25
    tape[160] = 71
    tape[164] = 17
    tape[168] = 15
    tape[172] = 64
    tape[176] = 26
    tape[180] = 4
    tape[184] = 32
    tape[188] = 65
    tape[192] = 58
    tape[196] = 20
    tape[200] = 36
    tape[204] = 2
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 9
    tape[5] = 48
    tape[11] = 4
    tape[12] = 6
    tape[16] = 2
    tape[20] = 1
    tape[24] = 1
    tape[28] = 1
    tape[32] = 11
    tape[36] = 6
    tape[40] = 12
    tape[44] = 12
    tape[48] = 16
    tape[52] = 7
    tape[56] = 12
    tape[60] = 22
    tape[64] = 3
    tape[68] = 14
    tape[72] = 28
    tape[76] = 30
    tape[80] = 14
    tape[88] = 22
    tape[92] = 36
    tape[96] = 34
    tape[100] = 20
    tape[104] = 41
    tape[108] = 9
    tape[112] = 33
    tape[116] = 26
    tape[120] = 42
    tape[124] = 10
    tape[128] = 46
    tape[132] = 15
    tape[136] = 10
    tape[140] = 51
    tape[144] = 5
    tape[148] = 23
    tape[152] = 11
    tape[156] = 22
    tape[160] = 47
    tape[164] = 8
    tape[168] = 63
    tape[172] = 80
    tape[176] = 2
    tape[180] = 74
    tape[184] = 12
    tape[188] = 85
    tape[192] = 60
    tape[196] = 5
    tape[200] = 95
    tape[204] = 11
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 8
    tape[5] = 52
    tape[11] = 5
    tape[12] = 5
    tape[16] = 3
    tape[20] = 3
    tape[28] = 8
    tape[32] = 7
    tape[36] = 12
    tape[44] = 6
    tape[48] = 12
    tape[52] = 13
    tape[60] = 25
    tape[64] = 10
    tape[68] = 16
    tape[72] = 1
    tape[76] = 21
    tape[80] = 10
    tape[84] = 24
    tape[88] = 17
    tape[92] = 34
    tape[96] = 32
    tape[100] = 27
    tape[104] = 5
    tape[108] = 8
    tape[112] = 40
    tape[116] = 50
    tape[120] = 19
    tape[124] = 36
    tape[128] = 19
    tape[132] = 50
    tape[136] = 28
    tape[140] = 55
    tape[144] = 9
    tape[148] = 49
    tape[152] = 30
    tape[156] = 66
    tape[160] = 18
    tape[164] = 33
    tape[168] = 30
    tape[172] = 23
    tape[176] = 11
    tape[180] = 6
    tape[184] = 24
    tape[188] = 73
    tape[192] = 79
    tape[196] = 41
    tape[200] = 13
    tape[204] = 5
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 7
    tape[5] = 53
    tape[12] = 3
    tape[16] = 1
    tape[20] = 5
    tape[24] = 5
    tape[28] = 1
    tape[32] = 2
    tape[36] = 6
    tape[40] = 10
    tape[44] = 5
    tape[48] = 1
    tape[52] = 8
    tape[56] = 20
    tape[60] = 13
    tape[64] = 13
    tape[68] = 22
    tape[72] = 20
    tape[80] = 4
    tape[84] = 33
    tape[88] = 6
    tape[92] = 14
    tape[96] = 12
    tape[100] = 28
    tape[104] = 42
    tape[108] = 48
    tape[112] = 8
    tape[116] = 7
    tape[120] = 44
    tape[124] = 38
    tape[128] = 15
    tape[132] = 52
    tape[136] = 15
    tape[140] = 62
    tape[144] = 14
    tape[148] = 4
    tape[152] = 36
    tape[156] = 67
    tape[160] = 21
    tape[164] = 65
    tape[168] = 35
    tape[172] = 6
    tape[176] = 18
    tape[180] = 51
    tape[184] = 63
    tape[188] = 76
    tape[192] = 14
    tape[196] = 6
    tape[200] = 26
    tape[204] = 41
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 6
    tape[11] = 2
    tape[12] = 8
    tape[16] = 2
    tape[20] = 4
    tape[24] = 7
    tape[28] = 3
    tape[32] = 9
    tape[36] = 9
    tape[40] = 2
    tape[44] = 16
    tape[48] = 12
    tape[52] = 19
    tape[56] = 8
    tape[60] = 25
    tape[64] = 3
    tape[68] = 23
    tape[72] = 16
    tape[76] = 4
    tape[80] = 15
    tape[84] = 11
    tape[88] = 14
    tape[92] = 30
    tape[96] = 26
    tape[100] = 40
    tape[104] = 16
    tape[108] = 44
    tape[112] = 46
    tape[116] = 8
    tape[120] = 3
    tape[124] = 2
    tape[128] = 53
    tape[132] = 31
    tape[136] = 16
    tape[140] = 35
    tape[144] = 31
    tape[148] = 32
    tape[152] = 25
    tape[156] = 3
    tape[164] = 14
    tape[168] = 46
    tape[172] = 52
    tape[176] = 5
    tape[180] = 32
    tape[184] = 22
    tape[188] = 28
    tape[192] = 40
    tape[196] = 51
    tape[200] = 91
    tape[204] = 49
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 5
    tape[5] = 50
    tape[11] = 8
    tape[12] = 3
    tape[16] = 1
    tape[20] = 5
    tape[24] = 2
    tape[28] = 9
    tape[32] = 3
    tape[36] = 6
    tape[40] = 9
    tape[44] = 9
    tape[48] = 16
    tape[52] = 13
    tape[56] = 7
    tape[60] = 4
    tape[64] = 8
    tape[68] = 26
    tape[72] = 29
    tape[76] = 1
    tape[80] = 3
    tape[84] = 10
    tape[88] = 34
    tape[92] = 15
    tape[96] = 40
    tape[100] = 24
    tape[104] = 10
    tape[108] = 19
    tape[112] = 17
    tape[116] = 18
    tape[120] = 21
    tape[124] = 11
    tape[128] = 39
    tape[132] = 46
    tape[136] = 57
    tape[140] = 20
    tape[144] = 45
    tape[148] = 55
    tape[152] = 21
    tape[156] = 59
    tape[160] = 14
    tape[164] = 54
    tape[168] = 59
    tape[172] = 12
    tape[176] = 83
    tape[180] = 56
    tape[184] = 37
    tape[188] = 60
    tape[192] = 44
    tape[196] = 83
    tape[200] = 39
    tape[204] = 31
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 4
    tape[5] = 56
    tape[11] = 2
    tape[12] = 9
    tape[24] = 3
    tape[28] = 3
    tape[32] = 9
    tape[36] = 4
    tape[40] = 11
    tape[44] = 10
    tape[48] = 12
    tape[52] = 7
    tape[56] = 16
    tape[60] = 7
    tape[64] = 17
    tape[68] = 10
    tape[72] = 10
    tape[76] = 2
    tape[80] = 23
    tape[84] = 19
    tape[88] = 19
    tape[92] = 41
    tape[96] = 30
    tape[100] = 29
    tape[104] = 44
    tape[108] = 25
    tape[112] = 35
    tape[116] = 12
    tape[120] = 29
    tape[124] = 17
    tape[128] = 38
    tape[132] = 12
    tape[136] = 49
    tape[140] = 34
    tape[144] = 18
    tape[148] = 65
    tape[152] = 24
    tape[156] = 33
    tape[160] = 56
    tape[164] = 58
    tape[168] = 30
    tape[172] = 30
    tape[176] = 53
    tape[180] = 82
    tape[184] = 62
    tape[188] = 80
    tape[192] = 39
    tape[196] = 7
    tape[200] = 78
    tape[204] = 46
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 3
    tape[5] = 50
    tape[11] = 8
    tape[20] = 2
    tape[24] = 4
    tape[28] = 4
    tape[32] = 8
    tape[36] = 11
    tape[40] = 1
    tape[44] = 2
    tape[48] = 10
    tape[52] = 13
    tape[60] = 15
    tape[64] = 1
    tape[68] = 5
    tape[72] = 29
    tape[76] = 28
    tape[80] = 2
    tape[84] = 33
    tape[88] = 5
    tape[92] = 2
    tape[96] = 36
    tape[100] = 4
    tape[104] = 34
    tape[108] = 35
    tape[116] = 32
    tape[120] = 54
    tape[124] = 48
    tape[128] = 27
    tape[132] = 50
    tape[136] = 1
    tape[140] = 10
    tape[144] = 17
    tape[148] = 27
    tape[152] = 18
    tape[156] = 65
    tape[160] = 39
    tape[164] = 59
    tape[168] = 35
    tape[172] = 35
    tape[176] = 51
    tape[180] = 1
    tape[184] = 12
    tape[188] = 68
    tape[192] = 80
    tape[196] = 15
    tape[200] = 4
    tape[204] = 1
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 2
    tape[5] = 56
    tape[12] = 5
    tape[20] = 5
    tape[24] = 7
    tape[28] = 9
    tape[32] = 9
    tape[40] = 11
    tape[44] = 16
    tape[48] = 1
    tape[52] = 10
    tape[56] = 4
    tape[60] = 16
    tape[64] = 15
    tape[68] = 12
    tape[72] = 25
    tape[76] = 32
    tape[80] = 12
    tape[84] = 10
    tape[88] = 22
    tape[92] = 12
    tape[96] = 31
    tape[100] = 32
    tape[104] = 29
    tape[108] = 37
    tape[112] = 9
    tape[116] = 29
    tape[120] = 48
    tape[124] = 44
    tape[128] = 5
    tape[132] = 10
    tape[136] = 2
    tape[140] = 27
    tape[144] = 61
    tape[148] = 41
    tape[152] = 30
    tape[156] = 57
    tape[160] = 13
    tape[164] = 70
    tape[168] = 7
    tape[172] = 5
    tape[176] = 79
    tape[180] = 44
    tape[184] = 68
    tape[188] = 70
    tape[192] = 69
    tape[196] = 48
    tape[200] = 79
    tape[204] = 2
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 1
    tape[11] = 5
    tape[12] = 3
    tape[20] = 2
    tape[24] = 6
    tape[28] = 7
    tape[32] = 11
    tape[36] = 3
    tape[40] = 1
    tape[44] = 8
    tape[48] = 14
    tape[56] = 1
    tape[60] = 17
    tape[64] = 8
    tape[68] = 10
    tape[72] = 2
    tape[76] = 24
    tape[80] = 7
    tape[84] = 17
    tape[88] = 15
    tape[92] = 9
    tape[96] = 24
    tape[100] = 33
    tape[104] = 26
    tape[108] = 32
    tape[112] = 30
    tape[116] = 25
    tape[120] = 43
    tape[124] = 33
    tape[128] = 12
    tape[132] = 30
    tape[136] = 43
    tape[140] = 6
    tape[144] = 23
    tape[148] = 7
    tape[152] = 71
    tape[156] = 50
    tape[160] = 47
    tape[164] = 25
    tape[168] = 61
    tape[172] = 41
    tape[176] = 13
    tape[180] = 5
    tape[184] = 73
    tape[188] = 1
    tape[192] = 5
    tape[196] = 29
    tape[200] = 13
    tape[204] = 11
    tape[208] = 21
    print(chr(tape[5]), end='')
    tape[0] = 0
    tape[5] = 53
    tape[11] = 2
    tape[12] = 7
    tape[16] = 3
    tape[20] = 3
    tape[24] = 1
    tape[28] = 3
    tape[32] = 9
    tape[36] = 10
    tape[40] = 13
    tape[48] = 1
    tape[52] = 9
    tape[56] = 5
    tape[60] = 13
    tape[64] = 5
    tape[68] = 4
    tape[72] = 27
    tape[76] = 10
    tape[80] = 29
    tape[84] = 34
    tape[88] = 26
    tape[92] = 22
    tape[96] = 38
    tape[100] = 20
    tape[104] = 19
    tape[108] = 31
    tape[112] = 10
    tape[116] = 40
    tape[120] = 1
    tape[124] = 9
    tape[128] = 53
    tape[132] = 6
    tape[136] = 40
    tape[140] = 20
    tape[144] = 54
    tape[148] = 62
    tape[152] = 47
    tape[156] = 53
    tape[160] = 55
    tape[164] = 63
    tape[168] = 11
    tape[172] = 24
    tape[176] = 80
    tape[180] = 42
    tape[184] = 35
    tape[192] = 87
    tape[196] = 26
    tape[200] = 27
    tape[204] = 5
    tape[208] = 3
    print(chr(tape[5]), end='')
    tape[0] = 10
    tape[3] = 2
    tape[5] = 0
    tape[6] = 0
    tape[9] = 0
    tape[11] = 0
    print(chr(tape[0]), end='')
    
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        
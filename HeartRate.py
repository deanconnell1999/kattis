def bpm(beats, seconds):
    return (60*beats)/seconds


no = int(input())
for i in range(no):
    inp = input().split()
    beat = float(inp[0])
    sec = float(inp[1])
    print(bpm(beat-1, sec), bpm(beat, sec), bpm(beat+1, sec))
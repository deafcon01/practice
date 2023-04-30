def characterReplacement(s, k)->int:
    left=0
    seen = {}
    maxlen=0
    for right, curr in enumerate(s):
        if curr in seen :

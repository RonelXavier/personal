finalcount = 0
potioncount = 0

for x in "CCCCAABBAABABBCAAACBCCBAACBBBACCBAAAAACACABACCCCBCCAABACCCBCBCBCCCAACBBCCCBACCABABBABCBBABAABBAACBABACBCCBBCACBACAAACAAABABAABBABCCABABCBBBBCCABABCBAAABCBACACACCAABBBCBBBAAABABBABABCACBCBCABABCAACCBACAACAABAABBBBCAACCABACCBCBBCACACACBCAABCCABBACCBACBCACBABBACABCAABABAACBCCBCBCCABBBABCBACCABCCAACCCAACBBABCAAAABCAAABBCABCABBBAABCBCBABBCCBCACBCCBAABBACACAABBCBBACABBACCBCCBCBABCABBCBCAABBAACACCBABCAABCCABCACAABBAACAACBACBABCAACAABBBCACAABBAACCABAAABAABABCBABBBBCBAABBBAAAACACCACBAAABABBAAAAACACCCBBCCCCBCCABBBCCBCBBCCBACABABCCBBABBAAABBCCBAABBACAAAACCBBABABBCBABBBBBCABCBBCAABBBBCCCBCACABCBCACBCBBAACCABBCBCBACBCACCBBABCCCBAAACBBACCCCBAABCBACACBBBACCABCACACCBBCBCBBCBCACABCACCABCBCCCACABCCBBBBBCACBBAAAACBBCAAAAAACAABBABCBBBBABBBAABBCCCBACCBACCBACACAACBABBCABBABCABCABACAAABBBCBCBABBBCACBAABABACAAAAABCBBABBBABCAABACCAACBBABCAACAACBBACABCCCCAABCABCACACBBCCCACBBCABBACAAACBABCCCBCBBCAABBBBAACCAAABBCCABCBACBBBABACCACACAABABABCCCCAACBBCACBCABACBBCCBACCBCBAAAAABAAACABCACBBCAAAACBCCCCBCBCABABCAACACABAAB":
  if x == "C":
    finalcount += 3
  if x == "A":
    finalcount += 0
  if x == "B":
    finalcount += 1
print (finalcount)
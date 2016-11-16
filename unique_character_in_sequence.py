# input is length of gorups and sequnce of number
# find number which is unique and do not repeat in sequence

# 1st way
def fn(s):
  order = []
  counts = {}
  for x in s:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1 
      order.append(x)
  for x in order:
    if counts[x] == 1:
      return x
  return None
 
 # 2nd way
 s = "aabccbdcbe"
while s != "":
    slen0 = len(s)
    ch = s[0]
    s = s.replace(ch, "")
    slen1 = len(s)
    if slen1 == slen0-1:
        print ch
        break;
else:
    print "No answer"

n = int(raw_input())
x = [int(i) for i in raw_input().split()]
print fn(x)

s = input('Input : ')
primary_output = ''
n =0
for i in range(int(len(s)/2)) :
    l= s[n]
    n+=1
    j = s[n]
    n+=1
    int_j = int(j)
    for k in range(int_j):
        primary_output+=l


sorted_output = sorted(primary_output,key=str.lower)
final_output = ''
for i in sorted_output :
    final_output+=i

print("Output : ",final_output)
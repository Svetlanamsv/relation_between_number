print("Enter four digit number:", end="\n")
n=int(input())
n_th=n//1000
n_h=(n%1000)//100
n_d=((n%1000)%100)//10
n_n=((n%1000)%100)%10
print(n_th)
print(n_h)
print(n_d)
print(n_n)
addit=n_th+n_n
subtr=n_h-n_d
if addit==subtr:
    print("True")
else:
    print("False")
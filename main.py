#declararea unei liste care sa contina elementele 7,8,9,2,3,1,4,10,5,6 ( in aceasta ordine
my_list=[7,8,9,2,3,1,4,10,5,6]
print('Lista principala:',my_list)

#afisarea unei alte liste ordonate ascendent (lista initiala trebuie pastrata in aceeasi forma)
sort_my_list = sorted(my_list)
print('Lista sortata crescator', sort_my_list)

#afisarea unei liste ordonate descendent
def_my_list = sorted(my_list, reverse=True)
print('Lista afisata descrescator:', def_my_list)

#afisarea numerelor pare din lista(folosind doar slice)
my_slice_list_par = sort_my_list[1::2]
print('Lista numerelor pare din lista :', my_slice_list_par)

#afisarea numerelor impare din lista(folosind doar slice)
my_slice_list_impar = sort_my_list[::2]
print('Lista numerelor impare din lista:', my_slice_list_impar)

#afisarea elementelor multiplii ai lui 3
my_list2 =[]

for n in sort_my_list:
    if n % 3==0:
        my_list2.append(n)
    else:
        continue

print("Multipli de 3:", my_list2)
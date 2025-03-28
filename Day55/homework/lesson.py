# 1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია
#  for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 

arr = []

arr1 = []

dict1 = {
    "age" : 13,
    "name" : "data",
    "surname" : "shavadze"
}

for i,x in dict1.items():
    arr.append(i)
    arr1.append(x)

print(arr, arr1)

# 2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] 
# თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.

result = [10,43,12,11,94,10,55,7,11] 

print(set(result))

# 4) შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს
#  ძველი value  და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.

dict2 = {}

key = input("enter your key")
value = input("enter your value")

dict2[key] = value

new_value = input("enter your new value")

dict2[key] = new_value

print(dict2)
 
# 5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“


def remu_duplicet(list1):
    list2 = []

    for i in list1:
        if i not in list2:
            list2.append(i)

    print(list2)



print(remu_duplicet ([1, 2, 3, 4, 5, 5, 3, 2, 5, 6, 12, 65]))

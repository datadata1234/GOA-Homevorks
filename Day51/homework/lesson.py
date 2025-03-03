# 2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),
# რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

shopping_list = ("pasta", "strawberry", "oil", "detergent", "bred")

(p, s, o, d, b) = shopping_list

print(p)
print(s)
print(o)
print(d)
print(b)

# 3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.

x = ("Hot Dog", "Hamburger", "Coca-Cola", "Beans", "Greasy Khachapuri")

y = list(x)
y[::] = "Apple", "Low-fat khachapuri", "Water", "Sour cream", "Milk"
x = tuple(y)

print(x)

# 4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.

# როდესაც ფუნქციის პარამეტრებში იყენებთ  Asterisk-ს, ის აგროვებს ყველა პოზიციურ არგუმენტს, რომლებიც არ ემთხვევა სხვა პარამეტრებს, tuple-ში.



# 5) მოცემულია შემდეგნაირი tuple:

# months = ("January", "February", "March", "April", "May")
# (first, second, third, fourth*) = months

#რას გამოიტანს მოცემული კოდი?

# print(first)
# print(second)
# print(third)
# print(fourth)



# ამას
"January"
"February"
"March"
["April", "May"]



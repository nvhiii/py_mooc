temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no)")
# ppl need basic garments
print(f"Wear jeans and a T-shirt")

if temp < 21:
    print(f"I recommend a jumper as well")

if temp < 11:
    print(f"Take a jacket with you")

if temp < 6:
    print(f"Make it a warm coat, actually")
    print(f"I think gloves are in order")

if rain == "yes":
    print(f"Don't forget your umbrella!")
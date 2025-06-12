import random
def get_numbers_ticket(min, max, quantity):
    if max-min < quantity:
        return "Range is less then qty. Correct your data and try again"
    population=[]
    for i in range (min, max+1):#Визначаємо набір чисел виходячи з діапазону
        population.append(i)
        i+=1
    return random.choices(population, weights=None, cum_weights=None, k=quantity) #обираємо рандомний набір в заданій кількості з наповненого діапазону
print(get_numbers_ticket(1,1000,5)) #візульне тестування результатів

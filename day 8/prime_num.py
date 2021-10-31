def prime_check(num):
    is_prime = True
    for i in range(2, num):
        if num %i == 0:
            is_prime = False
    if is_prime:
        print (f"The number {num} is a prime number ")
    else:
        print (f"The number {num} is not a prime number ")

print()
n = int(input("Enter the number to check prime or not : "))
prime_check(n)
print()

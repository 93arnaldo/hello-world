#FIZZBUZZ

print '''Hi This is the game FizzBuzz
 In case a number is divisible with 3, the diplay will show "fizz" instead of the number.
 If a number is divisible with 5, it prints "buzz".
 If it's divisible with both 3 and 5, it prints "fizzbuzz".'''

x = 0

while True:

    Number = int(raw_input('Please, enter a number between 1 and 100:'))

    if 1 <= Number <= 100:

        for x in range(Number):
            x += 1
            if x % 3 != 0:
                print x
            elif x % 3 == 0 and x % 5 == 0:
                print "FizzBuzz"
            else:
                print "Fizz"
        break #con este break tengo la intencion de parar el loop For pero en realidad paro todo el programa (el While true). mi intencion es que vuelvas al raw imput. Como se puede hacer?

    else:
        print "Please, enter a number between 1 and 100"
        break

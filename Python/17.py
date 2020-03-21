digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
digit3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_to_english(number):
    if  0 <= number < 10:
        return digit[number]
    if 10 <= number < 20:
        return digit2[number % 10]
    if number % 10 == 0 and number < 100:
        return digit3[number // 10 -2]
    if 20 < number < 100:
        return digit3[number // 10 -2] + " " + digit[number % 10]
    if number < 1000:
        r = digit[number // 100] + " hundred"
        if number % 100:
            r += " and " + number_to_english(number % 100)
        return r
    if number == 1000:
        return "one thousand"

    
print(sum(len(number_to_english(i).replace(" ", "")) for i in range(1, 1001)))

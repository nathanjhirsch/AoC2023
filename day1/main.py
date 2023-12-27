inputfile = "input.txt"

# # Part 1, comment out to run part 2
# numbers = []
# with open(inputfile) as f:
#     lines = f.readlines()
#     for line in lines:
#         num = []
#         for letter in line:
#             if letter.isdigit():
#                 num.append(letter)
#         line_num=num[0] + num[len(num)-1]
#         numbers.append(line_num)       
# print(numbers)

# sum=0
# for num in numbers:
#     sum += int(num)
# print(sum)

# Part 2
mappings_dict = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

numbers = []
with open(inputfile) as f:
    lines = f.readlines()
    for line in lines:
        repl_list = []
        for key in mappings_dict.keys():
            temp = line.replace(key, str(mappings_dict[key]))
            if len(temp) != len(line):
                repl_list.append(temp)
        repl_list.append(line)
        #I have all the possible transformations from str to int.
        #Plus I have the original string. So I can just find the first and last letters of them all and be done?
        first_digit_position = len(line)
        first_digit = ""
        last_digit_position = len(line)
        last_digit = ""

        for stringinstance in repl_list:
            for i, letter in enumerate(stringinstance):
                if letter.isdigit():
                    backposition = len(stringinstance) - i - 1
                    #Who has the earliest number?
                    if i < first_digit_position:
                        first_digit_position = i
                        first_digit = letter
                    #Who has the latest number?
                    if backposition < last_digit_position:
                        last_digit_position = backposition
                        last_digit = letter
            
        numbers.append("".join([first_digit, last_digit]))       

sum=0
for i, num in enumerate(numbers):
    sum += int(num)
print(sum)

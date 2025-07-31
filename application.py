# Section 1
# print("Hello World")
# print("This is the next statement")
#
# number = 77
# print(number)
#
# first_name = "Aidan"
#
# last_name = "Lachlan"
#
# name = first_name + " " + last_name
# print(name)
#
# weight = 160
# sentence = name + " weighs " + str(weight) + " lbs"
# print(sentence)

# Section 2
# adult = True
# data_type = type(adult)
# age = 28
# print(data_type)
# print(age)
# print(adult)
#
# adult = 12.08
# data_type = type(adult)
# print(data_type)
#
# adult = "String"
# data_type = type(adult)
# print(data_type)

# Section 3
# num1 = 3
#
# num2 = 10
#
# answer = num2 % num1
# print(answer)
# answer = 10 + 3 * 9 - 4
#
# print(answer)

# Section 4 // String indexing and slicing
# sentence = 'This is a sentence'
# # next_sentence = 'I'm coming home'
# print(sentence)
# # print(next_sentence)
# next_sentence = "I'm coming home"
# print(next_sentence)
#
# sentence = "I'm coming \nhome"
# print(sentence)
#
# sentence = 'This is a sentence'
# print(sentence[0])
# print(sentence[-1])
# print(sentence[0:4])
# print(sentence[0:7])
#
# sentence = "abcdefg"
# print(sentence[0:7:2])
# print(sentence[3:])
# print(sentence[-3:])

# Section 5 // Basic string methods
# sentence = "this is a sentence"
# sentence_to_upper = sentence.upper() # method
#
# print() # function
# print(sentence_to_upper)
#
# sentence = "this IS a SENTENCE"
# print(sentence.lower())
# print(sentence.capitalize())
#
# is_digit = sentence.isdigit()
# print("is_digit?", is_digit)
#
# sentence = "9484"
# print(sentence)
# print(sentence.isdigit())
# sentence = "93893843 3984934392830"
# print(sentence, "is_digit?", is_digit)
# sentence = "A83739586325"
# is_alnum = sentence.isalnum()
# print(sentence,"is_alnum?", is_alnum)
#
# sentence = "A09832094%4$al342"
#
# print(sentence.startswith("A098"))

# print(sentence.startswith("%4$", 9))

# Section 6 // Formatting string with Format method

# correct_answer = 15
# sentence = f"The sum of 5 + 10 is {correct_answer}"
# print(sentence)
# answer = 50
# sentence = "The sum of 5 + 10 is {0}".format(answer)
# print(sentence, answer == correct_answer)
#
# sentence = "The sum of 5 + 10 is {0}".format("nice day")
# print(sentence)
#
# sentence = "The sum of {0} + {0} is {0}".format(10)
# print(sentence, False)
# sentence = "The sum of {0} + {1} is {2}".format(10, 15, 25)
# print(sentence)

# Section 7 // String are Immutable

# my_var = "abcdefg"
# print(my_var[0])
#
# # my_var[0] = '1' # error: 'str' object does not support item assignment
# # print(my_var[0])
#
# # print("1" + my_var[1:])
# my_var = "1" + my_var[1:]
# print(my_var)

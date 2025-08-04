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

# Part 2: Section 8(1) // Lists
# mutable
# my_list = [1, 2, 3, 4, 5]
# # my_list.pop() # removes last item (same as JS) // can specify index
#
# my_list[0] = 'S'
#
# print(type(my_list))
# print(my_list)
#
# my_list[0] = ['hello', 'good bye']
# my_list.append("this is a sentence")
#
# sentence = my_list.pop()
#
# print(my_list)
#
# print(sentence)
#
# None
#
# my_list = [4, 5, 3, 1, 2]
#
# my_list.sort()
#
# print(my_list)
#
# my_list = [4, 5, 3, 1, 2]
# my_list.reverse()
# print(my_list)
#
# my_list = ['4', '5', '3', '1', '2']
# my_list.sort()
# my_list.reverse()
# print(my_list)
#
# my_list = ['b', 'd', 'a', 'z', 'x']
# my_list.sort()
# print(my_list)
#
# print(my_list[2:])
# print(my_list[2:4])
# print(my_list[-1])
#
# item_count = len(my_list)
# print(item_count)
#
# my_list = ['b', 'd', 'a', 'z', 'x']
#
# another_list = [4, 5, 3, 1, 2]
#
# # new_list = my_list + another_list
# # print(new_list)
#
# my_list.append(another_list)
# print(my_list)
# # concatenate the last three items of the sorted and reversed lists
# my_list = ['b', 'd', 'a', 'z', 'x']
# another_list = [1, 2, 3, 4, 5]
#
# my_list.sort()
# my_list.reverse()
# print(my_list)
# another_list.reverse()
# print(another_list)
#
# result = my_list[2:] + another_list[2:]
# print('result:', result)

# Section 9(2) // Accessing Elements in Nested Lists

# my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', 'banana'], 'd']
# # print 'banana'
# print(my_list[-2][2])
#
# my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
# # print 'robert'
# print(my_list[-2][2][1])
#
# my_list[2] = 'computer'
# print(my_list)
# # change 'robert' to 'joe'
#
# my_list[-2][2][1] = 'joe'
# print(my_list)

# Section 10(3) // Finding index positions in lists and counting duplicates

# my_list = ['a','b', 'c', 'd']
#
# idx_pos = my_list.index('c')
# print(idx_pos)
#
# my_list = ['a','b', 'c', 'd', 'c', 'c']
# c_count = my_list.count('c')
# print(c_count)

# Section 11(4) // Tuples

# my_list = [1, 2, 3]
#
# my_list[1] = 'NEW VALUE'
#
# print(my_list)
#
# my_tuple = (1, 2, 3, "some data", [1, 2, 3])
# print(my_tuple)
#
# print(my_tuple[4])

# my_tuple[3] = 4 # tuple object does not support item assignment
# my_tuple[4][2] = "new value"  # changing a value in the list inside the tuple works
# print(my_tuple)
#
# my_tuple = (1, 2, 3, "some data", 'some data', 'some data', [1, 2, 3])
#
# count = my_tuple.count("some data")
# print(count)
#
# print(my_tuple[3:6]) # slicing a tuple returns a tuple
#
# str_tuple = my_tuple[3:6]
# print(type(str_tuple))
#
# extracted = my_tuple[6]
# print(extracted)
# print(type(extracted))

# Section 12(5) // dictionaries

# dict = {'k1': 'some data', '7': 'other data'}
#
# value = dict['k1']
# print(value)
#
# value = dict['7']
# print(value)
#
# dict['7'] = 'NEW VALUE'
# print(dict)
#
# dict['k1'] = 'new value'
# print(dict)
#
# people_weight_dict = {'john': 134, 'mike': 170, 'robert': 165}
#
# print(people_weight_dict)
#
# people_weight_dict['john'] = 150
# print(people_weight_dict['john'])
#
# print(people_weight_dict)
#
# weight_of_mike = people_weight_dict.pop('mike')  # storing .pop() will return the value from key-value pair
# print(weight_of_mike)
# print(people_weight_dict)
#
# people_weight_dict = {'john': 134, 'mike': 170, 'robert': 165}
#
# people_weight_dict.clear()  # empties the dictionary
# print(people_weight_dict)
#
# people_weight_dict = {'john': 134, 'mike': 170, 'robert': 165, 'items': ['orange', 'banana']}
#
# people_weight_dict['99'] = 'some data'  # adding key value pairs
# print(people_weight_dict)
# print(people_weight_dict['99'])
# print(people_weight_dict['items'])
# print(people_weight_dict['items'][1])
#
# people_weight_dict = {'john': 134, 'mike': 170,
#                       'robert': 165, 'items': ['orange', {'k1': 'some value'}],
#                       'tuple': (1, 2, 3, 4, 5)
#                       }
#
# print(people_weight_dict['items'][1]['k1'])
#
# my_tuple = people_weight_dict['tuple']
# print(my_tuple)
# print(my_tuple[2])
#
# tuple_removed = people_weight_dict.pop('tuple')
# print(people_weight_dict)
# print(tuple_removed)


# Section 13(6) // Comparison Operators

print(10 == 10)  # True
print(10 == 9)  # False
print(5 == '5')  # False
print(5 == 5.00)  # True
print(5 < 10)  # True
print(5 > 10)  # False
print(5 >= 5)  # True
print(5 != 6)  # True
print(5 != 5)  # False

print(('hello' == 'Hello') or (5 == 5))  # True
print((('hello' == 'Hello') or (5 == 6)) and True)  # False (False and True => False)

print(not 5) # False
print(not False) # True
print(not True) # False

condition = not (5==5) # False

print(type(condition)) # boolean

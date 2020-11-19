"""
I was bored one day and decided to look at last names in the phonebook for my
area.
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
Example:
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Linear Search (Brute Force): O(n)
    # set 2 indicies n1 and n2 0 and 1 respectively
    # iterate over the surnames list using a range based loop
        # 
        # check if surnames at index of n1 is greater than surnames at index n2
            # return n2

        # increment n1
        # increment n2

    # Binary Search: O(log n)
    # grab the first surname
    first_surname = surnames[0]
    # set a min to 0
    min = 0
    # set a max to the length of surnames - 1
    max = len(surnames) - 1

    # while my min is less than my max
    while min < max:
        # guess the halfway point with normalization
        guess = min + ((max - min) // 2)

        # if our guess comes after our surname or is our surname
        if surnames[guess] >= first_surname:
            # go right
            min = guess

        # otherwise
        else:
            # go left
            max = guess

        # if our min and max overlap / converge
        if min + 1 == max:
            # our max is alphabetically first
            # so return our max
            return max

# Revised

    # for i in range(len(surnames)):
    #     if surnames[i]>surnames[i+1]:
    #         return i +1

# Brute Force attempt

#     counter = 0
#     last_name = ''
#     for name in surnames:
#         if last_name == '':
#             last_name = name[0]
#         if ord(name[0]) < ord(last_name):
#             return counter
#         counter += 1
#     return('fail')

# print(find_rotation_point(surnames))
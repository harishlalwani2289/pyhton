import random
import sys

import numpy as np

# This cide is from https://dev.to/jamesshah/housie-tambola-ticket-generator-using-python-31m1

def get_tickets():
    global i
    ticket_array = np.zeros((3, 9), dtype=int)
    # This is the total indices available for us
    # We have to select random indices for all the three rows from all the indices available
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    random_indices = []

    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[18:], 5)
    for i in first_row:
        random_indices.append(i)
    for i in second_row:
        random_indices.append(i)
    for i in third_row:
        random_indices.append(i)

    # Generating numbers for each column
    total_numbers = [i for i in range(1, 91)]
    for num in random_indices:
        if num[1] == 0:
            number = random.choice(total_numbers[:10])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 1:
            number = random.choice(total_numbers[10:20])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 2:
            number = random.choice(total_numbers[20:30])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 3:
            number = random.choice(total_numbers[30:40])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 4:
            number = random.choice(total_numbers[40:50])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 5:
            number = random.choice(total_numbers[50:60])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 6:
            number = random.choice(total_numbers[60:70])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 7:
            number = random.choice(total_numbers[70:80])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 8:
            number = random.choice(total_numbers[80:89])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0

    # Sorting each column
    for col in range(9):

        # if all the rows are filled with a random number

        if ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0:
            for row in range(2):
                if ticket_array[row][col] > ticket_array[row + 1][col]:
                    temp = ticket_array[row][col]
                    ticket_array[row][col] = ticket_array[row + 1][col]
                    ticket_array[row + 1][col] = temp


        # if 1st and 2nd row are filled by random number

        elif ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0:
            if ticket_array[0][col] > ticket_array[1][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[1][col]
                ticket_array[1][col] = temp


        # if 1st and 3rd row are filled by random number

        elif ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0:
            if ticket_array[0][col] > ticket_array[2][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

        # if 2nd and 3rd rows are filled with random numbers

        elif ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0:
            if ticket_array[1][col] > ticket_array[2][col]:
                temp = ticket_array[1][col]
                ticket_array[1][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

    return ticket_array


if __name__ == "__main__":

    # Take number of tickets from user as system argument
    numberOfTickets = sys.argv[1]
    tickets = []

    for i in range(int(numberOfTickets)):
        ticket = get_tickets()
        tickets.append(ticket)

    for ticket in tickets:
        print(ticket)

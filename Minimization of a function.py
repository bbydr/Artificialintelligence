
""""
EARIN - Introduction to Artificial Intelligence - Exercise#1
Merve Rana Kızıl
Beste Baydur
"""

import numpy as np
import random
import time


class Optimizer:

    def __init__(self, A, b, c, size, max_iter, desired_Jx, max_comp_time):
        self.A = A
        self.b = b
        self.c = c
        self.x = [0] * size
        self.size = size
        self.max_iter = max_iter
        self.desired_Jx = desired_Jx
        self.max_comp_time = max_comp_time

    # Function J(x)
    def f(self):
        return self.c + np.dot(self.b, self.x) + self.x @ self.A @ self.x

    # First derivative of the function
    def fprime(self):
        return self.b + 2 * self.A @ self.x

    # Second derivative of the function
    def fsecond(self):
        return 2 * self.A

    # Defines the starting point
    def starting_point(self):
        while True:
            print("Define the starting point.")
            print("Enter 1 to set x0 directly.")
            print("Enter 2 to define the lower and upper limits.")
            option = int(input())
            if option == 1 or option == 2:
                break

        if option == 1:
            # iterating till the range
            print("Enter the elements of vector x0: ")
            for i in range(0, size):
                element = float(input())
                np.append(self.x, element)

        elif option == 2:
            print("Enter the lower limit: ")
            l = int(input())
            print("Enter the upper limit: ")
            u = int(input())
            self.x = np.array([l, u])
            # Generate random integers from lower limit to upper limit
            for i in range(0, size):
                np.append(self.x, random.randint(l, u))

    # Newton's method
    def newtons_method(self):
        iters = 0
        comp_time = 0
        h = self.f() / self.fprime()
        while iters < self.max_iter and comp_time <= self.max_comp_time and self.f() != desired_Jx:
            start = time.time()
            h = np.linalg.inv(self.fsecond()) @ self.fprime()
            # x(i+1) = x(i) - f'(x) / f''(x)
            self.x = self.x - h
            iters = iters + 1
            end = time.time()
            comp_time = comp_time + end - start

            print("Iteration", iters, "\nX value is", self.x)  # Print iterations
            print("The local minimum occurs at", self.x)

        print("Newton's method: ")
        print("Found solution: ", self.x)
        print("Function value: ", self.f())
        print("--------------------------------------------------------")
        return self.x, self.f()

    # Simple gradient descent method
    def gradient_descent(self):
        iters = 0
        rate = 0.001  # learning rate (a small constant)
        comp_time = 0

        while iters < self.max_iter and comp_time <= self.max_comp_time and self.f() != desired_Jx:
            # starting time
            start = time.time()
            self.x = self.x - rate * self.fprime()  # Grad descent
            iters = iters + 1  # iteration count
            print("Iteration", iters, "\nX value is", self.x)  # Print iterations
            print("The local minimum occurs at", self.x)

        print("Simple gradient descent method")
        print("Found solution: ", self.x)
        print("Function value: ", self.f())
        print("--------------------------------------------------------")
        return self.x, self.f()


if __name__ == "__main__":
    answer = input("Do you want to run the program in batch mode (yes/no)? ")
    while answer != 'yes' and answer != 'no':
        answer = input("Do you want to run the program in batch mode (yes/no)? ")

    while answer == 'yes':
        n = int(input("Enter the number of times you want to start the program: "))
        if n >= 2:
            break
        else:
            print("You chose the batch mode. n must be greater than 1.")
    else:
        n = 1

    while True:
        print("Choose a method.")
        print("Enter 1 for simple gradient descent method.")
        print("Enter 2 for Newton's method.")
        option = int(input())
        if option == 1 or option == 2:
            break
        else:
            print("Enter a valid input.")

    try:
        size = int(input('Enter the size of the matrices (e.g. enter 2 for a 2x2 matrix): '))
    except ValueError:
        print("Invalid input.")

    sum_func = 0
    sum_x = [0] * size
    func_arr = []
    x_std_dev = []

    # Take the elements of positive-definite matrix A
    A = []
    while True:
        temp_list = []
        print("Enter the elements of matrix A: ")
        print("Press enter for each element, row-wise")
        for i in range(size):
            for j in range(0, size):
                temp_list.append(float(input()))
            A.append(temp_list)
            temp_list = []
        # Check whether the input is valid
        if np.all(np.linalg.eigvals(A) > 0):
            break
        else:
            A = []
            print("Invalid input. Please enter a positive-definite matrix.")
    A = np.array(A)

    # Take the elements of vector b
    print("Enter the elements of vector b: ")
    b = []
    for i in range(0, size):
        b.append(float(input()))  # adding the element
    b = np.array(b)

    # Take the scalar number c
    c = float(input("Enter c: "))

    for i in range(0, n):
        print("Define the stopping condition.")
        try:
            max_iter = int(input("Maximum numbers of iterations: "))
            desired_Jx = float(input("Desired J(x) value to reach: "))
            max_comp_time = int(input("Maximum computation time: "))
        except ValueError:
            print("Invalid input.")

        optimizer = Optimizer(A, b, c, size, max_iter, desired_Jx, max_comp_time)
        optimizer.starting_point()

        x = []
        func = 0

        if option == 1:
            x, func = optimizer.gradient_descent()
        elif option == 2:
            x, func = optimizer.newtons_method()

        sum_func = sum_func + func
        sum_x = np.add(sum_x, x)
        func_arr.append(func)
        x_std_dev.append(x)

    # Print the found solutions’ means and standard deviations if the batch mode is chosen
    if answer == 'yes':
        print("Mean of the found solutions: ", sum_x / size)
        print("Mean of the function values: ", sum_func / size)
        print("Standard deviation of the found solutions: ", np.std(x_std_dev, axis=0))
        print("Standard deviation of the function values: ", np.std(func_arr))

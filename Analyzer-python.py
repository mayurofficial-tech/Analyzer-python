import numpy as np


class DataAnalytics:
    def __init__(self, array=None):
        self.array = np.array(array) if array is not None else None

    # ---------- Array Management ----------
    def create_array(self, dimensions, elements, rows=1, cols=1):
        elements = list(map(int, elements))
        if dimensions == 1:
            self.array = np.array(elements)
        elif dimensions == 2:
            self.array = np.array(elements).reshape(rows, cols)
        elif dimensions == 3:
            depth = len(elements) // (rows * cols)
            self.array = np.array(elements).reshape(depth, rows, cols)
        return self.array

    def indexing(self, row, col):
        return self.array[row, col]

    def slicing(self, row_start, row_end, col_start, col_end):
        return self.array[row_start:row_end, col_start:col_end]

    def combine_arrays(self, other_array):
        return np.vstack((self.array, other_array))

    def split_array(self, sections):
        return np.array_split(self.array, sections)

    # ---------- Mathematical Operations ----------
    def add_arrays(self, other_array):
        return self.array + other_array

    def subtract_arrays(self, other_array):
        return self.array - other_array

    def multiply_arrays(self, other_array):
        return self.array * other_array

    def divide_arrays(self, other_array):
        return self.array / other_array

    def dot_product(self, other_array):
        return np.dot(self.array, other_array)

    # ---------- Search, Sort, and Filter ----------
    def search_value(self, value):
        return np.where(self.array == value)

    def sort_array(self):
        return np.sort(self.array)

    def filter_array(self, condition_func):
        return self.array[condition_func(self.array)]

    # ---------- Aggregates ----------
    def sum(self):
        return np.sum(self.array)

    def mean(self):
        return np.mean(self.array)

    def median(self):
        return np.median(self.array)

    def std_dev(self):
        return np.std(self.array)

    def variance(self):
        return np.var(self.array)

    # ---------- Statistics ----------
    def min_value(self):
        return np.min(self.array)

    def max_value(self):
        return np.max(self.array)

    def percentile(self, q):
        return np.percentile(self.array, q)

    def correlation(self, other_array):
        return np.corrcoef(self.array.flatten(), other_array.flatten())[0, 1]


# ---------- Menu-driven UI ----------
def main():
    obj = DataAnalytics()

    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nSelect Array Type:\n1. 1D\n2. 2D\n3. 3D")
            t = int(input("Enter type: "))
            if t == 1:
                elements = input("Enter elements: ").split()
                arr = obj.create_array(1, elements)
            elif t == 2:
                r = int(input("Rows: "))
                c = int(input("Cols: "))
                elements = input(f"Enter {r * c} elements: ").split()
                arr = obj.create_array(2, elements, r, c)
            print("Array created:\n", obj.array)

        elif choice == 2:
            print("\nMathematical Ops:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
            op = int(input("Choose operation: "))
            elements = input("Enter elements of same size: ").split()
            other = np.array(list(map(int, elements))).reshape(obj.array.shape)

            if op == 1:
                print("Result:\n", obj.add_arrays(other))
            elif op == 2:
                print("Result:\n", obj.subtract_arrays(other))
            elif op == 3:
                print("Result:\n", obj.multiply_arrays(other))
            elif op == 4:
                print("Result:\n", obj.divide_arrays(other))

        elif choice == 3:
            print("\n1. Combine Arrays\n2. Split Array")
            op = int(input("Choose: "))
            if op == 1:
                elements = input("Enter elements of another array: ").split()
                other = np.array(list(map(int, elements))).reshape(obj.array.shape)
                print("Combined Array:\n", obj.combine_arrays(other))
            elif op == 2:
                sec = int(input("Enter number of splits: "))
                print("Splits:", obj.split_array(sec))

        elif choice == 4:
            print("\n1. Search\n2. Sort\n3. Filter")
            op = int(input("Choose: "))
            if op == 1:
                val = int(input("Enter value: "))
                print("Found at:", obj.search_value(val))
            elif op == 2:
                print("Sorted Array:\n", obj.sort_array())
            elif op == 3:
                cond = int(input("Enter threshold: "))
                print("Filtered Array:", obj.filter_array(lambda x: x > cond))

        elif choice == 5:
            print(
                "\n1. Sum\n2. Mean\n3. Median\n4. Std Dev\n5. Variance\n6. Min\n7. Max\n8. Percentile\n9. Correlation")
            op = int(input("Choose: "))
            if op == 1:
                print("Sum:", obj.sum())
            elif op == 2:
                print("Mean:", obj.mean())
            elif op == 3:
                print("Median:", obj.median())
            elif op == 4:
                print("Std Dev:", obj.std_dev())
            elif op == 5:
                print("Variance:", obj.variance())
            elif op == 6:
                print("Min:", obj.min_value())
            elif op == 7:
                print("Max:", obj.max_value())
            elif op == 8:
                q = int(input("Enter percentile: "))
                print("Percentile:", obj.percentile(q))
            elif op == 9:
                elements = input("Enter elements of another array: ").split()
                other = np.array(list(map(int, elements))).reshape(obj.array.shape)
                print("Correlation:", obj.correlation(other))

        elif choice == 6:
            print("Thank you for using NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()

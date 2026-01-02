# Numpy Analyzer with Advanced Features
# Features: Encapsulation, Classmethod, Staticmethod, Menu-driven UI    
#Library: numpy

import numpy as np

class DataAnalytics:
    def __init__(self, array=None):
        self.array = array

    # ---------- Encapsulation example (private helper) ----------
    def __validate_array_for_math(self, other):
        if self.array is None:
            raise ValueError("No base array available. Create an array first.")
        if self.array.shape != other.shape:
            raise ValueError("Arrays must have the same shape for this operation.")

    # ---------- Classmethod and Staticmethod ----------
    @classmethod
    def from_input(cls, dim):
        """Create array by taking user input based on dimension choice."""
        if dim == 1:
            n = int(input("Enter the number of elements: "))
            elems = list(map(float, input(f"Enter {n} elements separated by space: ").split()))
            if len(elems) != n:
                print("Incorrect number of elements. Array not created.")
                return cls()
            arr = np.array(elems)
        elif dim == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = rows * cols
            elems = list(map(float, input(f"Enter {total} elements for the array separated by space: ").split()))
            if len(elems) != total:
                print("Incorrect number of elements. Array not created.")
                return cls()
            arr = np.array(elems).reshape(rows, cols)
        elif dim == 3:
            d1 = int(input("Enter dimension 1 size: "))
            d2 = int(input("Enter dimension 2 size: "))
            d3 = int(input("Enter dimension 3 size: "))
            total = d1 * d2 * d3
            elems = list(map(float, input(f"Enter {total} elements for the array separated by space: ").split()))
            if len(elems) != total:
                print("Incorrect number of elements. Array not created.")
                return cls()
            arr = np.array(elems).reshape(d1, d2, d3)
        else:
            print("Invalid dimension choice.")
            return cls()

        print("\nArray created successfully:")
        print(arr)
        return cls(arr)

    @staticmethod
    def display_array(arr, title="Array"):
        print(f"\n{title}:")
        print(arr)

    # ---------- Array Management ----------
    def indexing(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return
        print(f"\nCurrent Array:\n{self.array}")
        try:
            indices = input("Enter index/indices (e.g., 0 or 1,2 for 2D or 1,2,3 for 3D): ")
            if "," in indices:
                idx = tuple(map(int, indices.split(",")))
                print("Indexed Element:", self.array[idx])
            else:
                idx = int(indices)
                print("Indexed Element:", self.array[idx])
        except Exception as e:
            print("Invalid index:", e)

    def slicing(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        print(f"\nCurrent Array:\n{self.array}")
        print("Enter slice ranges separated by ':' for each dimension.")
        print("Example: for 3D use '0:2,0:1,1:3' (dim1,dim2,dim3)")
        print("For 2D: '0:2,1:3'")
        print("For 1D: '0:5'")
        try:
            slice_input = input("Enter slice: ").strip()

            if slice_input.count(',') == 2:  # 3D
                slices = slice_input.split(',')
                d1 = slices[0].split(':')
                d2 = slices[1].split(':')
                d3 = slices[2].split(':')

                s1 = int(d1[0]) if d1[0] != '' else None
                e1 = int(d1[1]) if len(d1) > 1 and d1[1] != '' else None

                s2 = int(d2[0]) if d2[0] != '' else None
                e2 = int(d2[1]) if len(d2) > 1 and d2[1] != '' else None

                s3 = int(d3[0]) if d3[0] != '' else None
                e3 = int(d3[1]) if len(d3) > 1 and d3[1] != '' else None

                sliced = self.array[s1:e1, s2:e2, s3:e3]
                print("\nSliced Array:")
                print(sliced)

            elif slice_input.count(',') == 1:  # 2D
                slices = slice_input.split(',')
                row_range = slices[0].split(':')
                col_range = slices[1].split(':')

                r_start = int(row_range[0]) if row_range[0] != '' else None
                r_end = int(row_range[1]) if len(row_range) > 1 and row_range[1] != '' else None

                c_start = int(col_range[0]) if col_range[0] != '' else None
                c_end = int(col_range[1]) if len(col_range) > 1 and col_range[1] != '' else None

                sliced = self.array[r_start:r_end, c_start:c_end]
                print("\nSliced Array:")
                print(sliced)

            else:  # 1D
                start, end = slice_input.split(":")
                start = int(start) if start != "" else None
                end = int(end) if end != "" else None
                sliced = self.array[start:end]
                print("\nSliced Array:")
                print(sliced)

        except Exception as e:
            print("Invalid slice format. Use format like '0:2,0:1,1:3' for 3D:", e)

    def combine_arrays(self):
        if self.array is None:
            print("No base array. Create an array first.")
            return
        print("\nOriginal Array:")
        print(self.array)

        total = self.array.size
        print(f"Total elements needed: {total}")
        elems_input = input(f"Enter the elements of another array to combine ({total} elements separated by space): ").split()
        elems = list(map(float, elems_input))
        if len(elems) != total:
            print(f"Incorrect number of elements. Got {len(elems)}, expected {total}.")
            return
        other = np.array(elems).reshape(self.array.shape)
        print("\nSecond Array:")
        print(other)

        # Vertical stack similar to example
        combined = np.vstack((self.array, other))
        print("\nCombined Array (Vertical Stack):")
        print(combined)

    def split_array(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        print("\nOriginal Array:")
        print(self.array)
        try:
            num_splits = int(input("Enter number of splits: "))
            splitted = np.array_split(self.array, num_splits)
            for i, part in enumerate(splitted, start=1):
                print(f"\nPart {i}:")
                print(part)
        except Exception as e:
            print("Error while splitting:", e)

    # ---------- Mathematical Operations ----------
    def elementwise_operation(self, op):
        if self.array is None:
            print("No base array. Create an array first.")
            return

        total = self.array.size
        print(f"Total elements needed: {total}")
        elems_input = input(f"Enter the same-size array elements ({total} elements separated by space): ").split()
        elems = list(map(float, elems_input))
        if len(elems) != total:
            print(f"Incorrect number of elements. Got {len(elems)}, expected {total}.")
            return

        other = np.array(elems).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)
        print("\nSecond Array:")
        print(other)
        try:
            self.__validate_array_for_math(other)
            if op == "add":
                result = self.array + other
                title = "Result of Addition"
            elif op == "sub":
                result = self.array - other
                title = "Result of Subtraction"
            elif op == "mul":
                result = self.array * other
                title = "Result of Multiplication"
            elif op == "div":
                result = self.array / other
                title = "Result of Division"
            else:
                print("Invalid operation.")
                return

            print(f"\n{title}:")
            print(result)
        except Exception as e:
            print("Error:", e)

    def dot_and_matrix_multiplication(self):
        if self.array is None:
            print("No base array. Create an array first.")
            return
        if self.array.ndim != 2:
            print("Dot and matrix multiplication supported only for 2D arrays.")
            return

        print("\nBase 2D Array:")
        print(self.array)
        print("\nEnter another 2D array for dot/matrix multiplication.")
        try:
            rows2 = int(input("Enter the number of rows of second array: "))
            cols2 = int(input("Enter the number of columns of second array: "))
            total2 = rows2 * cols2
            print(f"Total elements needed: {total2}")
            elems_input = input(f"Enter {total2} elements separated by space: ").split()
            elems = list(map(float, elems_input))
            if len(elems) != total2:
                print(f"Incorrect number of elements. Got {len(elems)}, expected {total2}.")
                return
            other = np.array(elems).reshape(rows2, cols2)

            print("\nSecond Array:")
            print(other)

            if self.array.shape[1] != rows2:
                print(f"Incompatible shapes for matrix multiplication. Base: {self.array.shape}, Second: {other.shape}")
                return

            dot_result = np.dot(self.array, other)
            matmul_result = self.array @ other

            print("\nDot Product Result:")
            print(dot_result)
            print("\nMatrix Multiplication Result:")
            print(matmul_result)
        except Exception as e:
            print("Error:", e)

    # ---------- Search, Sort, Filter ----------
    def search_value(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        val = float(input("Enter value to search: "))
        positions = np.argwhere(self.array == val)
        if positions.size == 0:
            print(f"Value {val} not found in array.")
        else:
            print(f"Value {val} found at indices:")
            print(positions)

    def sort_array(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        order = input("Enter order (asc/desc): ").strip().lower()
        print("\nOriginal Array:")
        print(self.array)

        if self.array.ndim == 1:
            sorted_arr = np.sort(self.array)
            if order == "desc":
                sorted_arr = sorted_arr[::-1]
        else:
            # sort along first axis (row-wise for 2D, etc.)
            sorted_arr = np.sort(self.array, axis=1)
            if order == "desc":
                sorted_arr = np.flip(sorted_arr, axis=1)

        print("\nSorted Array:")
        print(sorted_arr)
        if self.array.ndim == 2:
            print("(Sorting applied row-wise.)")

    def filter_values(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        print("Filter condition options: >, >=, <, <=, ==, !=")
        cond = input("Enter condition (e.g., > 10): ").strip().split()
        if len(cond) != 2:
            print("Invalid condition format.")
            return

        op, num = cond[0], float(cond[1])

        if op == ">":
            result = self.array[self.array > num]
        elif op == ">=":
            result = self.array[self.array >= num]
        elif op == "<":
            result = self.array[self.array < num]
        elif op == "<=":
            result = self.array[self.array <= num]
        elif op == "==":
            result = self.array[self.array == num]
        elif op == "!=":
            result = self.array[self.array != num]
        else:
            print("Invalid operator.")
            return

        print("\nFiltered values:")
        print(result)

    # ---------- Aggregating & Statistical Functions ----------
    def agg_and_stat(self):
        if self.array is None:
            print("No array available. Create an array first.")
            return

        while True:
            print("\nAggregates and Statistics:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentiles")
            print("9. Correlation Coefficient (with another array)")
            print("10. Go Back")

            choice = input("Enter your choice: ").strip()

            print("\nOriginal Array:")
            print(self.array)

            if choice == "1":
                print("Sum of Array:", np.sum(self.array))
            elif choice == "2":
                print("Mean of Array:", np.mean(self.array))
            elif choice == "3":
                print("Median of Array:", np.median(self.array))
            elif choice == "4":
                print("Standard Deviation of Array:", np.std(self.array))
            elif choice == "5":
                print("Variance of Array:", np.var(self.array))
            elif choice == "6":
                print("Minimum value:", np.min(self.array))
            elif choice == "7":
                print("Maximum value:", np.max(self.array))
            elif choice == "8":
                p = float(input("Enter percentile (0-100): "))
                print(f"{p}th Percentile:", np.percentile(self.array, p))
            elif choice == "9":
                self.correlation()
            elif choice == "10":
                break
            else:
                print("Invalid choice. Try again.")

    def correlation(self):
        total = self.array.size
        print(f"Total elements needed: {total}")
        elems_input = input(f"Enter another array of same size ({total} elements separated by space): ").split()
        elems = list(map(float, elems_input))
        if len(elems) != total:
            print(f"Incorrect number of elements. Got {len(elems)}, expected {total}.")
            return
        other = np.array(elems).reshape(self.array.shape)

        # flatten both
        a_flat = self.array.flatten()
        b_flat = other.flatten()
        corr_matrix = np.corrcoef(a_flat, b_flat)
        print("\nCorrelation Coefficient Matrix:")
        print(corr_matrix)
        print("Correlation Coefficient (between arrays):", corr_matrix[0, 1])

# ---------- Menu-driven UI ----------
def main():
    analyzer = DataAnalytics()

    print("="*30)
    print("\nWelcome to the NumPy Analyzer!")
    print("="*30)

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nArray Creation:")
            print("Select the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            dim_choice = int(input("Enter your choice: "))
            analyzer = DataAnalytics.from_input(dim_choice)

            if analyzer.array is not None:
                while True:
                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")
                    sub_choice = input("Enter your choice: ").strip()
                    if sub_choice == "1":
                        analyzer.indexing()
                    elif sub_choice == "2":
                        analyzer.slicing()
                    elif sub_choice == "3":
                        break
                    else:
                        print("Invalid choice. Try again.")

        elif choice == "2":
            if analyzer.array is None:
                print("Create an array first.")
                continue
            print("\nMathematical Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot & Matrix Multiplication (2D)")
            op_choice = input("Enter your choice: ").strip()
            if op_choice == "1":
                analyzer.elementwise_operation("add")
            elif op_choice == "2":
                analyzer.elementwise_operation("sub")
            elif op_choice == "3":
                analyzer.elementwise_operation("mul")
            elif op_choice == "4":
                analyzer.elementwise_operation("div")
            elif op_choice == "5":
                analyzer.dot_and_matrix_multiplication()
            else:
                print("Invalid choice.")

        elif choice == "3":
            if analyzer.array is None:
                print("Create an array first.")
                continue
            print("\nCombine or Split Arrays:")
            print("1. Combine Arrays")
            print("2. Split Array")
            cs_choice = input("Enter your choice: ").strip()
            if cs_choice == "1":
                analyzer.combine_arrays()
            elif cs_choice == "2":
                analyzer.split_array()
            else:
                print("Invalid choice.")

        elif choice == "4":
            if analyzer.array is None:
                print("Create an array first.")
                continue
            print("\nSearch, Sort, and Filter:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            ssf_choice = input("Enter your choice: ").strip()
            if ssf_choice == "1":
                analyzer.search_value()
            elif ssf_choice == "2":
                analyzer.sort_array()
            elif ssf_choice == "3":
                analyzer.filter_values()
            else:
                print("Invalid choice.")

        elif choice == "5":
            analyzer.agg_and_stat()

        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            print("="*30)

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



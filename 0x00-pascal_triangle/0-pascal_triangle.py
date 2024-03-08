def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
    - n: Integer representing the number of rows.

    Returns:
    - List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

# For testing the code
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

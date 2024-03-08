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

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

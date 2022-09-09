import numpy as np


def sort_number() -> None:
    ...


if __name__ == "__main__":
    a = np.array([
        [
            np.array([0, 1, 2, 3]),
            np.array([4, 5, 6, 7])
        ],
        [
            np.array([8, 9, 10]),
            np.array([12, 13, 14])
        ]
    ])

    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(a[0, :1], end="\n\n")

    print('*' * 20)

    print(b[::-1, 1:], end="\n\n")  # reversed

    print(b[::, 1:], end="\n\n")  # Normal
    print(b[::-1, :1], end="\n\n")  # reversed order with only first column

    b[::, 2:] = 0  # reatribuição ao eixo fatiado.
    print(b, end="\n\n")

    names = np.array(["Henrique", "Millena", "Arthur", "Milene", "Default"])

    # validação boleana, isso gera um np.array com True, nas posições que forem válidas
    validate_name = names == "Henrique"

    # gerando um nArray aleatório com np.random.randn que tenha o mesmo número de linhas que o range de names
    random_numbers = np.random.randn(names.size, 4)

    print(validate_name, end="\n\n")
    print(random_numbers, end="\n\n")

    # in boolean nArray I will be access just the true lines.
    print(random_numbers[validate_name], end="\n\n")

    # boolean validation with indexation.
    print(random_numbers[validate_name, :2], end="\n\n")

    # Reverse nArray boolean logical, with not operator.
    print(random_numbers[~validate_name], end="\n\n")
    # or use
    negation_form = names != "Henrique"
    print(random_numbers[negation_form], end="\n\n")

    # idexation with aritmethics operators.

    # or condition - use | operator:
    dif_condition = (names == "Henrique") | (names == "Default")
    print(random_numbers[dif_condition], end="\n\n")

    # and condition - use & operator:
    personal_condition = (names != "Henrique") & (names != "Default")
    print(random_numbers[personal_condition], end="\n\n")

    # personal condition -> only negative numbers, it will return one unique nArray, with all negative numbers
    print(random_numbers[random_numbers < 0], end="\n\n")

    # dynamic attribution -> in all positions with negative numbers, i will substitute for zero
    random_numbers[random_numbers < 0] = 0
    print(random_numbers, end="\n\n")

    # dynamic selection in nArray
    new_example = np.empty((6, 3))

    for i in range(6):
        new_example[i] = i+2

    print(new_example, end="\n\n")

    # select especific lines in list of array
    print(new_example[[1, 3, 4]], end="\n\n")

    # select especific lines using the inverse form.
    print(new_example[[-2, -3, -4]], end="\n\n")

    # Here I create one nArray with 32 sequecial numbers values and I resize than to 8 lines and 4 columns
    arr = np.arange(32).reshape(8, 4)

    print(arr)


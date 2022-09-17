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
        new_example[i] = i + 2

    print(new_example, end="\n\n")

    # select especific lines in list of array
    print(new_example[[1, 3, 4]], end="\n\n")

    # select especific lines using the inverse form.
    print(new_example[[-2, -3, -4]], end="\n\n")

    # Here I create one nArray with 32 sequecial numbers values, and I resize than to 8 lines and 4 columns
    arr = np.arange(32).reshape(8, 4)

    print(arr)
    # get value by indice, it works like tuple, it may return a bidimentional nArray with selection.
    # [(1,0), (3,3), (7, 2)]
    print(arr[[1, 3, 7], [0, 3, 2]], end="\n\n")

    """
    First I select the lines 1, 4, 2, 3 of arr, after this,
      I select only the numbers after de (2) second line using [2:]
    """
    print(arr[[1, 4, 2, 3]][2:, [1, 3, 0, 2]], end="\n\n")

    print(arr[[5, 6, 7]][1:, ::-1], end="\n\n")

    print(arr[~arr % 2 == 0], end="\n\n")

    # generate one new nArray for exaple.
    arr = np.arange(30).reshape(3, 10)

    # when I use the (.T) I transpose the array data.
    # .T is equal to use .transpose()
    print(arr.T, end="\n\n")

    arr = np.random.randn(6, 3)

    print(np.dot(arr.T, arr))

    arr = np.arange(16).reshape((2, 2, 4))

    print(arr, end="\n\n")
    print(arr.T, end="\n\n")
    print(arr.transpose((1, 0, 2)), end="\n\n")

    """
    swapaxes:
        aceita um par de numero de eixos e troca os eixos indicados para reorganizar os dados.
        Return: swapaxer return just a data visualizer, not a copy, in which case, you will need perform an assignment
         to a variable.
    """
    print(arr.swapaxes(1, 2))

    """
    Universal Functions (Ufunc):
        Ufunc are functions that perform modifications on all the data of your nArray.
        Ufunc unic (Ufunc unária) = with unic param
        Ufunc binary (Ufunc binária) = with multiples params
    """
    ex_arr = np.arange(0, 10)

    # Unic Ufunc example
    print(np.sqrt(ex_arr), end="\n\n")
    print(np.exp(ex_arr), end="\n\n")

    ex_a, ex_b = np.random.randint(1, 8), np.random.randint(1, 8)
    print(np.sqrt(ex_a), end="\n\n")
    print(np.sqrt(ex_b), end="\n\n")

    # Binary Ufunc example
    print(np.maximum(ex_a, ex_b), end="\n\n")

    # Ufunc with multples returns
    ex_arr = np.random.rand(7) * 5

    print('ex_arr: ', ex_arr, end="\n\n")

    remainder, whole_part = np.modf(ex_arr)

    print(remainder, end="\n\n")
    print(whole_part, end="\n\n")

    """
    logical operations with np.where()
    np.where(conditional, if::true, ::else)
    """
    arr_value, arr_value2 = np.array([2, 4, 6, 8, 10]), np.array([3, 5, 7, 9, 11])
    arr_condition = np.array([True, False, True, True, False])

    # using only python list comprehension
    valid_value = [
        (x if y else z)
        for y, x, z in
        zip(arr_condition, arr_value, arr_value2)
    ]
    print(valid_value, end="\n\n")

    # using np.where
    new_value = np.where(arr_condition, arr_value, arr_value2)
    print(new_value, end="\n\n")

    # is posible use one general condition argument.
    new_example = np.where(arr_value > 5, arr_value, arr_value2)
    print(new_example, end="\n\n")

    # is possible set one unic value
    new_example = np.where(arr_value > 5, 'sim', arr_value2)
    print(new_example, end="\n\n")

    """
    math and static methods in numpy
    """
    arr = np.arange(0, 40).reshape(10, 4)
    print('arr: ', arr, end="\n\n")
    print(np.sum(arr), end="\n\n")  # it's like arr.sum()
    print(np.mean(arr), end="\n\n")  # it's like arr.mean()

    # using axis param, to apply operation in colum(0) or line(1) of matrice
    print(arr.sum(axis=0), end="\n\n")
    print(arr.mean(axis=1), end="\n\n")

    # cumsum is used for calc the acummulate sum.
    print(arr.cumsum(), end="\n\n")
    print('*' * 30, end="\n\n")

    # is possible use axis in cumsum on matrices
    arr = np.arange(40).reshape((4, 2, 5))
    print('arr: ', arr, end="\n\n")
    print(arr.cumsum(axis=0), end="\n\n")
    
    """
    methods for boolean nArrays
    """
    
    arr = np.random.randn(100)

    print('arr bool: ', arr, end="\n\n")
    print('arr: ', (arr > 0).sum(), end="\n\n")  # operation = (arr > 0).sum() it will sum all values true in condition

    arr_bool = np.array([True, False, True, True, False])

    # arr.all return True if all values is True
    print(arr_bool.all(), end="\n\n")

    # arr.any return True if any value is True
    print(arr_bool.any(), end="\n\n")




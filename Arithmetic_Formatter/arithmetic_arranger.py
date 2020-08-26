import re


def arithmetic_arranger(problems, solution=False):
    problem_str = str(problems)

    # Catch common errors -------------------------------------------------------------------------
    if len(problems) > 5:
        return "Error: Too many problems."

    if re.findall("[/|*]", problem_str):
        return "Error: Operator must be '+' or '-'."

    if re.search("[a-zA-Z]", problem_str) is not None:
        return "Error: Numbers must only contain digits."

    if re.search("[0-9][0-9][0-9][0-9][0-9]", problem_str):
        return "Error: Numbers cannot be more than four digits."

    # Split input into numbers and operators ---------------------------------------------------------
    sums_split = re.split(',', problem_str)
    sums_split_num = re.findall("[0-9]+", str(sums_split))

    first_number = sums_split_num[::2]

    second_number = sums_split_num[1::2]

    sums_split_operator = re.findall("[+|-]", str(sums_split))

    # Set up rows for calculations ---------------------------------------------------------
    first_num_row = ""
    second_num_and_operator_row = ""
    third_dash_row = ""
    fourth_sol_row = ""

    # Put together numbers, operators and dashes into one vertical equation  --------------------------
    for i, (first_num, operator, sec_num) in enumerate(zip(first_number, sums_split_operator, second_number)):
        max_len = max(len(first_num), len(sec_num))
        row_width = max_len + 2

        eq_solution = int(first_num) + int(sec_num) if operator == '+' else int(first_num) - int(sec_num)

        first_num_row += first_num.rjust(row_width)
        second_num_and_operator_row += operator + sec_num.rjust(row_width - 1)
        third_dash_row += ''.rjust(row_width, '-')
        fourth_sol_row += str(eq_solution).rjust(row_width).rstrip()

        if i < len(problems) - 1:
            first_num_row += '    '
            second_num_and_operator_row += '    '
            third_dash_row += '    '
            fourth_sol_row += '    '

    if solution:
        arranged_problems = f'{first_num_row}\n{second_num_and_operator_row}\n{third_dash_row}\n{fourth_sol_row}'
    else:
        arranged_problems = f'{first_num_row}\n{second_num_and_operator_row}\n{third_dash_row}'
    return arranged_problems

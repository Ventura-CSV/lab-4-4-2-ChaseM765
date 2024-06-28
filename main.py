def main():
    while True:
        try:
            number = int(input('Enter value: '))
        except ValueError:
            print('Invalid input: Input must be numeric')
            continue
        else:
            print(number)
            break

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()

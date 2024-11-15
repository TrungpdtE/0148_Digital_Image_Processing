def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    
    return True

def normalize(fullname):
    fullname = fullname.strip()
    fullname = fullname.lower()
    words = fullname.split(' ')
    
    for i, w in enumerate(words):
        words[i] = w.capitalize()
    
    return ' '.join(words)

def print_fullname(fullname):
    print('%-30s10'%(fullname))

def print_num(n):
    print('%09d'%(n))

def print_float(n):
    print('%.4f'%(n))

def split_dollar(w):
    return w.split('$')[1]

def count_letters(word):
    word = word.lower()
    dict_letters = {}

    for lt in word:
        if lt in dict_letters:
            dict_letters[lt] += 1
        else:
            dict_letters[lt] = 1
    return dict_letters

def split_even_odd(arr):
    evens = []
    odds = []

    for it in arr:
        if it % 2 == 0:
            evens.append(it)
        else:
            odds.append(it)
    return evens, odds

def ctdlcb_bai04():
    set_toan = {'An', 'Binh', 'Chi', 'Dung'}
    set_van = {'An', 'Chi', 'Giang'}

    print(set_toan.intersection(set_van))
    print(set_toan.difference(set_van))
    print(set_van.difference(set_toan))
    print(len(set_toan.union(set_van)))

def bttt_bai01():
    students = ['Giang', 'Binh', 'An', 'Dung', 'Chi']
    print(students)
    # interchange sort
    n = len(students)
    for i in range(0, n-1, 1): # 0 -> n-2
        for j in range(i+1, n, 1): # i+1 -> n-1
            if students[i] > students[j]:
                students[i],students[j] = students[j], students[i]
    
    print(students)

if __name__ == '__main__':
    print(is_leap_year(1900))
    print(is_prime(9))
    print(normalize('nguyEN thAnh aN'))
    print_fullname('Thành An')
    print_num(123)
    print_float(123456.12)
    print(split_dollar('Thanh$An$Nguyen'))
    print(count_letters('Nguyen Thanh An'))
    print(split_even_odd(range(10)))
    ctdlcb_bai04()
    bttt_bai01()
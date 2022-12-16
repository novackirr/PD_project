#IDcomplexity - переменная, определяющая сложность (уровень вложенности)
#IDvariant - переменная, определяющая вариант (от нее зависит, какие функции выбираются)

import latex2sympy2
#import hashlib
import random
import sympy
from sympy import cos, sin, exp, root, cot, tan, E, log, div, pi, S #, preview
from sympy.calculus.util import continuous_domain


def F1(IDcomplexity: int, IDvariant: str, var: str) -> str:
    '''
    Первая часть генератора выражений
    генерирует только функции (sin, cos, и т.д.)
    '''

    if IDcomplexity > 0:
        k: str = IDvariant[IDcomplexity-1]
        # k: int = hash_dict[random.choice(hash_key)]
        if k == '0':
            return r'\sin{'+F1(IDcomplexity-1, IDvariant, var)+'}'
        elif k == '1':
            return r'\cos{'+F1(IDcomplexity-1, IDvariant, var)+'}'
        elif k == '2':
            return r'\tan{'+F1(IDcomplexity-1, IDvariant, var)+'}'
            #return r'\sqrt['+str(random.randint(0,9))+']{'+F1(IDcomplexity-1,IDvariant)+'}'
        elif k == '3':
            return r'\cot{'+F1(IDcomplexity-1, IDvariant, var)+'}'
            #return r'\sqrt{'+F1(IDcomplexity-1,IDvariant)+'}'
        elif k == '4':
            return 'e^{'+F1(IDcomplexity-1, IDvariant, var)+'}'
        elif k == '5':
            return str(random.randint(1,3))+'^{'+F1(IDcomplexity-1, IDvariant, var)+'}'
        elif k == '6':
            return r'\left ('+F1(IDcomplexity-1, IDvariant, var)+r'\right )^'+str(random.randint(0,3))
        elif k in'789':
            return str(random.randint(1,2))+F1(IDcomplexity-1, IDvariant, var)                                                                  
    else:
        return var


def F2(IDcomplexity: int, IDvariant: str, var: str = 'x') -> str:
    '''
    Вторая часть генератора выражений
    определяет будет ли итоговое выражение
    суммой (f + g), отношением (f / g), 
    произведением (f * g) или разностью (f - g)
    '''

    IDvariant2 = str(IDvariant)[2:] + str(IDvariant)[:2]
    if IDcomplexity > 1:    
        k: str = IDvariant[IDcomplexity-1]
        # k: int = hash_dict[random.choice(hash_key)]
        if k in '0,1':
            return F1(IDcomplexity-1, IDvariant, var)+'+'+F1(IDcomplexity-1, IDvariant2, var)
        elif k in '2,3,4':
            return r'\frac{'+F1(IDcomplexity-1, IDvariant, var)+'}{'+F1(IDcomplexity-1, IDvariant2, var)+'}'
        elif k in '5,6,7':
            return F1(IDcomplexity-1, IDvariant, var)+r'\cdot'+F1(IDcomplexity-1, IDvariant2, var)
        elif k in '8,9':
            return F1(IDcomplexity-1, IDvariant, var)+'-'+F1(IDcomplexity-1, IDvariant2, var)

def pairwise_simple(x: int, y: int) -> bool:
    '''
    Функция для определения
    являются ли 2 числа взаимо простыми
    (Нужно для 6-ого задания)
    '''

    while (x and y):
        if (x > y):
            x %= y
        else:
            y %= x
    if (x + y == 1):
        return True
    else:
        return False

def prty_eq(eq) -> str:
    return str(eq).lower().replace(' ', '')

def norm_num(n: str) -> str:
    return n.replace(' ', '').replace(',', '.')

def rgr_gen(var: str):
    '''
    Функция-итератор, которая бесконечно
    выдаёт по одному выражению, пока не сработает break
    '''

    while True:
        '''
        random.seed(hash_key)
        salt = mospolytech1928145
        # Имя Фамилия Отчество УчебнаяГруппа ВремяЗахода Соль
        hash_str = f'{Name}{SName}{LName}{Group}{timeOfEnter}{salt}'
        hash_key = hashlib.md5(bytes(hash_str, 'utf-8')).hexdigest()
        
        hash_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,'h': 8, 'i': 9,
            'j': 0, 'k': 1, 'l': 2, 'm': 3, 'n': 4, 'o': 5,'p': 6, 'q': 7, 'r': 8, 's': 9,
            't': 0, 'u': 1, 'v': 2, 'w': 3,'x': 4, 'y': 5, 'z': 6}
        '''
        hash_key = str(random.randint(10**10, 10**11))
        result = sympy.simplify( latex2sympy2.latex2sympy( F2(4, hash_key, var) ) )
        n = 0
        
        for s in '0123456789':
            n += str(result).count(s)
        m = n/len(str(result))
        
        if var in str(result) and len(str(result)) < 40 and m <= 0.2:
            yield result

def Task1(generator: iter, var: str ='x'):
    n = 6
    for eq in generator(var):
        r = str(sympy.diff(eq, var))
        if len(r) < 45 and r != '0':
            n -= 1
            print(f'equation = {prty_eq(eq)},\t diff = {prty_eq(r)}')
            if n == 0:
                break

def Task2(generator: iter, var: str = 't'):
    # http://mathprofi.ru/proizvodnye_neyavnoi_parametricheskoi_funkcii.html
    pass

def Task3(generator, var: str = 'x'):
    n = 2
    for eq in generator(var):
        r = str(sympy.diff(eq, var, var))
        if len(r) < 50 and r != '0':
            n -= 1
            print(f'equation = {prty_eq(eq)},\t diff^2 = {prty_eq(r)}')
        if n == 0:
            break

def Task4(generator: iter, var: str = 't'):
    # https://function-x.ru/derivative_and_tangent.html
    pass

def Task5():
    pass

def Task6(var: str = 'x'):
    n = 10
    
    variant1 = random.randint(0, 1)
    k = (-1)**variant1
    x = sympy.Symbol(var)
    for _ in range(n):
        eq = random.choice([sin, cos, tan, cot, root, cot, pow, E])#,div, E])
        eq = div
        if eq == sin or eq == cos:
            variant2 = random.randint(0, 1)
            b = k*random.randint(1,20)

            if variant2:
                a = random.choice([0, 90])
                f = eq(x)
            else:
                a = random.randint(1,15)
                b = random.randint(30,40)
                f = eq(a*pi*x/b)

            ''' 
				ANS
			'''
            ans = f.subs(x, a) + sympy.diff(f).subs(x, a)*b

        elif eq == tan or eq == cot:
            if eq == tan:
                a = 0
            else:
                a = 90
                
            b = k*random.randint(1,9)
            f = eq(x)

        elif eq == pow:
            a = random.randint(1,4)
            b = random.randint(1,3)
            c = k*random.randint(1,9) / 100
            f = eq(x, b)
            #ans = f.subs(x, a) + sympy.diff(f).subs(x, a)*c
            print(f'{a}^{c+b} ans={round(float(ans), 3)}')

        elif eq == div:
            '''
            TODO Solver
            '''
            b = k*random.randint(1,9) / 100
            degree = random.randint(2,4)
            a = random.randint(1,4)**degree
            k1 = random.randint(1,9)
            f = k1/root(x, degree)
            print(f)
            #ans = f.subs(x, a) + sympy.diff(f).subs(x, a)*b
            print(f'{1}/root[{degree}]{a+b} ans={round(float(ans), 3)}')

        elif eq == root:
            f = sympy.core.numbers.Integer(3.8)
            while type(f) == sympy.core.numbers.Integer:
                a = random.randint(1,9)
                b = random.randint(a,9)
                l = random.choice(tuple(sympy.primerange(0, 100)))
                while not pairwise_simple(a, b):
                    a = random.randint(1,9)
                    b = random.randint(a,9)
                f = eq(l**a, b)
            #print(type(f))

        elif eq == E:
            a = random.randint(1,3)
            b = k*random.randint(1,9)/100
            f = E**(a*x)
            #ans = f.subs(x, a) + sympy.diff(f).subs(x, a)*b

        '''
        TODO Solver
        '''
        
        #print(f)

def Task7(generator: iter, var: str = 'x'):
    n = 2
    for eq in generator(var):
        r = sympy.diff(eq, var)
        var_sympy = sympy.Symbol(var)

        try:
            domain_f = continuous_domain(r, var_sympy, S.Reals)
        except NotImplementedError:
            continue
        
        try:
            domain = [i for i in range(-3, 6) if i in domain_f]
        except TypeError:
            continue
        
        if r.atoms(sin) or r.atoms(cos):
            try:
                if pi in domain_f:
                    domain = [-3*pi/2, -pi, -3*pi/4, -pi/2, -pi/4, 0]
                    domain += [-i for i in domain[::-1][1:]]
            except TypeError:
                continue
        
        domain_upper = random.choice(sorted(domain)[1:])
        domain_lower = random.choice([i for i in domain if i < domain_upper])

        if len(str(r)) < 50 and r != 0:
            n -= 1
            print(f'equation={eq},\t bounds={(domain_lower, domain_upper)}')
        if n == 0:
            break

def Task8():
    pass

'''
with open('solution.png', 'wb') as outputfile:
    sympy.preview(solution, viewer='BytesIO', outputbuffer=outputfile)
'''

#print('#'*10+'Task1'+'#'*10)
#Task1(rgr_gen)
#print()
#print('#'*10+'Task3'+'#'*10)
#Task3(rgr_gen)
#print()
#print('#'*10+'Task6'+'#'*10)
Task6()
#print()
#print('#'*10+'Task7'+'#'*10)
#Task7(rgr_gen)

'''
JSON
{
    Task1: {
        eq: '22*cos(x)-cos(11*x)',
        ans: '-22*sin(x)+11*sin(11*x)'
    }
}
'''
import os

def thousand_sep(num):
    return ('{:,}'.format(num))

Successione_di_Fibonacci = [1, 1]

_count = 0

for _ in range(10000):

    _count += 1

    if len(Successione_di_Fibonacci) < _count:

        Successione_di_Fibonacci.append(Successione_di_Fibonacci[_count-2] + Successione_di_Fibonacci[_count-3])

while True:

    os.system('cls')

    try:

        target = int(input('機器人：閣下欲知費式數列何項？\n\n您：'))

        os.system('cls')

        if target < 0:

            raise ValueError
        
        elif target == 0:

            print('費波那契數列 第 0 項：\n\n0')

            input('\nENTER 鍵繼續...')

        else:

            print('機器人：請稍後...')

            if len(Successione_di_Fibonacci) <= target:
                
                os.system('cls')

                for _ in range(target - len(Successione_di_Fibonacci)):

                    _count += 1

                    Successione_di_Fibonacci.append(Successione_di_Fibonacci[_count-2] + Successione_di_Fibonacci[_count-3])

                    print(len(Successione_di_Fibonacci), '|', Successione_di_Fibonacci[_count-2] + Successione_di_Fibonacci[_count-3])

            os.system('cls')

            if len(thousand_sep(Successione_di_Fibonacci[target-1])) > 100:

                print('機器人：費波那契數列第 {} 項計算完成！由於數值過大，該數值已被儲存在 \'Successione_di_Fibonacci.txt\''.format(target))

                with open(file='Successione_di_Fibonacci.txt', mode='w+', encoding='utf-8') as file:

                    file.write('費波那契數列 第 {} 項：\n\n{}'.format(target, thousand_sep(Successione_di_Fibonacci[target-1])))

            else:
                    
                print('費波那契數列 第 {} 項：\n\n{}'.format(target, thousand_sep(Successione_di_Fibonacci[target-1])))

            input('\nENTER 鍵繼續...')

    except ValueError as error:

        input(error)


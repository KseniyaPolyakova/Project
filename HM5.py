{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cf3ae727",
   "metadata": {},
   "source": [
    "Для того чтобы оценка за данную работу пошла в зачёт нужно отправить ссылку на нее в гит или ноутбук до <b> 17.10.2021 17:00 </b>."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfc3e82d",
   "metadata": {},
   "source": [
    "<b>Задание 1.</b> Создайте массив, который состоит из целых чисел от -50 до 50 включительно. Затем удалите последние 25 элеметов массива. Затем разверните массив. Добавьте в конец массива 999. Создайте новый массив в который войдут все четные числа из ранее полученного массива и напечатайте его."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f65fc6c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40, -42, -44, -46, -48, -50]\n"
     ]
    }
   ],
   "source": [
    "mylist = list(range(-50, 51))\n",
    "for i in range(25):\n",
    "    mylist.pop()\n",
    "mylist.reverse()\n",
    "mylist.append(999)\n",
    "newlist = [i for i in mylist if i % 2 == 0]\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4907145c",
   "metadata": {},
   "source": [
    "<b>Задание 2.</b> Даны несколько массивов целых чисел (A, B, C, D). Напишите программный код, с помощью которого вы сможете определить длину самой длинной непрерывной последовательности равных значений для каждого из массивов."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "02880b3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7, 3, 3]\n"
     ]
    }
   ],
   "source": [
    "# [1, 1, 1, 2, 3, 4, 5, 6, 3, 4, 1, 1, 1, 1] - самая длинная последовательность длины 4\n",
    "A = [1] * 20 + [1, 1, 3] * 30 + [1] * 21\n",
    "\n",
    "B = list(range(1, 9, 2)) * 3 + list(range(4, 1, 1)) * 2 + [3] * 3\n",
    "B.pop()\n",
    "B.reverse()\n",
    "B.pop()\n",
    "B.reverse()\n",
    "\n",
    "C = [b - 2 for b in B]\n",
    "C.reverse()\n",
    "C =  A + C\n",
    "\n",
    "D = [777] + [666] + [1,2,1,1] * 2 + [1,1,1,1,3]*3 + [1, 4] * 2\n",
    "print(B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a28bc2bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "2\n",
      "23\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def f(A):\n",
    "    maxx = 1\n",
    "    a = 1\n",
    "    for i in range(len(A) - 1):\n",
    "        if A[i + 1] == A[i]:\n",
    "            a += 1\n",
    "            if maxx < a:\n",
    "                maxx = a\n",
    "        else:\n",
    "            a = 1\n",
    "    return maxx\n",
    "print(f(A))\n",
    "print(f(B))\n",
    "print(f(C))\n",
    "print(f(D))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8efc26b7",
   "metadata": {},
   "source": [
    "<b>Задание 3.</b> Напишите функция, которая на вход принимает прямоугольную матрицу и возвращает транспонированную матрицу. Протестируйте функцию на матрицах A, B, C."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d27847e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "A = [[1, 1], [1, 0]]\n",
    "B = [[2, 3, 4], [4, 5, 6], [7, -1, -2], [-4, -6, 99], [1, 0, 1]]\n",
    "C = [[1, 2, 3, 4, 5]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8cce8472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 1], [1, 0]]\n",
      "[[2, 4, 7, -4, 1], [3, 5, -1, -6, 0], [4, 6, -2, 99, 1]]\n",
      "[[1], [2], [3], [4], [5]]\n"
     ]
    }
   ],
   "source": [
    "def m(A):\n",
    "    At = []\n",
    "    a = []\n",
    "    for i in range(len(A[0])):\n",
    "        for j in range(len(A)):\n",
    "            a.append(A[j][i])\n",
    "        At.append(a)\n",
    "        a = []\n",
    "    return At\n",
    "print(m(A))\n",
    "print(m(B))\n",
    "print(m(C))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

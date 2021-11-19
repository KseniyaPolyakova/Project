{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Создайте класс Point(x, y) x, y - координаты точки на плоскости.\n",
    "- Реализуйте два метода a.distanceTo(b) - евкливодов расстояние между $a$ и $b$\n",
    "- Переопределите __str__ так чтобы при печати экземпляра выводилось (x, y) - то есть координаты точки"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Point:\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "    def x(self):\n",
    "        return self.x\n",
    "    def y(self):\n",
    "        return self.y\n",
    "    def distanceTo(self, second):\n",
    "        return ((self.x - second.x) ** 2 + (self.y - second.y) ** 2) ** 0.5\n",
    "    def __str__(self):\n",
    "        return \"(\" + str(self.x) + \",\" + str(self.y) +  \")\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "3\n",
      "1\n",
      "(1.0,3.0) (3.0,1.0)\n",
      "2.8284271247461903\n"
     ]
    }
   ],
   "source": [
    "x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())\n",
    "point1 = Point(x1, y1)\n",
    "point2 = Point(x2, y2)\n",
    "print(point1, point2)\n",
    "print(Point.distanceTo(point1, point2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.8284271247461903\n"
     ]
    }
   ],
   "source": [
    "print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- После того как Вы создадите класс запустите следующий код"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "random.seed(42)\n",
    "points = list()\n",
    "for i in range(1000):\n",
    "    x = random.randint(1, 100)\n",
    "    y = random.randint(1, 100)\n",
    "    points.append(Point(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Напишите метод, который определит у какой из заданых точек больше всего соседей в радиусе 5.\n",
    "- Если таких точек несколько, то тогда выведите точку с наименьше суммой координат, если таких точек несколько, то выведите точку с наименьше абсциссой."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(96,71)\n",
      "(37,78)\n",
      "(16,59)\n",
      "(96,70)\n",
      "(96,71)\n",
      "(12,61)\n",
      "(16,59)\n"
     ]
    }
   ],
   "source": [
    "count = 0\n",
    "list1 = []\n",
    "for i in points:\n",
    "    for j in points:\n",
    "        point1 = i\n",
    "        point2 = j\n",
    "        if Point.distanceTo(point1, point2) <= 5:\n",
    "            count += 1\n",
    "    list1.append(count)\n",
    "    count = 0\n",
    "maxx = max(list1)\n",
    "list_point = []\n",
    "for i in range(len(list1)):\n",
    "    if list1[i] == maxx:\n",
    "        list_point.append(points[i])\n",
    "for i in list_point:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(12,61)\n"
     ]
    }
   ],
   "source": [
    "min_sum = 200\n",
    "list_point2 = []\n",
    "for i in list_point:\n",
    "    x = Point.x(i)\n",
    "    y = Point.y(i)\n",
    "    summ = x + y\n",
    "    if summ <= min_sum:\n",
    "        min_sum = summ\n",
    "for i in list_point:\n",
    "    x = Point.x(i)\n",
    "    y = Point.y(i)\n",
    "    if x + y == min_sum:\n",
    "        list_point2.append(i)\n",
    "if len(list_point2) == 1:\n",
    "    print(list_point2[0])\n",
    "else:\n",
    "    min_x = 100\n",
    "    for i in list_point:\n",
    "        x = Point.x(i)\n",
    "        if x < min_x:\n",
    "            min_x = x\n",
    "            print(i)\n",
    "            break"
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
 "nbformat_minor": 4
}

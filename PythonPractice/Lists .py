{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'13579'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystr = '0123456789'\n",
    "mystr[1::2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "mylst = [1, 2.3, 4 + 5j, True, 'str', [1,2,3], ('a','b','c')]\n",
    "print(type (mylst))\n",
    "print (type(mylst[1]))\n",
    "mylst[-2][-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[True, (4+5j), 2.3, 1]\n"
     ]
    }
   ],
   "source": [
    "# Slicing (Start: Stop : step) defaultvalues: start: 0 stop: len-1 step =1\n",
    "# print(mylst[:])\n",
    "# print(mylst[::])\n",
    "mylst = [1, 2.3, 4 + 5j, True, 'str', [1,2,3], ('a','b','c')]\n",
    "# print(mylst[:-1])\n",
    "# print(mylst[-4:])\n",
    "print(mylst[3::-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "101"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mylt = [1,2,3,[1,2,3,[4,5,7,[10,20,90,[100,101]]]]]\n",
    "mylt[-1][-1][-1][-1][-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2.3, (4+5j), True, 'str', [1, 2, 3], ('a', 'b', 'c'), 'j', '1', 'g', '2', 'n']\n"
     ]
    }
   ],
   "source": [
    "mylst = [1, 2.3, 4 + 5j, True, 'str', [1,2,3], ('a','b','c')]\n",
    "mylst.extend('j1g2n')\n",
    "print(mylst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2.3, (4+5j), True, 'str', [1, 2, 3], ('a', 'b', 'c'), 'j', 'g', '2', 'n']\n",
      "1 <class 'str'>\n"
     ]
    }
   ],
   "source": [
    "# mylst.insert(2, 'insert')\n",
    "\n",
    "a = mylst.pop(-4)\n",
    "print(mylst)\n",
    "print(a, type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mylst2 = [1,2,3,4,5,6,7,8,9,10]\n",
    "for each in mylst2:\n",
    "    print(each + 2)\n",
    "mylst2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "mylst2 = [1,2,3,4,5,6,7,8,9,10]\n",
    "mylst3 = []\n",
    "for each in mylst2:\n",
    "    mylst3.append(each ** 2)\n",
    "print(mylst3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 1, 2, 3, 1, 2, 3]"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1 = [1,2,3]\n",
    "l2 = [4,5,6]\n",
    "l1 * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(3 in mylst2) and (5 in mylst2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

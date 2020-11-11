{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO WORLD\n",
      "hello @orld\n",
      "Hello world\n",
      "he@@o wor@d\n",
      "hello -1orld\n"
     ]
    }
   ],
   "source": [
    "mystr ='hello world'\n",
    "print(mystr.upper())\n",
    "print(mystr.replace('w', '@'))\n",
    "print(mystr.capitalize())\n",
    "print(mystr.replace('l', '@', -3))\n",
    "print(mystr.replace('w','-1'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Negative number -5\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "num = \n",
    "if(num > 0):\n",
    "    print('positive number', num)\n",
    "    print(num>0)\n",
    "elif(num < 0):\n",
    "    print('Negative number', num)\n",
    "    print(num<0)\n",
    "else:\n",
    "    print('number is zero', num)\n",
    "    print(num ==0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your num: 9\n",
      "9 is a odd number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter your num: \"))\n",
    "if(num % 2 == 0):\n",
    "    print('{} is a Even number'.format(num))\n",
    "else:\n",
    "    print('{} is a odd number'.format(num))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your scr: -10\n",
      "-10 is a Grade F\n"
     ]
    }
   ],
   "source": [
    "scr = int(input(\"enter your scr: \"))\n",
    "if(scr >= 90 & scr < 100):\n",
    "    print('{} is a Grade A'.format(scr))\n",
    "elif(scr >= 80 and scr < 89):\n",
    "    print('{} is a Grade B'.format(scr))\n",
    "elif(scr >= 70 and scr < 79):\n",
    "    print('{} is a Grade c'.format(scr))\n",
    "elif(scr >= 60 and scr < 69):\n",
    "    print('{} is a Grade F'.format(scr))\n",
    "else:\n",
    "    print('{} is a Grade F'.format(scr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a two value: 10 20\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "int() argument must be a string, a bytes-like object or a number, not 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-47-171a3e0f9aac>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mop1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter a two value: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;31m#op1 = float(input(\"enter your operend 1st: \"))\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#op2 = float(input(\"enter your operend 2nd: \"))\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0moperator\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"what you wanna do +,-,*,/,% ?: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mif\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0moperator\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'+'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: int() argument must be a string, a bytes-like object or a number, not 'list'"
     ]
    }
   ],
   "source": [
    "# op1, op2 = int(input(\"Enter a two value: \").split())\n",
    "op1 = float(input(\"enter your operend 1st: \"))\n",
    "op2 = float(input(\"enter your operend 2nd: \"))\n",
    "operator = input(\"what you wanna do +,-,*,/,% ?: \")\n",
    "if (operator == '+'):\n",
    "    print('{} is the result'.format(op1 + op2))\n",
    "elif(operator == '-'):\n",
    "    print('{} is the result'.format(op1 - op2))\n",
    "elif(operator == '*'):\n",
    "    print('{} is the result'.format(op1 * op2))\n",
    "elif(operator == '/'):\n",
    "    if(op2 == 0):\n",
    "        print('Denominator should not be zero')\n",
    "    else:\n",
    "        print('{} is the result'.format(op1 / op2))\n",
    "elif(operator == '%'):\n",
    "    print('{} is the result'.format(op1 % op2))\n",
    "else:\n",
    "    print('You missed something')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# n1 = int(input())\n",
    "# print(type(n1))\n",
    "n1 = 2\n",
    "(2.0).is_integer()\n",
    "# if (isinstance(int(n1), int)):\n",
    "#     print('integer number')\n",
    "# elif(isinstance(float(n1), float)):\n",
    "#     print('float number')\n",
    "# else:\n",
    "#     print('enter valid number')\n",
    "# # if (isinstance (n1,float)\n",
    "\n",
    "    \n",
    "# print (n1, type(n1))\n",
    "# print('\\n',n1,'\\n',n2,'\\n',n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(-2.0).is_integer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your operend 1st: 1\n",
      "enter your operend 2nd: 2\n",
      "enter your operend 3rd: e\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: 'e'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-122-d6aa06de8ac6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mn1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"enter your operend 1st: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mn2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"enter your operend 2nd: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mn3\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"enter your operend 3rd: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn1\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mn2\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mn3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'e'"
     ]
    }
   ],
   "source": [
    "n1 = float(input(\"enter your operend 1st: \"))\n",
    "n2 = float(input(\"enter your operend 2nd: \"))\n",
    "n3 = float(input(\"enter your operend 3rd: \"))\n",
    "\n",
    "if(n1 != n2 != n3):\n",
    "    if (n3 < n1 and n1 < n2):\n",
    "        print(n2, 'is the lasgest number')\n",
    "    elif(n1 > n3 and n1 > n2):\n",
    "        print(n1, 'is the largest number')\n",
    "    else:\n",
    "        print(n3, 'is the largest number')\n",
    "\n",
    "    if (n1 < n3 and n1 < n2):\n",
    "        print(n1, 'is the smallest number')\n",
    "    elif(n2 < n3 and n2 < n1):\n",
    "        print(n2, 'is the smallest number')\n",
    "    else:\n",
    "        print(n3, 'is the smallest number')\n",
    "else:\n",
    "    print('All are equal')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4(b): [10,20,30], [0, -1 ,10], [-3, -2, -4], [10,100,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(1, 10, 3)\n"
     ]
    }
   ],
   "source": [
    "lst = (range (1,10,3))\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2552478402608\n",
      "2552475709232\n",
      "24\n",
      "52\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "a = 1.2\n",
    "b = 'aaz'\n",
    "print (id(a))\n",
    "print (id(b))\n",
    "print (sys.getsizeof(a))\n",
    "print (sys.getsizeof(b))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n",
      "21\n",
      "22\n",
      "23\n",
      "24\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "for chk in range (1,50):\n",
    "    if (chk >= 15 and chk <=25):\n",
    "        print(chk)\n",
    "   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "sumx = 0\n",
    "a= 1\n",
    "while (a <= 100):\n",
    "    sumx = sumx + a\n",
    "    a = a + 1\n",
    "print(sumx)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "sumx = 0\n",
    "for var in range(101):\n",
    "    sumx = sumx + var\n",
    "print (sumx)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: a\n",
      "Wrong input you have  2 attemps left\n",
      "Enter a number: d\n",
      "Wrong input you have  1 attemps left\n",
      "Enter a number: g\n",
      "exceeded limit\n"
     ]
    }
   ],
   "source": [
    "chance = 0\n",
    "maxlimit = 2\n",
    "while(True):\n",
    "    num = input(\"Enter a number: \") \n",
    "    if (num.isnumeric()):\n",
    "        continue\n",
    "    elif (chance < maxlimit):\n",
    "        print('Wrong input you have ', maxlimit-chance,'attemps left')\n",
    "        chance += 1\n",
    "        continue\n",
    "    else:\n",
    "        print('exceeded limit')\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "s\n",
      "worng input\n"
     ]
    }
   ],
   "source": [
    "import itertools\n",
    "for var in itertools.count():\n",
    "    num = input()\n",
    "    if (num.isnumeric()):\n",
    "        var = 0\n",
    "        continue\n",
    "    else:\n",
    "        print('worng input')\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 291,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1500,1505,1510,1512,1515,1519,1520,1525,1526,1530,1533,1535,1540,1545,1547,1550,1554,1555,1560,1561,1565,1568,1570,1575,1580,1582,1585,1589,1590,1595,1596,1600,1603,1605,1610,1615,1617,1620,1624,1625,1630,1631,1635,1638,1640,1645,1650,1652,1655,1659,1660,1665,1666,1670,1673,1675,1680,1685,1687,1690,1694,1695,1700,1701,1705,1708,1710,1715,1720,1722,1725,1729,1730,1735,1736,1740,1743,1745,1750,1755,1757,1760,1764,1765,1770,1771,1775,1778,1780,1785,1790,1792,1795,1799,1800,1805,1806,1810,1813,1815,1820,1825,1827,1830,1834,1835,1840,1841,1845,1848,1850,1855,1860,1862,1865,1869,1870,1875,1876,1880,1883,1885,1890,1895,1897,1900,1904,1905,1910,1911,1915,1918,1920,1925,1930,1932,1935,1939,1940,1945,1946,1950,1953,1955,1960,1965,1967,1970,1974,1975,1980,1981,1985,1988,1990,1995,2000,2002,2005,2009,2010,2015,2016,2020,2023,2025,2030,2035,2037,2040,2044,2045,2050,2051,2055,2058,2060,2065,2070,2072,2075,2079,2080,2085,2086,2090,2093,2095,2100,2105,2107,2110,2114,2115,2120,2121,2125,2128,2130,2135,2140,2142,2145,2149,2150,2155,2156,2160,2163,2165,2170,2175,2177,2180,2184,2185,2190,2191,2195,2198,2200,2205,2210,2212,2215,2219,2220,2225,2226,2230,2233,2235,2240,2245,2247,2250,2254,2255,2260,2261,2265,2268,2270,2275,2280,2282,2285,2289,2290,2295,2296,2300,2303,2305,2310,2315,2317,2320,2324,2325,2330,2331,2335,2338,2340,2345,2350,2352,2355,2359,2360,2365,2366,2370,2373,2375,2380,2385,2387,2390,2394,2395,2400,2401,2405,2408,2410,2415,2420,2422,2425,2429,2430,2435,2436,2440,2443,2445,2450,2455,2457,2460,2464,2465,2470,2471,2475,2478,2480,2485,2490,2492,2495,2499,2500,2505,2506,2510,2513,2515,2520,2525,2527,2530,2534,2535,2540,2541,2545,2548,2550,2555,2560,2562,2565,2569,2570,2575,2576,2580,2583,2585,2590,2595,2597,2600,2604,2605,2610,2611,2615,2618,2620,2625,2630,2632,2635,2639,2640,2645,2646,2650,2653,2655,2660,2665,2667,2670,2674,2675,2680,2681,2685,2688,2690,2695,2700\n"
     ]
    }
   ],
   "source": [
    "n1 =[]\n",
    "for var in range (1500, 2701):\n",
    "    if ((var % 7 == 0) | (var % 5 == 0)):\n",
    "        n1.append(str(var))\n",
    "print (','.join(n1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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

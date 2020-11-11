{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
    "        break"
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

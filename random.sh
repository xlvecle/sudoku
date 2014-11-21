str=`python random_sudoku.py`
str=`./solve_sudoku $str`
str=`python remove.py $str`
python show.py $str

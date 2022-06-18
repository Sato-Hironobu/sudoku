from problems import problems

import sys

def print_sudoku(sudoku):
    
    print("-" * 17)
    for i in range(81):
            if i % 27 == 26:
                print(sudoku[i])
                print("-" * 17)
            elif i % 9 == 8:
                print(sudoku[i])
            elif i % 3 == 2:
                print(sudoku[i], end="|")
            else:
                print(sudoku[i], end=" ")
                
class Sudoku:
    
    def __init__(self, source):
        self.body = []
        for char in source:
            self.body.append(int(char))
        self.table = [ [1 for i in range(81)] for j in range(9)]
        self.startup()
    
    def startup(self):
        for position in range(81):
            num = self.body[position]
            if num:
                for i in range(9):
                    if i != num - 1:
                        self.table[i][position] = 0
                for type in ("row", "column", "square"):
                    for j in self.get_block_of_position(position, type=type):
                        if j != position:
                            self.table[num-1][j] = 0
        
    def print(self):
        print_sudoku(self.body)
    
    def check_table(self):
        for i in range(9):
            print(f"Table for {i+1}")
            print_sudoku(self.table[i])
    
    def get_block_of_position(self, position, type):
        if type == "row":
            block_number = position // 9
        elif type == "column":
            block_number = position % 9
        else:
            block_number = position % 9 // 3 + position // 9 // 3 * 3
        return self.get_block_by_block_number(block_number, type)
        
    def get_block_by_block_number(self, block_number, type):
        if type == "row":
            return [block_number * 9 + i for i in range(9) ]
        elif type == "column":
            return [block_number + 9 * i for i in range(9)]
        else:
            head = block_number // 3 * 27 + block_number % 3 * 3
            return [head + 9 * i + j for i in range(3) for j in range(3)]

    def update(self, number):
        changed = 0
        for i in range(9):
            for type in ("row", "column", "square"):
                for block_number in range(9):
                    found = self.search_block(i, type, block_number)
                    if found:
                        self.body[found] = i + 1
                        changed = 1
        return changed
    
    def search_block(self, num, type, block_number):
        block = self.get_block_by_block_number(block_number, type=type)
        cnt = 0
        for i in block:
            if self.table[num][i] == 1:
                position = i
                cnt += 1
            if cnt == 1:
                return position
        return None
        
    def modify(self):
        pass

    def main(self):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prob_num = int(sys.argv[1])
    else:
        prob_num = 1
    source = problems[prob_num - 1]
    sudoku = Sudoku(source)
    sudoku.print()
    sudoku.check_table()
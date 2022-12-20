# A - Rock B - Paper C - Scissors
# X - LOSE Y - DRAW Z - WIN
# 1 - Rock 2 - Paper 3 - Scissors 
# 0 - Lost 6 - Win 3 - Draw 

def main():
    totalWin = 0
    
    with open("day2input.txt") as f:
        lines = f.readlines()
        f.close()
                
    for i in lines:
        if i[2] == 'X':
            if i[0] == 'A':
                totalWin += 3
            if i[0] == 'B':
                totalWin += 1
            if i[0] == 'C':
                totalWin += 2
        if i[2] == 'Y':
            totalWin += 3
            if i[0] == 'A':
                totalWin += 1
            if i[0] == 'B':
                totalWin += 2
            if i[0] == 'C':
                totalWin += 3    
        if i[2] == 'Z':
            totalWin += 6
            if i[0] == 'A':
                totalWin += 2
            if i[0] == 'B':
                totalWin += 3
            if i[0] == 'C':
                totalWin += 1    
            
            
    print(totalWin)
        
 
 
    
if __name__ == "__main__":
    main()
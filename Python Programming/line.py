line_1 = []
line_2 = []

def main():
    global line_1,line_2
    for i in range(0,12):
        if i < 3:
            get_point = float(input("Enter x,y,z Co-ordinates of 1st Position Vecotr: "))
            line_1.append(get_point)
        elif 2 < i < 6 :
            get_point = float(input("Enter x,y,z Co-ordinates of 1st Displacement Vecotr: "))
            line_1.append(get_point)
        elif 5 < i < 9 :
            get_point = float(input("Enter x,y,z Co-ordinates of 2nd Position Vecotr: "))
            line_2.append(get_point)
        elif 8 < i < 12 :
            get_point = float(input("Enter x,y,z Co-ordinates of 2nd Displacement Vecotr: "))
            line_2.append(get_point)
    if(check_line(line_1,line_2)):
        print("Lines are intersecting!")        
    else:
        print("Lines are parallel!")

def check_line(line_1,line_2):
    
    # Forming Equations
    
    equation_1 = [line_1[0]-line_2[0],line_2[3],-line_1[3]]
    equation_2 = [line_1[1]-line_2[1],line_2[4],-line_1[4]]
    equation_3 = [line_1[2]-line_2[2],line_2[5],-line_1[5]]
    
    
    # Using matrix approach
    # Checking Determinent of the matrices
    
    determinent = equation_2[2]*equation_1[1]-equation_2[1]*equation_1[2]
    
    if(determinent == 0):
        return False
    
    unknows = matrix_solver(equation_1,equation_2,determinent)
    # print(unknows)
    # if(0 <= unknows[0] <= 1):
    #     pass
    # elif(0 <= unknows[1] <= 1):
    #     pass
    # else:
    #     return False
    
    # # Skew Case
    # if(int(equation_3[0]) == int(equation_3[1]*unknows[0] + equation_3[2]*unknows[1])):
    #     pass
    # else:
    #     return False
    
    #Checking Intersection 
    intersection_1 = [(line_1[0] + unknows[1]*line_1[3]),line_1[1] + unknows[1]*line_1[4],line_1[2] + unknows[1]*line_1[5]]
    intersection_2 = [(line_2[0] + unknows[0]*line_2[3]),line_2[1] + unknows[0]*line_2[4],line_2[2] + unknows[0]*line_2[5]]
    for i in range(0,3):
        if(intersection_1[i] != intersection_2[i]):
            return False
    return True


def matrix_solver(equation_1,equation_2,determinent):
    equation_1[1],equation_2[2] = equation_2[2],equation_1[1]
    equation_1[2] = -equation_1[2] 
    equation_2[1] = -equation_2[1]
    unknown_1 = (equation_1[1]*equation_1[0] + equation_1[2]*equation_2[0])/determinent
    unknown_2 = (equation_2[1]*equation_1[0] + equation_2[2]*equation_2[0])/determinent
    return unknown_1,unknown_2   
main()
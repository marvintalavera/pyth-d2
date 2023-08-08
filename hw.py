def max_num(x,y,z):
    return max([x,y,z])

print(max_num(2,100,40))

def multi_list(num_list):
    if len(num_list)==0:
        return 0
    else:
        total=1
        for i in num_list:
            total=total*(i)
        print(total)

multi_list([2,6,3])

def rev_string(word):
    return word[::-1]

print(rev_string('hello'))

def num_within(x,y,z):
    return x in range(y,z+1)

print(num_within(2,1,6))
print(num_within(4,5,6))
print(num_within(4,4,6))

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(8)
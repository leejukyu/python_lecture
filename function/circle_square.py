def circle_square(radius):
    area = 2*radius*3.14
    circum = radius*radius*3.14
    # print("둘레 : ",area, "면적 : ",circum)
    return area, circum
radius = float(input("반지름을 입력하세요"))
print(circle_square(radius))
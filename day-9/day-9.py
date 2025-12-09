points = []

with open("day-9.txt", "r") as file:
    points = [[int(c) for c in line.strip().split(",")] for line in file]


# Part 1


largest_area = 0

areas = [] # store areas for part 2


def get_area(point1, point2): # gets the area
    return (abs(point1[0]-point2[0])+1) * (abs(point1[1] - point2[1])+1)

for i, point1 in enumerate(points[:-1]):
    for j, point2 in enumerate(points[i+1:], start=i+1):
        
        a = get_area(point1, point2)
        areas.append((i, j, a))
        if a > largest_area:
            largest_area = a

print("Largest Area (Part 1):", largest_area)


# Part 2


def check_horizontal(p1, p2): # checks if line is horizontal or vertical
    if p1 == p2:
        raise Exception("Same points!")
    if p1[0] != p2[0] and p1[1] != p2[1]:
        raise Exception("Not linear")
    if p1[0] != p2[0]: # x coord is not the same
        return True
    return False


def normalize_rect(p1, p2): # returns (x1, y1, x2, y2) of rect
    x1, y1 = p1
    x2, y2 = p2
    return (min(x1, x2), min(y1, y2),
            max(x1, x2), max(y1, y2))

def inside_polygon(polygon, line): # checks if a line starts within the polygon (check if the point is in the polygon)
    is_horizontal = check_horizontal(*line)
    unchanging_coord = 0
    if is_horizontal:
        unchanging_coord = line[0][1]
    else:
        unchanging_coord = line[0][0]
    inside = False
    for i in range(len(polygon)-1):
        p1 = polygon[i]
        p2 = polygon[i+1]
        x1, y1, x2, y2 = normalize_rect(p1, p2)
        if is_horizontal != check_horizontal((x1, y1), (x2, y2)): # if they are perpendicular
            if is_horizontal:
                if unchanging_coord >= y1 and unchanging_coord <= y2 and line[0][0] <= x1 and line[1][0] >= x1:
                    inside = not inside
                    
            else:
                if unchanging_coord >= x1 and unchanging_coord <= x2 and line[0][1] <= y1 and line[1][1] >= y1:
                    inside = not inside

    return inside

def within_rect(point, rect):
    x, y = point
    x1, y1, x2, y2 = rect
    return x > x1 and x < x2 and y > y1 and y < y2





def crosses_edge(polygon, line, rect): # excluding vertices of the line, including vertices of the polygon (if one is within the line)!!!
    is_horizontal = check_horizontal(*line)
    unchanging_coord = 0
    if is_horizontal:
        unchanging_coord = line[0][1]
    else:
        unchanging_coord = line[0][0]

    for i in range(len(polygon)-1):
        p1 = polygon[i]
        p2 = polygon[i+1]
        x1, y1, x2, y2 = normalize_rect(p1, p2)
        if is_horizontal != check_horizontal((x1, y1), (x2, y2)): # if they are perpendicular
            if is_horizontal: # horizontal line
                if unchanging_coord > y1 and unchanging_coord < y2 and line[0][0] < x1 and line[1][0] > x1:
                    return True
                elif unchanging_coord >= y1 and unchanging_coord <= y2 and line[0][0] <= x1 and line[1][0] >= x1 and (within_rect((x1, y1),  rect) or within_rect((x2, y2), rect)):
                    return True
                    
            else: # veritcal line
                if unchanging_coord > x1 and unchanging_coord < x2 and line[0][1] < y1 and line[1][1] > y1:
                    return True
                elif unchanging_coord >= x1 and unchanging_coord <= x2 and line[0][1] <= y1 and line[1][1] >= y1 and (within_rect((x1, y1), rect) or within_rect((x2, y2), rect)):
                    return True

    return False

def rectangle_fully_inside_polygon(xmin, ymin, xmax, ymax, polygon):

    # is fully inside if an odd number of edges to the right of a single point (inclusive of vertices),
    # and no polygon edges perpendicularly cross any edge of the rectangle (excusive of vertices)

    if not inside_polygon(polygon, ((xmax, ymax), (100000, ymax))): # check if a single of the rectangle is in the polygon
        return False

    # define the lines that make up the rect
    lines = [((xmin, ymin), (xmin, ymax)), ((xmin, ymin), (xmax, ymin)), ((xmax, ymin), (xmax, ymax)), ((xmin, ymax), (xmax, ymax))]
    for line in lines:
        if crosses_edge(polygon, line, (xmin, ymin, xmax, ymax)): # if a perimeter line of the rect crosses an edge of the polygon, it goes out of bounds of the polygon (therefore invalid)
            return False
    
    return True




points = points + [points[0]] # close polygon

largest_area = 0


areas.sort(key = lambda x:x[2], reverse=True) # sort rects by area descending

for area in areas:
    i, j, a = area
    
    point1 = points[i]
    point2 = points[j]

    r = normalize_rect(point1, point2)

    if rectangle_fully_inside_polygon(*r, points):
        print("Valid Area (Part 2):", a, ", debug:", area, point1, point2)
        break

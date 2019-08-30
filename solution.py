

def main():
    origin_inside = 0
    origin_outside = 0
    for coords in read_txt_file("triangles.txt"):
        ## calculate all the trinagle areas
        tri_area = area_of_triangle(coords)
        origin = [0,0]
        sub_tri1 = area_of_triangle(origin + coords[2:])
        sub_tri2 = area_of_triangle(coords[:2] + origin + coords[4:])
        sub_tri3 = area_of_triangle(coords[:4] + origin)
        
        boolean = is_inside_triangle(tri_area, sub_tri1,
                                     sub_tri2, sub_tri3)
        if boolean:
            origin_inside +=1
            continue
        origin_outside += 1
    print("{} triangles contain the origin".format(origin_inside))
    print("{} triangles do not contain the origin".format(origin_outside))
    return (origin_inside, origin_outside)

## generator yields triangles.txt coordinates
def read_txt_file(file_name):
    with open(file_name) as f:
        for line in f:
            coords = [int(i) for i in line.split(",")]
            yield coords

## calulates area or triangles
def area_of_triangle(coords_list):
    x1, y1, x2, y2, x3, y3 = coords_list
    area = abs(.5 * (x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)))
    return area

## adds area of origin sub triangles
## to see if they are equal to containing triangle
def is_inside_triangle(triangle, sub_tri_1, sub_tri2, sub_tri3):
    return triangle == sub_tri_1 + sub_tri2 + sub_tri3


if __name__ == "__main__":
    main()

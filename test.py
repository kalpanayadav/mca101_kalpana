https://goo.gl/ix9qBKimport sys
sys.path.append('/home/administrator/Desktop/abhi')
import areareac
import areatri
def main():
    
    """
    objective  : to find the area of triangle or area of rectangle
                by choice taken by the user
    user input :
                for Reactangle
                length: length of rectanlgle
                breadth: breadth of the rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    """
    areatype = input('which area you want to compute(triangle/reactangle):   ') 
  if areatype == 'reactangle':
    print("\t=======================")
    print("compute the area of reactangle")
    print("\t=======================")
    length = int(input("enter length of reactangle:   "))
    breadth= int(input("enter breadth of reactangle:   "))
    print('\n the area of reactangle is:' area.areareac(length,breadth))
  elif areatype == 'triangle':
    print("\t=======================")
    print("compute the area of triangle")
    print("\t=======================")
    hieght = int(input("enter hieght of triangle:   "))
    base= int(input("enter base of triangle:   "))
    print('\n the area of reactangle is:' area.areatri(hieght,base))
if __name__== '__ main __':
    main()


import math

def calc_distance(point1, point2):
    # Extraire les coordonnées des points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Calculer la distance entre les points en utilisant la formule de la distance euclidienne en 3D
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

# Points
point1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
point2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

# Calculer et afficher les distances entre les points correspondants
for p1, p2 in zip(point1, point2):
    distance = calc_distance(p1, p2)
    print("Distance entre", p1, "et", p2, ":", distance)

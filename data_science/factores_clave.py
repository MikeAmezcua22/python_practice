"""
Ciencia de Datos desde Cero - Análisis de Redes de Amistad
"""
from collections import Counter


# ============================================================================
# DATOS
# ============================================================================

users = [
  { "id": 0, "name": "Hero" },
  { "id": 1, "name": "Dunn" },
  { "id": 2, "name": "Sue" },
  { "id": 3, "name": "Chi" },
  { "id": 4, "name": "Thor" },
  { "id": 5, "name": "Clive" },
  { "id": 6, "name": "Hicks" },
  { "id": 7, "name": "Devin" },
  { "id": 8, "name": "Kate" },
  { "id": 9, "name": "Klein" }
]

friendship_pairs = [
  (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
  (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]


# ============================================================================
# CLASES
# ============================================================================

class Solution:
  def factor_clave(self, users, friendship_pairs):
    """Construye un diccionario de amistades bidireccional"""
    friendship = {user["id"]: [] for user in users}

    for i, j in friendship_pairs:
      friendship[i].append(j)
      friendship[j].append(i)

    return friendship 


# ============================================================================
# FUNCIONES
# ============================================================================

def number_of_friends(user, friendship):
  """¿Cuántos amigos tiene un usuario?"""
  user_id = user["id"]
  friends_ids = friendship[user_id]
  return len(friends_ids)


def foaf_ids_bad(user, friendship):
  """Obtiene todos los amigos de amigos (con duplicados)"""
  return [
    foaf_id
    for friend_id in friendship[user["id"]]
    for foaf_id in friendship[friend_id]
  ]


def friendship_of_friends(user, friendship):
  """Obtiene amigos de amigos únicos (excluyendo al usuario y amigos directos)"""
  user_id = user["id"]
  return Counter(
    foaf_id
    for friend_id in friendship[user_id]
    for foaf_id in friendship[friend_id]
    if foaf_id != user_id and foaf_id not in friendship[user_id]
  )


# ============================================================================
# PRUEBAS Y ANÁLISIS
# ============================================================================

if __name__ == "__main__":
  # Construir red de amistades
  solution = Solution()
  friendship = solution.factor_clave(users, friendship_pairs)
  
  # Análisis de conexiones totales y promedio
  total_connections = sum(
    number_of_friends(user, friendship)
    for user in users
  )
  
  num_user = len(users)
  avg_connections = total_connections / num_user
  
  # Ranking de usuarios por número de amigos
  num_friends_by_id = [
    (user["id"], number_of_friends(user, friendship)) 
    for user in users
  ]
  num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], 
                         reverse=True)
  
  # Amigos de amigos
  foaf_id = foaf_ids_bad(users[0], friendship)
  print("Amigos de amigos del usuario 0:", foaf_id)
  
  # Mejores recomendaciones de amistad
  print("Mejores candidatos para usuario 3:", friendship_of_friends(users[3], friendship))

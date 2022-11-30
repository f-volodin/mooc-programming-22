def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dic = { }
    dic["name"] = name
    dic["director"] = director
    dic["year"] = year
    dic["runtime"] = runtime
    database.append(dic)
def find_movies(database: list, search_term: str):
    lister = [ ] 
    for i in database:
        u = i["name"]
        if search_term.lower() in u.lower():
            lister.append(i)
    return(lister)
#[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
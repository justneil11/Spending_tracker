from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, activated_tag) VALUES (%s, %s) RETURNING id"
    values = [tag.name, tag.activated]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['activated_tag'], row['id'])
        tags.append(tag)
    return tags

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def select(id):
    tag = None 
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        tag = Tag(result["name"], result["activated_tag"], result["id"])
    return tag

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name, activated_tag) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.activated, tag.id]
    run_sql(sql, values)
from google.cloud import datastore


def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])


# [START from_datastore]
def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id
    return entity
# [END from_datastore]


# [START list]
def list(entity, sort_field, limit=10, cursor=None):
    ds = get_client()

    query = ds.query(kind=entity, order=[sort_field])
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(list(map(from_datastore, page)))
    next_cursor = (
        query_iterator.next_page_token.decode('utf-8')
        if query_iterator.next_page_token else None)

    return entities, next_cursor
# [END list]


def read(entity, id):
    ds = get_client()
    key = ds.key(entity, int(id))
    results = ds.get(key)
    return from_datastore(results)


# [START update]
def update(update_entity, data, exclude, id=None):
    ds = get_client()
    if id:
        key = ds.key(update_entity, int(id))
    else:
        key = ds.key(update_entity)

    entity = datastore.Entity(
        key=key,
        exclude_from_indexes=[exclude])

    entity.update(data)
    ds.put(entity)
    return from_datastore(entity)


create = update
# [END update]


def delete(delete_entity, id):
    ds = get_client()
    key = ds.key(delete_entity, int(id))
    ds.delete(key)





def _insert_user(user_id, message_id=None, lang=None):
    columns = '(id, message_id'
    if not message_id:
        message_id = 'null'
    values = f'({user_id}, {message_id}'
    if lang:
        columns += ', lang)'
        values += f", '{lang}')"
    else:
        columns += ')'
        values += ')'
    return f'''
    insert into users {columns}
    values {values}
    '''

# either one of
def _update_user(message_id=None, lang=None):
    if not message_id:
        message_id = 'null'
    values = f'message_id = {message_id}'
    if lang:
        values += f", lang = '{lang}'"
    return f'''
    update set {values}
    '''

def update_user(user_id, message_id=None, lang=None):
    return f'''
    {_insert_user(user_id, message_id, lang)}
    on conflict on constraint users_pkey do
    {_update_user(message_id, lang)}
    '''

def get_user(user_id):
    return f'select * from users where id = {user_id}'

# --------------------------------------------------------------------------

def districts():
    return 'select * from districts'

def routes(route_type):
    return f'select * from routes where type={route_type}'

def get_user_filters(user_id):
    return f'''
    select
        uf.id, uf.name
    from user_filters uf
    where user_id = {user_id};
    '''

def get_filter(user_id,
               filter_id):
    return f'''
    select
        uf.id, uf.name, ff.type, ff.city,
        ff.district, ff.sex, ff.pets,
        ff.smoke, ff.owner, ff.rooms,
        ff.min_price, ff.max_price,
        gf.route_id, gf.radius
    from user_filters uf
        join f_filters ff
            on uf.f_filter_id = ff.id
        left join g_filters gf
            on uf.g_filter_id = gf.id
    where
          user_id = {user_id} and uf.id = {filter_id};
    '''

def get_property_item(filter_id, property_id):
    return f'''
    with filter as (select *
        from user_filters where id = {filter_id}
    )
    select (select user_id from filter),
           (select name from filter),
           p.*, d.* from property p
        join description d on p.description_id = d.id
    where p.id = {property_id};
    '''


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
def get_users_count():
    return f'select count(*) from users;'

def cities():
    return 'select * from cities'

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
    if property_id:
        return f'''
        with filter as (select *
            from user_filters where id = {filter_id}
        )
        select (select user_id from filter),
               (select name from filter),
               p.*, d.* from property p
            join description d on p.description_id = d.id
        where p.id = {property_id}
        '''
    else:
        return f'select user_id, name from user_filters where id = {filter_id}'

def insert_user_ad(property):
    return f'''
    insert into user_ads
        (title, description, url, photo, contact_name, contact_phone, amenities, demands, type, city, district, sex, pets, smoke, owner, rooms, price, latitude, longitude)
    values
        {property.get_tuple()}
    '''

def get_last_user_ad():
    return '''
    select * from user_ads
    order by id desc
    limit 1
    '''

def delete_user_ad(ad_id):
    return f'delete from user_ads where id = {ad_id}'

def insert_ad_in_db(ad_id, timestamp):
    return f'''
with ad as (
    select * from user_ads
    where id = {ad_id}
),
ins_d as (
    insert into description (
        title, description, url, photo, contact_name, contact_phone, amenities, demands
    )
    select title, description, url, photo, contact_name, contact_phone, amenities, demands
    from ad
    returning id as d_id
),
ins_p as (
    insert into property (
        type, city, district, sex, pets, smoke, owner, rooms, price, latitude, longitude, description_id
    )
    select type, city, district, sex, pets, smoke, owner, rooms, price, latitude, longitude, d_id
    from ad, ins_d
    returning id as p_id
)
insert into items (
    site, item_id, added, property_id
)
select 0, 0, {timestamp}, p_id
from ins_p
returning id
'''

def get_city_and_district_by_geo(lat, lon, radius=0.5):
    return f'''
select p.district, d.city_id, count(p.id)
from property p
join districts d on p.district = d.id
where (point(longitude,latitude) <@> point({lon},{lat}) < {radius}*0.621371)
group by p.district, d.city_id
order by count desc
limit 1'''

def get_users(lang=None):
    q = 'select id from users'
    if lang:
        q += f" where lang = '{lang}'"
    return q


def get_a_user_ads_count(date):
    return f"select count(*) from user_ads where published>='{date}'"


def get_filter_count():
    return 'select count(*) from user_filters'


def get_active_users(date):
    return f"select count(*) from users where last_activity>='{date}'"


def set_active_day(date, user_id):
    return f"update users set last_activity='{date}' where id='{user_id}'"


def insert_statistic_record(timestamp: int, amount: int, type_: int) -> str:
    return f'''
insert into users_statistics (
    timestamp, amount, type
)
values ({timestamp}, {amount}, {type_})'''


def q_insert_post(data, lang):

    return f"insert into posts (post_text, id, lang) values('{data}', 1, '{lang}')"

def q_get_post():
    return "select * from posts"

def q_delete_post():
    return "delete from posts"

def q_get_file_id_ads():
    return '''
        select photo from user_ads
        order by id desc
        limit 1
        '''


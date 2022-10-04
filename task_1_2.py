from http.cookies import SimpleCookie
def parse_cookie(rawdata):
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('yummy_cookie=choco;') == {'yummy_cookie': 'choco'}
    assert parse_cookie('id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;') == {'id': 'a3fWa'}
    assert parse_cookie('id=a3fWa; Max-Age=2592000') == {'id': 'a3fWa'}
    assert parse_cookie('qwerty=219ffwef9w0f; Domain=somecompany.co.uk') == {'qwerty': '219ffwef9w0f'}
    assert parse_cookie('flavor=choco; SameSite=None; Secure') == {'flavor': 'choco'}
    assert parse_cookie('PHPSESSID=298zf09hf012fh2; csrftoken=u32t4o3tb3gg43; _gat=1') == {'PHPSESSID': '298zf09hf012fh2', 'csrftoken': 'u32t4o3tb3gg43', '_gat': '1'}
    assert parse_cookie('ckpf_ppid_safari=a271b829cc244d5c94faae14f73f34df; ckpf_ppid_safari=21ebcecf7ab7400483c654469c6b24fb; ecos.dt=1600401456420; ecos.dt=1600401456208;') == {'ckpf_ppid_safari': '21ebcecf7ab7400483c654469c6b24fb', 'ecos.dt': '1600401456208'}
    assert parse_cookie('ckns_orb_fig_cache={%22ad%22};') == {'ckns_orb_fig_cache': '{%22ad%22}'}
    assert parse_cookie('id=3db4adj3d; Path=/about/') == {'id': '3db4adj3d'}
    assert parse_cookie('id=3db4adj3d; HttpOnly') == {'id': '3db4adj3d'}





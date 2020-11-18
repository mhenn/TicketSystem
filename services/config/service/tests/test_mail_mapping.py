import json
# /mail-mapping/
#get

url = '/config/mail-mapping/'

def test_mail_insert_one(app, client, insert_mail_one):
    res = client.get(url)
    inserted_mail = insert_mail_one[0]
    ret_map = json.loads(res.data)['mapping'][0]
    assert res.status_code == 200
    for k in inserted_mail:
        assert inserted_mail[k] == ret_map[k]


def test_mail_insert_multiple(app, client, insert_mail_multiple):
    res = client.get(url)
    inserted_mail = insert_mail_multiple[0]
    ret_map = json.loads(res.data)['mapping']
    assert res.status_code == 200
    for i in range(len(inserted_mail)):
        for k in inserted_mail[i]:
            assert inserted_mail[i][k] == ret_map[i][k]
   
def test_mail_insert_none(app, client, insert_nothing):
    res = client.get(url)
    res_map = json.loads(res.data)['mapping']
    assert res.status_code == 200
    assert len(res_map) == 0

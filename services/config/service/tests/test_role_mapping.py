import json
# /mapping-mapping/
#GET

url = '/config/role-mapping/'

def test_mappings_get_with_insert_one(app, client, insert_mapping_one):
    res = client.get(url)
    print(res.data)
    inserted_mapping = insert_mapping_one[0]
    ret_map = json.loads(res.data)['mapping'][0]
    assert res.status_code == 200
    for k in inserted_mapping:
        assert inserted_mapping[k] == ret_map[k]


def test_mappings_get_with_insert_multiple(app, client, insert_mapping_multiple):
    res = client.get(url)
    inserted_mapping = insert_mapping_multiple[0]
    ret_map = json.loads(res.data)['mapping']
    assert res.status_code == 200
    for i in range(len(inserted_mapping)):
        for k in inserted_mapping[i]:
            assert inserted_mapping[i][k] == ret_map[i][k]
   
def test_mappings_iget_with_insert_none(app, client, insert_nothing):
    res = client.get(url)
    res_map = json.loads(res.data)['mapping']
    assert res.status_code == 200
    assert len(res_map) == 0

#POST

def test_mappings_post(app,client, insert_nothing):
   
    res = client.post(url, data='{"name": "test1", "mappingId": "1234", "type": "mapping", "actions": ["created"]}')
    d = insert_nothing
    count = d.mapping.count_documents({})
    assert res.status_code == 200
    assert count == 1


def test_mappings_post_wrong(app,client, insert_nothing):
    res = client.post(url, data='{"caption":"test"}')
    d = insert_nothing
    count = d.queue.count_documents({})
    assert res.status_code == 400
    assert count == 0

def test_mappings_post_empty(app, client, insert_nothing):
    res = client.post(url, data='')
    d = insert_nothing
    count = d.queue.count_documents({})
    assert res.status_code == 400
    assert count == 0


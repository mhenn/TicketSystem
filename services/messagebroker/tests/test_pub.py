import json
# /pubs/
#get

url = '/pubsub/'

def test_pubs_get_one_pub(app, client, insert_pub):
    res = client.get(url)
    pubs = json.loads(res.data)['publishers']
    key = 'publisher'
    assert res.status_code == 200
    assert len(pubs) == 1
    assert pubs[0][key] == insert_pub[0][key]

def test_pubs_get_many_pubs(app, client, insert_multiple_pubs):
    res = client.get(url)
    pubs = json.loads(res.data)['publishers']
    assert res.status_code == 200
    assert len(pubs) == len(insert_multiple_pubs[0])

def test_pubs_get_no_pubs(app, client, insert_nothing):
    res = client.get(url)
    print(res.data)
    pubs = json.loads(res.data)['publishers']
    assert res.status_code == 200
    assert len(pubs) == 0
    

##POST

def test_pubs_post(app,client, insert_nothing):
   
    res = client.post(url, data='{"publisher":"test"}')
    d = insert_nothing
    count = d.pub.count_documents({})
    assert res.status_code == 200
    assert count == 1

def test_pubs_post_to_of_the_same(app,client, insert_nothing):
   
    res = client.post(url, data='{"publisher":"test"}')
    res = client.post(url, data='{"publisher":"test"}')
    d = insert_nothing
    count = d.pub.count_documents({})
    assert res.status_code == 409
    assert count == 1


def test_pubs_post_wrong(app,client, insert_nothing):
    res = client.post(url, data='{"caption":"test"}')
    d = insert_nothing
    count = d.pub.count_documents({})
    assert res.status_code == 400
    assert count == 0

def test_pubs_post_empty(app, client, insert_nothing):
    res = client.post(url, data='')
    d = insert_nothing
    count = d.pub.count_documents({})
    assert res.status_code == 400
    assert count == 0




def assert_list(orig, response):
    for i in range(len(orig)):
        for k in orig[i]:
            assert orig[i][k] == response[i][k]

def assert_map(orig, response):
    for k in orig:
        assert response[k] == orig[k]



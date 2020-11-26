
def assert_list(orig, response):
    for i in range(len(orig)):
        for k in orig[i]:
            assert orig[i][k] == response[i][k]




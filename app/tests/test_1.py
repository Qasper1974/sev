from django import urls

import pytest

# test if a random website is able to get a 200 success http response when 
# requesting access to the home and 'add a word' html page

@pytest.mark.parametrize('param', [
    ('home'),
    ('create_word'),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200
    
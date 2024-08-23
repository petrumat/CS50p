# Import necessary packages and modules
import pytest
from watch import parse


# Test different (expected) str combinations
# Ideal str format: <iframe#src="https://www.youtube.com/embed/#"#></iframe>
# where above # is any ASCII, whitespace or [:/.;-] char
def test_str():
    assert parse('') == None    # Test empty argument
    assert parse('cat') == None # Test a random str
    assert parse('<iframe src="cat"></iframe>') == None # Test random str close to accepted format

    # Test correct str with 'http' protocol with and without 'www.'
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

    # Test correct str with 'https' protocol with and without 'www.'
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

    # Test correct str with many HTML attributes
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

    # Test incorrect str without youtube address
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None


# Test invalid argument type
def test_non_str():
    with pytest.raises(TypeError):
        parse(123)   # Test argument type 'int'
        parse(123.567)   # Test argument type 'float'

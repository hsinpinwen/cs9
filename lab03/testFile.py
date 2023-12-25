from lab03 import multiply
from lab03 import collectMultiples
from lab03 import countVowels
from lab03 import reverseVowels
from lab03 import removeSubString

def test_multiply():
    assert multiply(-5, -2) == 10
    assert multiply(-5, 3) == -15
    assert multiply(5, -4) == -20
    assert multiply(0, 5) == 0
    assert multiply(5, 6) == 30

def test_collectMultiples():
    assert collectMultiples([1,3,5,7,9], 3) == [3,9]
    assert collectMultiples([2,4,6,8,9], 2) == [2,4,6,8]
    assert collectMultiples([], 3) == []
    assert collectMultiples([3,5,9], 2) == []

def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("HELLO WORLD") == 3
    assert countVowels("") == 0

def test_reverseVowels():
    assert reverseVowels("Eunoia") == "aiouE"
    assert reverseVowels("spike defused") == "eueei"
    assert reverseVowels("CANDY CRUSH") == "UA"
    assert reverseVowels("") == ""

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("potatotomato", "ato") == "pottom"
    assert removeSubString("", "") == ""

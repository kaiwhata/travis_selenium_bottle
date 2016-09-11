#pytest will run all files in the current directory and its subdirectories of the form test_*.py or *_test.py.
#More generally, it follows standard test discovery rules.

# content of test_sample.py
def func(x):
  return x + 1

def test_answer():
  assert func(3) == 5

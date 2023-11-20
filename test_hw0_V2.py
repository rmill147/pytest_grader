import os
import pytest
from importlib import import_module

@pytest.fixture(scope="module", autouse=True)
def v2_setup():
    # Runs before tests:
    print("\n set-up....")
    print("\n Files in submissions:")
    for filename in os.listdir('submissions'):
        f = os.path.join('submissions', filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            # module_name = os.path.splitext(filename)[0]
            # selected_student = "submissions.%s" % module_name
            # student = import_module(selected_student)
            # return student

    yield
    # Runs after tests:
    print("tear-down...")


def create_test_hw_0(student_id,file_name):

    class test_hw0:
        def setup(self):
            print(f"Student ID: {student_id}")
            print(f"File name: {file_name}")

        def test_output0(v2_setup):
            student = import_module(file_name)
            expected = [('Princess Bride, The (1987)', 4.232394366197183, 142),
                        ('Pulp Fiction (1994)', 4.197068403908795, 307),
                        ("Amelie (Fabuleux destin d'Amélie Poulain, Le) (2001)", 4.183333333333334, 120),
                        ('Forrest Gump (1994)', 4.164133738601824, 329),
                        ('Monty Python and the Holy Grail (1975)', 4.161764705882353, 136),
                        ('Fargo (1996)', 4.116022099447513, 181), ('Trainspotting (1996)', 4.03921568627451, 102),
                        ('Back to the Future (1985)', 4.038011695906433, 171),
                        ('Finding Nemo (2003)', 3.9609929078014185, 141), ('Groundhog Day (1993)', 3.944055944055944, 143)]
            # student = picked_student()
            actual = student.part0
            assert actual == expected

        def test_output1(v2_setup):
            student = import_module(file_name)
            expected = [('Usual Suspects, The (1995)', 4.237745098039215, 204)]
            # student = picked_student()
            actual = student.part1
            assert actual == expected

        def test_output2(v2_setup):
            student = import_module(file_name)
            expected = [('Waterworld (1995)', 2.9130434782608696, 115)]
            # student = picked_student()
            actual = student.part2
            assert actual == expected

        def test_output3(v2_setup):
            student = import_module(file_name)
            expected = [('Star Wars: Episode IV - A New Hope (1977)', 5.0, 104),
                        ('Star Wars: Episode V - The Empire Strikes Back (1980)', 4.8076923076923075, 78),
                        ('Star Wars: Episode VI - Return of the Jedi (1983)', 4.730263157894737, 76),
                        ('Godfather, The (1972)', 4.673469387755102, 49),
                        ('Lawrence of Arabia (1962)', 4.666666666666667, 15), ('To Kill a Mockingbird (1962)', 4.65, 10),
                        ('Shawshank Redemption, The (1994)', 4.622641509433962, 53), (
                        'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)', 4.590909090909091,
                        22), ('In Bruges (2008)', 4.541666666666667, 12), (
                        'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', 4.536764705882353,
                        68)]
            # student = picked_student()
            actual = student.part3
            assert actual == expected

    return test_hw0


grades = {}
i = 0
for filename in os.listdir('submissions'):
    print("filename:")
    print(filename)
    directory = 'submissions'
    f = os.path.join('submissions', filename)
    if os.path.isfile(f):
        module_name = os.path.splitext(filename)[0]
        selected_student = "%s.%s" % (directory,module_name)
        classIteration = "Test" + str(i)
        print(classIteration)
        globals()[classIteration] = create_test_hw_0(i,selected_student)
        i = i+1

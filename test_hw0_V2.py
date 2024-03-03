import os
import glob
import pytest
from importlib import import_module


def create_test_class(module_id,module_name):

    class TestClass:
        module_id = module_id
        module_name = module_name
        module = import_module(module_name)
        passed = 0
        tested = 0

        def test_0(self):
            expected = [('Princess Bride, The (1987)', 4.232394366197183, 142),
                        ('Pulp Fiction (1994)', 4.197068403908795, 307),
                        ("Amelie (Fabuleux destin d'Amélie Poulain, Le) (2001)", 4.183333333333334, 120),
                        ('Forrest Gump (1994)', 4.164133738601824, 329),
                        ('Monty Python and the Holy Grail (1975)', 4.161764705882353, 136),
                        ('Fargo (1996)', 4.116022099447513, 181), ('Trainspotting (1996)', 4.03921568627451, 102),
                        ('Back to the Future (1985)', 4.038011695906433, 171),
                        ('Finding Nemo (2003)', 3.9609929078014185, 141), ('Groundhog Day (1993)', 3.944055944055944, 143)]
            actual = self.module.part0
            assert actual == expected

        def test_1(self):
            expected = [('Usual Suspects, The (1995)', 4.237745098039215, 204)]
            actual = self.module.part1
            assert actual == expected

        def test_2(self):
            expected = [('Waterworld (1995)', 2.9130434782608696, 115)]
            actual = self.module.part2
            assert actual == expected

        def test_3(self):
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
            actual = self.module.part3
            assert actual == expected

    return TestClass

submission_dir = 'submissions'
filenames = glob.glob("%s/*.py" % submission_dir)
for module_id,filename in enumerate(filenames):
    basename = os.path.basename(filename)
    basename = os.path.splitext(basename)[0]
    module_name = "%s.%s" % (submission_dir,basename)
    class_name = "Test%d" % module_id
    test_class = create_test_class(module_id,module_name)
    test_class.basename = basename
    globals()[class_name] = test_class

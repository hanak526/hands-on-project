import sys, unittest
from md import calcenergy

class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        from ase import units
        from ase.lattice.cubic import FaceCenteredCubic
        from ase import units    
        atoms = FaceCenteredCubic(
        directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        symbol='Cu',
        size=(2, 1, 1),
        pbc=True,
    )
        from ase.calculators.emt import EMT
        atoms.calc = EMT()
        value = [-0.045452090868632666, 0.0, 0.0, -0.045452090868632666]
        self.assertEqual(value, calcenergy(atoms))
if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)

    sys.exit(not result.wasSuccessful())


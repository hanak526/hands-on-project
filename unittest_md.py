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
        size=(10, 10, 10),
        pbc=True,
    )
        from ase.calculators.emt import EMT
        atoms.calc = EMT()
        value = atoms.get_potential_energy()/len(atoms)
        real_value = calcenergy(atoms)
        message = "It works!"
        self.assertTrue(value==real_value[0],message)
if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
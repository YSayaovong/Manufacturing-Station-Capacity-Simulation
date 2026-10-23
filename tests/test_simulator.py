import unittest
import numpy as np
from station_capacity_simulator import StationConfig, MultiMachineLineSimulator

class SimulatorTests(unittest.TestCase):
    def config(self):return StationConfig('Example',60,100,1)
    def test_invalid_cycle_rejected(self):
        with self.assertRaises(ValueError):StationConfig('Bad',0,100,1)
    def test_invalid_horizon_rejected(self):
        with self.assertRaises(ValueError):MultiMachineLineSimulator([self.config()],0)
    def test_zero_runs_rejected(self):
        with self.assertRaises(ValueError):MultiMachineLineSimulator([self.config()],1).run_monte_carlo(0)
    def test_seed_is_reproducible_and_capacity_bounded(self):
        sim=MultiMachineLineSimulator([self.config()],1)
        a=sim.run_monte_carlo(50,123)['line_throughputs']
        b=sim.run_monte_carlo(50,123)['line_throughputs']
        np.testing.assert_array_equal(a,b)
        self.assertTrue(np.all((a>=0)&(a<=60)))

if __name__=='__main__':unittest.main()

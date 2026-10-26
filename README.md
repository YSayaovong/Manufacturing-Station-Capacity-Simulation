# Manufacturing Station Capacity Simulation
## Scope
Independent Python Monte Carlo demonstration using assumed cycle times, mean time between failures (MTBF), mean time to repair (MTTR) and parallel machine counts.

## Implementation
`station_capacity_simulator.py` defines station configurations and simulates alternating exponential uptime/repair periods for each machine over an eight-hour example horizon. It totals completed units per station, takes the minimum station total as a line-capacity approximation and counts which stations share that minimum across 500 seeded runs.

## Run
Install numpy and matplotlib, then:
```bash
python station_capacity_simulator.py
```
The example uses seed 123 and writes capacity, bottleneck and downtime PNGs into `assets/` relative to the script. Historical PNG filenames are retained.

## Interpretation and limitations
Stations are simulated independently with no starvation or blocking. Taking the minimum of their total capacities does not model chronological movement, buffers, transfer times or actual serial-line throughput. Incomplete cycle time is discarded at each failure interval. Ties count for every tied station, so bottleneck percentages can sum above 100%.

Parameters are illustrative rather than calibrated to a documented factory dataset. Positive finite configuration values, unique station names and positive integer run counts are validated. Four tests cover invalid inputs, seeded repeatability and capacity bounds. Benchmark comparisons and sensitivity experiments remain development work. This is a capacity-model learning project, not production-grade scheduling or reliability software.

## Reproduce validation
```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python station_capacity_simulator.py
```
The 500-run seed-123 example gives mean minimum-station capacity of about 356.4 units per eight-hour horizon. This is an assumption-based supporting project, not a result from a factory dataset or a resume claim of implemented production optimization.

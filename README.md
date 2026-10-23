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
The example uses seed 123 and writes throughput, bottleneck and downtime PNGs into the working directory. Existing screenshots are in `assets/`.

## Interpretation and limitations
Stations are simulated independently with no starvation or blocking. Taking the minimum of their total capacities does not model chronological movement, buffers, transfer times or actual serial-line throughput. Incomplete cycle time is discarded at each failure interval. Ties count for every tied station, so bottleneck percentages can sum above 100%.

Parameters are illustrative rather than calibrated to a documented factory dataset. Input validation, automated tests, benchmark comparisons and sensitivity experiments remain development work. This is a capacity-model learning project, not production-grade scheduling or reliability software.

## File naming and authorship
The script is named `station_capacity_simulator.py` to describe its implementation. Historical PNG filenames are retained for compatibility. Console and chart titles now label the minimum-station result as a capacity approximation. Naming/documentation changes were developed with AI assistance; they do not add a serial-flow model.

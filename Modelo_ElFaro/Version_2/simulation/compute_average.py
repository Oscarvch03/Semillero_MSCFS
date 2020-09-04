import sys
sys.path.insert(0, "../")

import Functions.average as av



filename = "puntajes_Random(p=0.8)"
av.average_score(filename, 3, 300)
av.plot_av()

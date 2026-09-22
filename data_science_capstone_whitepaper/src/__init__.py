import os
# Configure OpenMP thread count to prevent KMeans memory leak UserWarning on Windows with MKL
os.environ["OMP_NUM_THREADS"] = "1"

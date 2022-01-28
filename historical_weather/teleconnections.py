import typing

__all__ = ["arctic_oscillation", "north_american_oscillation", "pacific_decadal_oscillation"]

_AO = """
1950 -0.060  0.627 -0.008  0.555  0.072  0.539 -0.802 -0.851  0.358 -0.379 -0.515 -1.928
1951 -0.085 -0.400 -1.934 -0.776 -0.863 -0.918  0.090 -0.377 -0.818 -0.213 -0.069  1.987
1952  0.368 -1.747 -1.859  0.539 -0.774 -0.441  0.383 -0.030 -0.383 -0.437 -1.891 -1.827
1953 -1.036 -0.249  1.068 -1.256 -0.562  0.023  0.333  0.085  0.662 -0.194  0.354  0.575
1954 -0.148 -0.181  0.476  0.512 -1.656 -0.268  0.341 -0.122  0.301  0.513 -0.328  0.553
1955 -1.163 -1.542 -1.568  0.194  0.242 -0.266  0.332  0.760  0.357  0.099 -1.342 -0.444
1956 -1.204 -2.029  0.470 -0.868  1.391  0.280 -0.215 -0.652 -0.202  1.139 -0.066  0.001
1957  2.062 -1.513 -2.013  0.238 -0.966 -0.760 -0.646  0.097 -0.956  0.903 -1.380  0.828
1958 -1.438 -2.228 -2.522 -0.360 -0.336 -1.149 -0.684 -0.755 -0.012  0.770 -0.011 -1.687
1959 -2.013  2.544  1.432  0.119 -0.341 -0.033  0.105 -0.745 -0.281 -0.249 -1.411 -0.042
1960 -2.484 -2.212 -1.625 -0.297 -0.857  0.055 -0.619 -1.008 -0.382 -1.187 -0.553 -0.343
1961 -1.506  0.621  0.341 -0.237  0.157  0.837 -0.108  0.013  0.815  0.203 -0.010 -1.668
1962  1.645 -0.358 -2.848  1.169  0.068  0.287 -0.927  0.152 -0.056 -0.016 -1.112 -0.711
1963 -3.311 -1.721  0.724 -0.348  0.771 -0.585 -0.303 -0.625  0.083  1.069 -0.419 -1.178
1964  0.385 -0.575 -0.558  0.663  1.174  0.142  0.734 -1.207 -0.227  0.342 -0.344 -0.246
1965 -1.046 -2.084 -0.905  0.568 -0.153  0.038 -0.510 -0.255 -0.698  0.394 -1.341  0.163
1966 -3.232 -1.438 -0.911 -1.837  1.124  0.408  0.011 -0.945  0.011 -1.077  0.111 -1.401
1967 -0.576  1.180  1.967  1.700  0.127  0.647  0.259 -0.293  0.133  1.299  0.334 -0.347
1968 -0.409 -2.154  1.741  0.328 -0.241  0.420 -0.836 -0.671 -1.009 -1.013 -2.183 -0.783
1969 -2.967 -3.114 -1.582  0.438 -0.720 -0.348  0.410 -0.782 -0.083  0.098  0.326 -1.856
1970 -2.412 -1.325 -2.084  0.302  0.531  0.875  0.139 -0.263  0.030  0.098  0.378 -0.399
1971 -0.163 -0.922 -1.091 -0.583  0.679 -0.668 -0.578  0.818  0.153  1.185  0.419  0.824
1972  0.166 -0.195 -0.141  1.007  0.140 -0.049 -0.553 -0.082 -0.920  0.392 -0.380  1.238
1973  1.232  0.786  0.537 -1.126  0.073  0.531  0.270  0.313  0.114  0.337  0.002 -0.181
1974  0.232 -0.489 -0.746  0.309 -0.507 -0.048  0.390 -0.533 -0.136 -1.024 -0.435  0.556
1975  1.595  0.194  0.151  0.409 -0.614 -0.323  0.345  0.130  1.278  0.138  0.619  1.290
1976  0.034  1.656  0.587  0.440  0.060  0.328 -0.325  0.559 -0.743 -0.804 -0.087 -2.074
1977 -3.767 -2.010  0.344  1.329  0.104 -0.226 -0.492 -1.412  0.586 -0.009  0.605 -0.240
1978 -0.347 -3.014  0.502 -0.967  0.059  0.635 -0.604 -0.354 -0.099  0.895  2.470 -0.980
1979 -2.233 -0.697 -0.814 -1.157 -0.250  0.933  0.039 -0.684 -0.046 -1.243  0.475  1.295
1980 -2.066 -0.934 -1.433 -0.419 -1.155  0.721 -0.622 -0.185  0.313 -0.521 -1.361 -0.057
1981 -0.116 -0.332 -1.645  0.430  0.180 -0.438  0.561 -0.244 -1.040 -1.167 -0.188 -1.216
1982 -0.883  0.974  1.074  1.454 -0.209 -1.180  0.005  0.362  0.558 -0.211  0.661  0.967
1983  1.359 -1.806 -0.567 -0.738 -0.441  0.313  0.131  1.098  0.167  1.369 -0.688  0.186
1984  0.905 -0.303 -2.386 -0.284  0.479  0.007  0.019  0.466 -0.413 -0.270 -0.966  0.446
1985 -2.806 -1.440  0.551  0.652 -0.432 -0.347 -0.390 -0.001  0.114  1.035 -1.218 -1.948
1986 -0.568 -2.904  1.931  0.103  0.367  0.535 -0.008 -0.826 -0.023  1.425  0.926  0.060
1987 -1.148 -1.473 -1.746  0.387  0.325 -0.710 -0.466 -0.836  0.287 -0.080 -0.536 -0.534
1988  0.265 -1.066 -0.197 -0.561 -0.846  0.061 -0.143  0.255  1.039  0.032 -0.035  1.679
1989  3.106  3.279  1.530 -0.250  0.889  0.345  0.866  0.551  0.703  0.991  0.034 -0.644
1990  1.001  3.402  2.990  1.879  0.943  0.304 -0.296 -0.180 -0.210  0.660  0.521  1.277
1991  0.723 -0.876 -0.527  0.530  0.486 -0.115 -0.188  0.797 -0.112 -0.252  0.285  1.613
1992  0.550  1.122  0.984 -0.521  1.341 -0.302  0.191  0.535 -0.640 -0.366  0.717  1.627
1993  3.495  0.184  0.764 -0.435 -1.607 -0.520 -0.511 -0.393 -0.361 -0.565  1.002 -0.104
1994 -0.288 -0.862  1.881  0.225 -0.115  1.606  0.351  0.828 -0.084  0.174  1.779  0.894
1995 -0.154  1.429  0.393 -0.963 -0.891 -0.112 -0.217  0.544 -0.549  0.075 -0.723 -2.127
1996 -1.200  0.163 -1.483 -1.525 -0.226  0.497  0.715  0.125 -1.140  0.183  0.136 -1.721
1997 -0.457  1.889  1.091  0.324 -0.961 -0.815 -0.431  0.121  0.195 -0.700 -0.661 -0.071
1998 -2.081 -0.183 -0.254 -0.038  0.429 -0.711 -0.212  0.650 -1.050  0.294 -1.449  1.353
1999  0.110  0.482 -1.492  0.284  0.226  0.707 -0.002 -0.672  0.059 -0.006  0.611  1.043
2000  1.270  1.076 -0.451 -0.279  0.969  0.586 -0.649  0.144  0.395  0.317 -1.581 -2.354
2001 -0.959 -0.622 -1.687  0.906  0.452 -0.015 -0.031  0.521 -0.707  0.707  0.819 -1.322
2002  1.381  1.304  0.902  0.748  0.401  0.573  0.328 -0.229 -0.043 -1.489 -1.425 -1.592
2003 -0.472  0.128  0.933 -0.178  1.017 -0.102  0.075 -0.280  0.467 -0.670  0.642  0.265
2004 -1.686 -1.528  0.318 -0.409 -0.094 -0.236 -0.201 -0.720  0.855 -0.515  0.678  0.265
2005  0.356 -1.271 -1.348 -0.046 -0.763 -0.383 -0.030  0.026  0.802  0.030  0.228 -2.104
2006 -0.170 -0.156 -1.604  0.138  0.156  1.071  0.103 -0.265  0.606 -1.029  0.521  2.282
2007  2.034 -1.307  1.182  0.544  0.894 -0.555 -0.397 -0.034  0.179  0.383 -0.519  0.821
2008  0.819  0.938  0.586 -0.455 -1.205 -0.090 -0.480 -0.080 -0.327  1.676  0.092  0.648
2009  0.800 -0.672  0.121  0.973  1.194 -1.351 -1.356 -0.054  0.875 -1.540  0.459 -3.413
2010 -2.587 -4.266 -0.432 -0.275 -0.919 -0.013  0.435 -0.117 -0.865 -0.467 -0.376 -2.631
2011 -1.683  1.575  1.424  2.275 -0.035 -0.858 -0.472 -1.063  0.665  0.800  1.459  2.221
2012 -0.220 -0.036  1.037 -0.035  0.168 -0.672  0.168  0.014  0.772 -1.514 -0.111 -1.749
2013 -0.610 -1.007 -3.185  0.322  0.494  0.549 -0.011  0.154 -0.461  0.263  2.029  1.475
2014 -0.969  0.044  1.206  0.972  0.464 -0.507 -0.489 -0.372  0.102 -1.134 -0.530  0.413
2015  1.092  1.043  1.837  1.216  0.763  0.427 -1.108 -0.689 -0.165 -0.250  1.945  1.444
2016 -1.449 -0.024  0.280 -1.051 -0.036  0.312  0.848  0.472  0.781 -0.192 -0.611  0.179
2017  0.942  0.340  1.365 -0.089 -0.730  0.402  0.634  0.150 -0.492  0.690 -0.078 -0.059
2018 -0.281  0.113 -0.941  0.544  0.118  0.380  0.612  0.836  0.585  0.413 -0.112  0.110
2019    -0.713    1.149    2.116   -0.255   -1.231   -0.601   -0.890   -0.722    0.306   -0.082   -1.193    0.412
2020     2.419    3.417    2.641    0.928   -0.027   -0.122   -0.412   -0.381    0.631   -0.071    2.086   -1.736
2021    -2.248   -1.119    2.109   -0.204   -0.160    0.840    0.625   -0.217   -0.247   -0.139    0.099   -999.0"""

_NAO = """
 1821 -99.99 -99.99 -99.99 -99.99 -99.99 -99.99  -2.62  -0.14 -99.99 -99.99 -99.99 -99.99
 1822 -99.99 -99.99   2.99  -3.19   0.59  -0.86  -4.05  -0.19  -1.09  -2.00  -0.05  -0.73
 1823  -3.39 -99.99 -99.99 -99.99   4.65  -0.83   0.58   2.90   0.67  -1.39  -0.76  -0.20
 1824  -0.16   0.25  -1.44   1.46   1.34  -3.94  -2.75  -0.08   0.19 -99.99  -0.70  -0.01
 1825  -0.23   0.21   0.33  -0.28   0.13   0.41  -0.92   1.43  -0.95   1.98   1.06  -1.31
 1826  -3.05   4.87  -0.97   1.78  -1.20   0.83   1.89   2.72  -0.76   0.18  -2.41  -0.59
 1827  -0.45  -3.72   1.83  -0.83   1.20  -0.07   2.02  -3.56  -0.07  -3.02  -1.42   2.70
 1828   1.27   0.37  -0.18   0.04  -1.59  -1.33  -4.40  -2.54  -2.78   0.10  -2.57   3.04
 1829  -2.48   0.32  -2.54   0.12   1.80  -0.10   0.33   0.77   0.78   0.71  -0.33  -0.43
 1830  -2.33   1.20   3.58   3.08  -0.05  -0.85   3.19  -0.35   2.04   2.04   2.19  -3.13
 1831  -2.91   1.40   1.48  -3.15  -2.47  -1.36   2.71  -3.04  -1.53   0.85   0.26   0.36
 1832  -0.04   0.83   2.12  -1.51  -1.96  -3.62  -2.57   0.92   1.45   2.25   0.62   3.32
 1833  -0.36   2.52  -2.89   2.02   0.69  -1.52   0.13  -1.74  -0.93  -1.75   1.40   4.17
 1834   3.07   2.66   1.37  -2.38  -1.03   0.27  -0.73  -0.86  -0.62   0.30  -2.28   0.11
 1835   0.37   3.37   1.54  -1.02   0.58   0.10   0.57   2.35   0.29  -0.30  -1.31  -1.46
 1836   1.47   0.06   2.28   0.87  -1.50   2.95   4.33   2.80  -1.59  -1.17   2.04  -1.41
 1837  -1.16   4.67  -3.08  -0.56  -1.02  -2.98  -2.40   0.01   0.17   2.52   1.34   1.37
 1838  -2.16  -1.81   1.23  -0.61  -2.16   1.24   0.11   1.16   1.46   0.59  -2.65   2.55
 1839   1.24   4.20   0.79   1.40  -0.94   0.01   1.14   0.04   1.09  -1.27  -2.89  -0.63
 1840   2.97  -0.40  -3.05   0.87  -0.58  -0.09   1.23   0.05   0.46  -2.50   0.46  -2.43
 1841  -0.71  -1.37   2.41   1.97   1.65  -0.61  -0.62   2.39  -2.76  -2.13   1.76   0.21
 1842   2.45   4.26   3.43  -0.44  -0.85  -4.30  -4.05   1.03  -3.80  -3.73  -2.66   0.51
 1843   2.99  -3.51  -1.29   2.03  -0.49  -1.92   3.26   3.99  -0.58  -1.90   0.87   3.13
 1844   0.20   0.11   1.09   3.91  -2.77  -0.12   0.36  -1.00  -1.53  -0.99  -0.02  -1.90
 1845   1.17   0.06  -0.54   0.56  -0.97   2.07  -0.16  -0.29  -0.23   1.14   0.49   0.83
 1846   2.26   0.63   1.75  -1.42   0.19   1.45   2.84  -0.30  -1.18   0.01  -0.59  -2.55
 1847   0.03   0.10  -1.59   1.17   1.76  -0.26   0.75   1.13  -0.32   0.44   2.46   1.76
 1848  -0.79   1.77   0.76  -1.02   0.69  -1.78   1.87   2.64  -2.55  -2.44  -0.84   2.55
 1849   2.42   2.77  -0.56  -0.99  -0.52  -3.21   1.20   0.70  -2.23  -0.08   0.80  -1.24
 1850  -0.16   4.13  -2.22   0.97  -1.16   0.40   0.31   0.15  -2.08  -2.70   2.39   2.36
 1851   3.29   1.03   1.50  -1.66  -1.53  -1.62  -5.39   4.68   1.85   0.78  -1.77   1.74
 1852   1.46   0.41  -2.50  -1.60   0.25   0.09  -1.13   2.94  -2.02  -1.65  -0.93   1.03
 1853   1.31  -4.04  -0.32   0.76  -3.17   1.09   1.76  -2.36  -0.22  -0.47   0.51  -4.28
 1854   1.28   1.72   2.67   0.88   0.04  -0.06  -1.92  -0.03   2.62   1.11  -1.56   2.42
 1855  -1.84  -3.80  -0.05   0.99  -2.28   0.78  -2.61   3.81   0.79  -1.09  -2.42  -1.66
 1856  -1.25  -0.10  -2.27   2.00  -0.70   2.03  -0.16  -0.44  -0.50   1.12  -1.69  -0.23
 1857  -0.69   2.02   1.09   0.55  -0.17  -0.33   5.36   1.02   1.21  -0.20  -1.68   3.51
 1858   2.26  -0.54  -1.24   1.24   0.53  -0.24  -1.58   0.06   2.33  -1.86  -4.41   3.01
 1859   2.74   2.37   1.50  -1.12  -0.63  -0.06   2.24   1.82   0.11  -2.61   0.29  -1.31
 1860   1.54   0.32   1.08  -0.37  -1.51  -2.32  -2.27  -0.16  -0.92   2.28  -3.44  -2.14
 1861  -0.56   0.80   2.06  -1.86  -1.99  -1.04   0.73   2.91  -0.85  -0.80  -1.35  -1.50
 1862   1.15  -1.26  -2.25   0.64   0.65  -0.22  -2.08  -1.43  -1.50   1.75  -0.49   2.92
 1863   1.12   3.10   1.88   2.35  -1.49  -0.59  -0.43   0.10   2.46  -0.59   1.62   2.17
 1864   2.03  -0.27  -1.78   0.23  -1.83   1.76   0.50  -0.21   1.12  -6.05   0.01  -0.77
 1865   0.15  -0.42  -1.03   0.92   0.87   0.74  -0.07  -0.22   3.24  -2.66  -0.14   2.57
 1866   2.06   0.70  -2.10  -0.88  -1.54  -0.18   0.29   0.77   1.52  -0.03   1.01   2.14
 1867  -2.17   3.63  -3.03   3.08  -2.35  -1.20  -1.77   3.10   1.13   0.73  -1.51  -0.55
 1868   1.46   3.95   2.94   2.52   1.35   2.10   1.21   3.02  -2.65   1.87  -0.83   2.01
 1869   3.25   3.90  -1.91   2.62  -1.98  -0.71   0.29   1.15   0.62  -0.79   0.79  -0.69
 1870   0.32  -1.98  -2.07   2.92   1.55   0.56  -0.36  -3.41   1.71   1.30  -2.04  -3.52
 1871   0.67   1.71   1.15  -0.32  -2.50  -1.37   1.75   4.19  -1.93  -0.89  -3.72  -0.18
 1872   1.15   0.45  -1.20  -0.73   0.02  -0.34  -3.61  -1.43  -2.53  -0.91   0.67  -1.09
 1873   2.30   0.18  -0.39  -2.17  -0.93   0.78  -0.12   3.44  -0.57  -0.81  -2.23   2.01
 1874   1.56   2.07   1.47   2.99  -1.85  -0.76   0.18   0.82   0.74   0.86  -0.34  -2.12
 1875   2.06  -1.47  -0.61  -0.41   0.89   1.46  -1.44   1.71  -0.01  -0.75  -2.80   0.08
 1876   1.10   0.75  -0.29  -0.67  -1.45   1.71   3.48   1.02  -2.62  -2.19  -2.35  -1.13
 1877   2.39   1.96  -0.45  -2.30  -1.73  -0.32   1.18  -1.83  -3.74   1.25   2.06   2.16
 1878   1.18   2.20  -0.01   0.45   0.28  -1.54  -1.93  -2.46  -0.95  -1.44  -3.47  -3.31
 1879  -0.71   0.85  -0.08   0.10   0.63  -0.50  -1.57  -0.29   1.90  -1.88  -3.38   0.58
 1880   0.42   1.92   0.06   1.66  -1.78   0.45  -1.90  -0.43   0.92  -3.20   1.19   0.52
 1881  -3.60  -1.62  -0.51  -1.42   0.82   0.01   2.10   0.42  -0.25  -2.04   4.34   2.77
 1882   3.07   3.20   3.61  -0.42  -0.68  -0.64   1.60   2.05   0.40   0.65   2.01  -1.69
 1883   1.67   4.25  -3.04   0.88  -0.54  -1.75  -2.25   3.00   0.47   1.68   2.36   0.91
 1884   3.32   1.48   0.19  -2.36  -0.17   0.50  -0.80   2.16   1.60   0.27  -1.16   1.94
 1885  -0.80   0.09  -1.06   0.36   0.32   1.59   3.07  -1.03   1.40  -0.84  -0.76  -0.03
 1886  -1.41  -0.39   0.56  -1.37  -0.67  -1.17  -1.59   2.43  -0.34  -0.55   0.55   0.12
 1887   1.90   2.03  -0.85  -2.11   0.44   0.06   0.58  -1.19  -2.56  -1.14  -3.25  -1.62
 1888   0.21  -2.25  -1.50  -2.25   0.97  -1.70  -0.00   4.00  -0.42  -0.89   2.70   1.25
 1889   0.65  -0.20   0.11   1.05  -0.39   1.89  -1.03   3.78  -1.98  -1.23   2.70   2.30
 1890   4.32  -1.37   0.50  -0.08  -1.14   1.23   0.30   0.99   2.50   0.85   1.90  -2.75
 1891   0.27   2.81  -1.17  -0.92  -1.78  -3.74  -0.54   2.22   2.29  -0.46  -1.53   2.86
 1892  -0.77  -2.21  -1.53  -1.14  -0.57  -0.47   0.18   1.16   1.61  -3.68   0.81  -1.05
 1893  -1.61   2.54  -0.04   0.04   0.37  -0.56  -1.50   0.48  -0.97   0.32  -2.16   1.86
 1894   1.40   3.95   1.12   1.98  -1.38   2.78   1.18   0.91  -2.19  -2.24   1.96   0.94
 1895  -2.61  -4.14  -0.27   0.37   0.51  -0.20   1.21   1.72   1.15  -2.53   1.92   0.02
 1896  -0.23   2.33   1.39   2.54  -0.89  -0.27   1.23  -1.02   0.60  -2.77  -0.55   1.86
 1897  -2.36   3.32   2.31   4.28  -0.52  -1.42  -0.05   2.49   1.40  -0.60   0.02   1.35
 1898   1.97   1.90  -2.33   3.46  -0.53  -0.84  -1.53   3.56  -0.17  -1.15  -1.14   3.14
 1899   0.68  -0.17  -1.50   0.58  -1.03  -0.25   2.46  -1.13  -0.08  -0.12   1.94  -0.87
 1900   1.38  -2.36  -3.12   2.61  -0.57  -1.23  -0.21  -0.06   0.98  -0.57   0.65   3.50
 1901   0.98  -2.58  -0.91   2.53  -0.71   0.21  -1.83   1.14  -0.09  -0.47  -1.73  -1.38
 1902   1.41  -1.40   0.50  -1.14   0.54  -3.25  -1.24  -0.18  -1.51  -0.12  -0.09   1.27
 1903   1.28   4.86   4.05  -0.79   0.14  -2.80   0.43   3.67   0.22  -0.55   1.04  -1.09
 1904   2.24   1.21  -0.70   2.64   1.75  -0.87  -0.04   0.61  -0.43   0.04   0.07   0.88
 1905   1.81   2.09   2.23  -1.17  -0.72  -2.29  -0.05   0.97  -0.19  -3.10  -0.25   1.85
 1906   2.64   1.26  -0.25   1.67  -1.75  -1.68   1.29   0.38  -1.33   0.40   0.70   0.03
 1907   1.58   1.22   2.41   1.08  -1.42   0.76  -0.55   2.22   0.24  -1.59  -0.41   1.18
 1908   0.64   1.98   0.74  -1.75   1.92   0.83   0.09   0.60   0.98   0.24  -0.21   1.47
 1909   1.82  -0.54  -2.09   0.06  -0.92  -1.35   2.59   2.35  -1.29   0.59  -1.97  -0.48
 1910   2.57   3.85   0.55   0.08  -1.50  -1.07  -1.64   0.31  -1.15  -1.56  -0.87  -0.10
 1911   0.82   2.05  -1.40  -0.24   0.79   0.42   0.54   0.13   1.53  -1.88  -0.05   3.02
 1912  -0.91  -0.17   2.22  -0.10   1.70  -0.98  -1.42   0.07  -2.51   0.42   1.21   3.00
 1913   1.83   1.19   2.73   1.99   0.38   1.03  -0.99   0.65  -2.70  -1.48   4.62   1.23
 1914   0.58   2.45   1.72   2.08   2.19   0.57  -1.11   0.97   0.43  -1.10  -1.41   2.23
 1915   0.08   1.82  -1.91   2.91  -2.47  -2.30  -1.19  -1.29  -1.94  -0.99  -2.51  -0.65
 1916   3.82   2.03  -3.84   0.77  -0.72  -3.03  -0.69  -0.57  -2.59   2.20  -0.58  -1.80
 1917  -3.08  -1.59  -0.21  -0.92  -1.59   0.81  -0.21  -0.39   2.47   0.94   1.98  -2.80
 1918  -0.48   3.87   0.37  -1.91   0.23   1.31  -1.97   1.76  -0.17   0.56   0.26   2.32
 1919  -0.01  -0.49  -0.25   1.72   1.35   1.86  -1.33   4.03  -1.27  -2.24  -2.07   2.86
 1920   2.84   1.39   3.08   0.09   0.76  -1.62   1.87  -1.22   0.41  -1.15   1.48  -0.46
 1921   3.20   0.07   2.68  -0.09  -0.64  -1.60  -0.41  -0.65  -1.43  -0.22  -1.22   2.18
 1922   0.64   2.97  -0.23   0.80   2.36   0.79   1.79   0.09  -0.43  -3.95  -0.05   1.47
 1923   1.84   2.77  -0.10  -1.19   0.35   0.53   1.59   0.73   2.64   1.34  -1.97   1.25
 1924   0.86  -1.62  -1.88  -0.94  -0.55  -2.09   0.65   0.55   0.71   0.50  -0.21   3.86
 1925   4.23   1.95  -2.00   2.59   1.12  -2.20   1.37   1.43  -0.66  -0.98  -2.60  -0.72
 1926   1.70   1.84   0.56   2.33  -1.19  -1.79  -0.69   2.06   0.92  -4.16   0.12  -0.51
 1927   2.15   1.09   2.58   1.39  -2.03  -1.60  -0.16   1.60  -1.77  -2.04  -1.25  -3.14
 1928   3.04   3.52  -0.94   1.09  -2.90  -1.89   2.21  -1.80  -1.93   0.15   1.68   0.44
 1929  -1.26   0.27  -0.48  -3.80   0.67  -0.06   0.26  -0.07   0.25   0.29   2.15   3.80
 1930   1.51  -0.60  -0.70  -2.13   1.84  -0.37  -1.30   1.81  -2.07   0.89   1.44   1.21
 1931  -0.09   1.29  -2.18  -0.08  -0.62  -0.96  -0.13  -1.80  -2.73  -0.11   2.78   0.77
 1932   3.47  -3.31  -1.57   0.13  -0.68  -1.46  -0.80   2.18  -0.93   0.05   0.98   1.22
 1933   1.41  -1.81   1.26  -0.23  -0.55  -1.62   2.62   2.65  -2.03  -1.99  -2.97  -1.84
 1934   3.27   0.49   0.30  -1.67   1.41  -2.49  -1.17   1.51   2.50   0.76  -1.22   1.32
 1935  -0.50   2.70   0.39  -0.41  -3.21   1.34   2.03  -0.55   0.55   0.88   1.13  -1.37
 1936  -1.22  -2.44  -1.09  -1.54  -2.34   0.76   1.34   2.67  -0.81   0.87  -0.17   2.37
 1937   2.15   1.73  -2.02   2.19   2.31   0.49   0.19   0.28  -0.17  -2.41  -1.56  -1.09
 1938   2.64   0.60   3.13  -1.68  -0.35   0.97   1.60  -0.37  -0.29   1.88   3.24  -0.39
 1939  -0.69   2.91  -0.03   0.18  -0.90  -1.40  -0.44   0.80  -3.90  -2.51   1.53  -1.07
 1940  -2.27  -0.93  -0.72   0.53  -0.25  -1.20  -1.21   0.30  -1.10  -1.89   1.30   1.46
 1941  -3.50  -0.42  -1.29  -2.95  -0.54   0.24   1.08  -0.60  -0.97  -1.21  -0.09   1.44
 1942   0.75  -3.10  -0.92  -0.95   0.82  -2.10   0.15   0.08  -0.25  -0.21  -2.11   1.47
 1943   1.17   2.78   0.03   4.26   2.17   1.91   0.05  -0.18  -0.65   0.45   0.08  -0.39
 1944   3.63  -1.59  -0.82   1.30   0.42  -2.78  -2.16   0.15   0.36  -0.83   0.81   0.26
 1945  -2.12   4.67   2.51   1.15  -0.84   0.37  -0.40  -1.83   1.40  -0.22  -1.82  -0.25
 1946   1.41   0.99  -0.39   0.65  -2.70   2.56   2.66   0.62   1.98  -2.04  -1.26   1.22
 1947   0.39  -4.60  -1.28   6.66  -1.20   0.20   0.19  -1.08   1.18  -0.51  -0.25  -0.72
 1948   1.53   0.66   3.48  -0.48  -1.23  -0.27   0.59   0.34   0.82   0.43   2.64   1.09
 1949   1.50   4.01  -0.96   3.41  -1.39  -1.51  -0.93   1.38  -1.81   1.38   0.54   0.11
 1950   0.55   3.31   0.82   1.61  -1.73   1.26  -0.87  -0.28   1.51   0.78   0.78  -1.88
 1951   0.82   0.93  -2.01  -0.45  -2.11  -1.16   1.10   0.85  -0.22  -0.13  -0.97   2.54
 1952   0.92   0.15  -1.14   2.79  -0.94   0.02  -0.79  -1.05  -3.02   0.42  -1.51  -0.31
 1953  -0.02   0.54   1.25  -1.60  -0.75  -2.96   0.13   3.26   0.75   0.77   3.25   0.15
 1954   0.10   0.57  -0.29  -0.26  -0.91  -0.94   0.88  -0.59   2.49   2.09   1.54   1.44
 1955  -1.17  -2.21  -2.90   2.40   0.33  -0.18  -1.32   0.54   0.82  -2.35  -2.14   0.51
 1956  -0.76  -2.96   0.01  -1.90   4.54   1.26   0.35  -3.15  -0.51   1.23   1.39   2.57
 1957   2.53   1.08   0.42  -0.62  -0.84  -0.80  -0.48   0.70  -1.56   1.07  -1.59  -0.12
 1958   0.37  -0.03  -1.28   1.79   1.10  -1.44  -0.20   0.98  -0.23   1.65   0.43  -1.70
 1959  -1.15   2.46   1.82   1.51  -2.22   1.51   0.29   0.02  -1.81   1.51  -0.04   1.98
 1960  -0.70  -1.00  -0.87   1.93   0.07  -0.41   0.18  -1.84   0.24  -3.08   1.40   0.46
 1961   1.46   4.06   2.08   0.71  -0.94   2.13   0.63   3.38   2.01   1.00  -2.15  -1.72
 1962   2.44   0.77  -3.78   0.74  -0.10   1.41  -2.10   2.28   0.02  -0.34  -2.23  -0.66
 1963  -4.09  -1.90   2.79  -0.46   1.91  -1.77  -0.65  -0.96   0.94   2.79  -0.15  -3.09
 1964   0.93  -0.13  -0.77   0.95   2.51  -1.85   2.44  -2.46   0.50   0.63   1.33  -1.24
 1965   0.01  -3.03   0.23   2.14  -0.08   0.87  -1.71   1.59  -1.01  -1.26  -1.78   1.24
 1966  -1.01  -0.38   1.05   1.18   1.51   0.82  -1.99  -2.03  -0.47  -2.89  -0.07   1.68
 1967   0.04   1.70   3.00  -0.76  -0.46   1.96   1.44  -0.41   0.32   1.34  -0.91  -0.53
 1968   1.65  -1.53   0.34  -0.71  -1.50   0.95  -1.96  -1.45   0.50   0.03  -2.00  -1.73
 1969  -1.64  -3.16  -1.81   1.11  -0.23  -1.17   3.70  -1.62   0.38   0.70  -1.28  -0.26
 1970  -1.16   1.10  -1.78   2.52   1.87  -0.11   0.27  -0.20   0.47  -0.00   0.76  -1.58
 1971  -0.43   1.21  -1.76  -3.15  -0.62  -1.32  -1.04   0.07  -0.54   1.63  -1.46   0.76
 1972  -0.52  -0.20   0.26   0.22   1.24   1.07   0.41   0.11  -4.11  -1.74   0.64   2.11
 1973   1.37   1.22   1.04  -2.61   0.37   0.83  -1.85   2.32  -0.79  -1.03  -0.26  -1.65
 1974   3.75   0.68  -0.81  -2.30  -0.01  -0.14   2.07   0.89   0.11  -1.44   1.27   3.06
 1975   2.43   0.40  -1.26  -0.84  -2.42   0.18   0.63   0.08   1.75   0.39   0.86  -1.57
 1976   0.75   1.29   1.87  -1.53   1.20   1.76  -0.57   0.62  -3.46  -0.64   1.50  -3.63
 1977  -2.36   0.28   1.33   1.07  -1.62  -0.89  -1.14  -1.42   1.64   0.45   0.37  -0.25
 1978   0.46  -1.99   3.10  -3.12   0.37   0.14  -0.33   0.05   1.96   0.02   3.91  -2.08
 1979  -3.22  -0.62   0.54  -0.79   1.00   0.45   2.53  -0.85   1.12  -1.95   1.95   2.07
 1980  -1.80   0.70  -0.68   0.03  -2.26  -0.21  -0.91   0.30   1.72  -0.87  -2.06   1.55
 1981   1.00   1.04   0.01  -3.04   0.05  -1.57   1.74   1.01   0.27  -1.06   1.66  -2.20
 1982  -0.72   2.25   1.66  -0.99   1.10  -1.86  -0.65   1.45   1.08   0.32   1.71   2.64
 1983   4.82  -1.25   1.79  -1.01  -0.57   0.54  -0.75   0.56  -0.65   2.06  -2.28   0.83
 1984   2.53   1.73  -2.12   0.33  -2.34   0.33   0.93   1.00  -1.31   1.66  -1.16   1.52
 1985  -2.87  -0.24   0.07   0.34  -2.13  -1.08   1.09   2.33   0.00   0.14  -2.85  -0.43
 1986   1.46  -4.02   2.86  -0.93   2.16  -1.29   0.88  -2.21  -1.34   2.27   3.41   3.42
 1987  -2.12  -0.24   0.29   2.59  -0.81  -0.58  -1.25  -2.99   1.27  -0.80  -0.67  -0.81
 1988   0.53  -0.11   0.78  -2.39  -1.24  -2.75   1.46   0.73   0.80  -2.02  -1.47   1.85
 1989   3.53   3.61   2.45  -0.48   1.16  -0.53   0.58   1.76  -0.96   0.88  -2.97  -2.23
 1990   3.50   5.11   3.11   1.77  -1.19   0.42   1.43   3.31  -0.99  -0.59  -1.48   0.34
 1991   1.87  -0.02  -1.37   1.48  -0.04  -0.31  -0.28   2.71  -1.12  -1.77   1.68   1.24
 1992   0.64   3.18   1.66   1.32   0.79  -1.74   1.04   3.97   0.99  -3.33   4.52   0.21
 1993   3.91   0.11   1.47   0.83  -2.59   0.16   0.64   0.75  -2.60  -4.13   0.77   2.17
 1994   1.28   0.07   3.68   1.38  -1.43   2.98  -0.09  -1.59  -2.85  -1.88   1.68   2.86
 1995   2.70   3.13   1.06  -1.81  -0.36  -3.36  -0.96  -1.33  -1.55   1.22  -2.73  -3.33
 1996  -3.27  -0.12  -2.57  -0.31  -1.50   1.43   1.47  -0.19  -2.23  -0.07  -0.05  -4.70
 1997  -1.95   5.26   2.09  -0.97  -1.35  -4.05   1.18   1.78  -0.67  -2.26  -0.99  -0.20
 1998  -0.28   2.44   1.24  -0.39  -1.26  -0.85  -0.57   1.80  -3.48   1.34   1.13   1.95
 1999   0.90   1.80  -0.72   0.43   1.03   1.39  -1.85  -3.67  -0.51  -0.69   0.30   2.13
 2000   0.35   4.37   0.54  -3.34   0.31   0.89  -2.99   0.78  -1.10   1.37  -0.24  -1.41
 2001   0.02   0.07  -0.68   1.24  -0.09  -1.33  -1.12   1.64  -3.83   0.88   0.01  -2.25
 2002   2.31   3.01   0.09   0.91  -0.05   0.90  -0.71  -0.61  -3.58  -1.50  -0.27  -0.98
 2003   0.15   1.34   1.08  -1.74   1.17  -0.86   0.09  -0.99   0.35  -3.68   0.31  -0.85
 2004   0.20  -1.23   1.07   1.08  -0.67  -0.38  -0.30  -0.76   2.51  -2.18  -0.55   1.27
 2005   1.82  -2.25  -1.29   0.71  -0.13  -1.00  -0.08   0.94   0.50  -0.45  -1.01  -0.81
 2006  -0.10  -1.24  -1.12   0.57  -0.22  -0.41   0.83  -2.47  -1.02  -1.97   2.00   3.03
 2007   1.76   0.42   2.03  -0.10   0.62  -3.34  -1.05  -3.41  -1.18  -0.02  -1.67   1.36
 2008   1.85   1.79   0.37  -2.02  -3.26  -1.62  -1.13  -0.21  -2.07   0.01  -1.30  -0.58
 2009   0.60  -1.43   0.15   1.74   1.52  -3.05  -0.92   1.07  -0.63  -1.53   1.68  -3.73
 2010  -2.38  -3.92  -0.80  -1.03  -1.66  -3.65   0.06  -2.01  -2.38  -2.41  -3.34  -4.61
 2011  -1.38   2.79  -0.17   2.39   1.08  -1.58  -3.39  -2.41   2.97   1.31   0.74   3.20
 2012   2.05   1.28   1.78  -2.36  -0.83  -2.58  -1.31  -0.44  -1.44  -3.21  -1.11   0.60
 2013   1.08  -0.26  -3.75   0.03   1.23   1.40   2.52   2.16  -0.57  -0.36   0.04   3.54
 2014   0.71   2.32   1.64   0.84  -0.08  -1.98   0.91  -1.14  -2.10   0.31  -2.17   1.89
 2015   2.81   1.47   1.99   1.03   2.09   0.28  -2.16   1.47  -1.65  -1.13   3.54   4.22
 2016   1.17   1.61   0.33  -2.06  -0.83  -1.27   2.19   2.14   2.45  -1.47  -1.61   2.10
 2017   0.17   1.38   1.05   1.50   0.38  -0.55   0.10  -0.04   1.42   1.36  -0.90   1.00
 2018   1.82  -0.10  -1.12   2.37   2.01  -1.40   3.83   1.26   0.45  -1.17  -1.28   1.93
 2019  -0.36   1.90   2.39   1.70   2.05  -2.82  -2.79   0.10  -0.32  -1.11  -1.84   0.74
 2020   3.11   4.70   0.36  -0.71  -0.09  -1.52  -1.23  -1.36   0.49  -0.19   1.25  -0.78
 2021  -1.57   0.50   0.72  -3.31  -0.34   0.35  -1.59 -99.99 -99.99 -99.99 -99.99 -99.99"""

_PDO = """
1900     0.04   1.32   0.49   0.35   0.77   0.65   0.95   0.14  -0.24   0.23  -0.44   1.19
1901     0.79  -0.12   0.35   0.61  -0.42  -0.05  -0.60  -1.20  -0.33   0.16  -0.60  -0.14
1902     0.82   1.58   0.48   1.37   1.09   0.52   1.58   1.57   0.44   0.70   0.16  -1.10
1903     0.86  -0.24  -0.22  -0.50   0.43   0.23   0.40   1.01  -0.24   0.18   0.08  -0.03
1904     0.63  -0.91  -0.71  -0.07  -0.22  -1.53  -1.58  -0.64   0.06   0.43   1.45   0.06
1905     0.73   0.91   1.31   1.59  -0.07   0.69   0.85   1.26  -0.03  -0.15   1.11  -0.50
1906     0.92   1.18   0.83   0.74   0.44   1.24   0.09  -0.53  -0.31   0.08   1.69  -0.54
1907    -0.30  -0.32  -0.19  -0.16   0.16   0.57   0.63  -0.96  -0.23   0.84   0.66   0.72
1908     1.36   1.02   0.67   0.23   0.23   0.41   0.60  -1.04  -0.16  -0.41   0.47   1.16
1909     0.23   1.01   0.54   0.24  -0.39  -0.64  -0.39  -0.68  -0.89  -0.02  -0.40  -0.01
1910    -0.25  -0.70   0.18  -0.37  -0.06  -0.28   0.03  -0.06   0.40  -0.66   0.02   0.84
1911    -1.11   0.00  -0.78  -0.73   0.17   0.02   0.48   0.43   0.29   0.20  -0.86   0.01
1912    -1.72  -0.23  -0.04  -0.38  -0.02   0.77   1.07  -0.84   0.94   0.56   0.74   0.98
1913    -0.03   0.34   0.06  -0.92   0.66   1.43   1.06   1.29   0.73   0.62   0.75   0.90
1914     0.34  -0.29   0.08   1.20   0.11   0.11  -0.21   0.11  -0.34  -0.11   0.03   0.89
1915    -0.41   0.14  -1.22   1.40   0.32   0.99   1.07   0.27  -0.05  -0.43  -0.12   0.17
1916    -0.64  -0.19  -0.11   0.35   0.42  -0.82  -0.78  -0.73  -0.77  -0.22  -0.68  -1.94
1917    -0.79  -0.84  -0.71  -0.34   0.82  -0.03   0.10  -0.22  -0.40  -1.75  -0.34  -0.60
1918    -1.13  -0.66  -1.15  -0.32  -0.33   0.07   0.98  -0.31  -0.59   0.61   0.34   0.86
1919    -1.07   1.31  -0.50   0.08   0.17  -0.71  -0.47   0.38   0.06  -0.42  -0.80   0.76
1920    -1.18   0.06  -0.78  -1.29  -0.97  -1.30  -0.90  -2.21  -1.28  -1.06  -0.26   0.29
1921    -0.66  -0.61  -0.01  -0.93  -0.42   0.40  -0.58  -0.69  -0.78  -0.23   1.92   1.42
1922     1.05  -0.85   0.08   0.43  -0.19  -1.04  -0.82  -0.93  -0.81   0.84  -0.60   0.48
1923     0.75  -0.04   0.49   0.99  -0.20   0.68   1.16   0.84  -0.24   1.10   0.62  -0.36
1924     1.29   0.73   1.13  -0.02   0.36   0.75  -0.55  -0.67  -0.48  -1.25   0.24   0.11
1925    -0.05  -0.14   0.20   0.86   0.79  -1.08  -0.06  -0.86   0.52   0.04   0.88   1.19
1926     0.30   0.98  -0.50   2.10   1.43   2.03   1.05   1.64   1.18   1.65   1.00   1.06
1927     1.07   1.73   0.15  -0.18   0.30   0.69  -0.31  -0.73  -0.41  -0.62  -0.07   0.07
1928     0.96   0.79   0.52   0.81   0.66   0.15   0.30  -0.72  -1.41  -1.31   0.14   0.98
1929     0.97   0.52   0.50   0.55   1.07   0.50  -0.06  -0.69   0.45  -0.21   1.24  -0.03
1930     0.97  -1.06  -0.43  -0.70   0.06   0.58  -0.45  -0.53  -0.20  -0.38  -0.31   1.20
1931     0.08   1.56   1.13   1.28   1.66   0.39   1.49   0.02  -0.01  -0.17   0.34   1.09
1932    -0.26  -0.58   0.51   1.15   0.64   0.10  -0.12  -0.14  -0.40  -0.29  -0.88   0.02
1933     0.29   0.02   0.15  -0.05  -0.50  -0.68  -1.81  -1.56  -2.28  -1.19   0.55  -1.10
1934     0.17   0.68   1.34   1.63   1.23   0.51   0.44   1.54   1.25   2.10   1.63   1.67
1935     1.01   0.79  -0.11   1.10   0.99   1.39   0.68   0.63   0.98   0.21   0.13   1.78
1936     1.79   1.75   1.36   1.32   1.83   2.37   2.57   1.71   0.04   2.10   2.65   1.28
1937     0.00  -0.49   0.38   0.20   0.53   1.75   0.11  -0.35   0.63   0.76  -0.18   0.55
1938     0.50   0.02   0.24   0.27  -0.25  -0.20  -0.21  -0.45  -0.01   0.07   0.48   1.40
1939     1.36   0.07  -0.39   0.45   0.98   1.04  -0.21  -0.74  -1.10  -1.31  -0.88   1.51
1940     2.03   1.74   1.89   2.37   2.32   2.43   2.12   1.40   1.10   1.19   0.68   1.96
1941     2.14   2.07   2.41   1.89   2.25   3.01   2.33   3.31   1.99   1.22   0.40   0.91
1942     1.01   0.79   0.29   0.79   0.84   1.19   0.12   0.44   0.68   0.54  -0.10  -1.00
1943    -0.18   0.02   0.26   1.08   0.43   0.68  -0.36  -0.90  -0.49  -0.04   0.29   0.58
1944     0.18   0.17   0.08   0.72  -0.35  -0.98  -0.40  -0.51  -0.56  -0.40   0.33   0.20
1945    -1.02   0.72  -0.42  -0.40  -0.07   0.56   1.02   0.18  -0.27   0.10  -1.94  -0.74
1946    -0.91  -0.32  -0.41  -0.78   0.50  -0.86  -0.84  -0.36  -0.22  -0.36  -1.48  -0.96
1947    -0.73  -0.29   1.17   0.70   0.37   1.36   0.16   0.30   0.58   0.85  -0.14   1.67
1948    -0.11  -0.74  -0.03  -1.33  -0.23   0.08  -0.92  -1.56  -1.74  -1.32  -0.89  -1.70
1949    -2.01  -3.60  -1.00  -0.53  -1.07  -0.70  -0.56  -1.30  -0.93  -1.41  -0.83  -0.80
1950    -2.13  -2.91  -1.13  -1.20  -2.23  -1.77  -2.93  -0.70  -2.14  -1.36  -2.46  -0.76
1951    -1.54  -1.06  -1.90  -0.36  -0.25  -1.09   0.70  -1.37  -0.08  -0.32  -0.28  -1.68
1952    -2.01  -0.46  -0.63  -1.05  -1.00  -1.43  -1.25  -0.60  -0.89  -0.35  -0.76   0.04
1953    -0.57  -0.07  -1.12   0.05   0.43   0.29   0.74   0.05  -0.63  -1.09  -0.03   0.07
1954    -1.32  -1.61  -0.52  -1.33   0.01   0.97   0.43   0.08  -0.94   0.52   0.72  -0.50
1955     0.20  -1.52  -1.26  -1.97  -1.21  -2.44  -2.35  -2.25  -1.95  -2.80  -3.08  -2.75
1956    -2.48  -2.74  -2.56  -2.17  -1.41  -1.70  -1.03  -1.16  -0.71  -2.30  -2.11  -1.28
1957    -1.82  -0.68   0.03  -0.58   0.57   1.76   0.72   0.51   1.59   1.50  -0.32  -0.55
1958     0.25   0.62   0.25   1.06   1.28   1.33   0.89   1.06   0.29   0.01  -0.18   0.86
1959     0.69  -0.43  -0.95  -0.02   0.23   0.44  -0.50  -0.62  -0.85   0.52   1.11   0.06
1960     0.30   0.52  -0.21   0.09   0.91   0.64  -0.27  -0.38  -0.94   0.09  -0.23   0.17
1961     1.18   0.43   0.09   0.34  -0.06  -0.61  -1.22  -1.13  -2.01  -2.28  -1.85  -2.69
1962    -1.29  -1.15  -1.42  -0.80  -1.22  -1.62  -1.46  -0.48  -1.58  -1.55  -0.37  -0.96
1963    -0.33  -0.16  -0.54  -0.41  -0.65  -0.88  -1.00  -1.03   0.45  -0.52  -2.08  -1.08
1964     0.01  -0.21  -0.87  -1.03  -1.91  -0.32  -0.51  -1.03  -0.68  -0.37  -0.80  -1.52
1965    -1.24  -1.16   0.04   0.62  -0.66  -0.80  -0.47   0.20   0.59  -0.36  -0.59   0.06
1966    -0.82  -0.03  -1.29   0.06  -0.53   0.16   0.26  -0.35  -0.33  -1.17  -1.15  -0.32
1967    -0.20  -0.18  -1.20  -0.89  -1.24  -1.16  -0.89  -1.24  -0.72  -0.64  -0.05  -0.40
1968    -0.95  -0.40  -0.31  -1.03  -0.53  -0.35   0.53   0.19   0.06  -0.34  -0.44  -1.27
1969    -1.26  -0.95  -0.50  -0.44  -0.20   0.89   0.10  -0.81  -0.66   1.12   0.15   1.38
1970     0.61   0.43   1.33   0.43  -0.49   0.06  -0.68  -1.63  -1.67  -1.39  -0.80  -0.97
1971    -1.90  -1.74  -1.68  -1.59  -1.55  -1.55  -2.20  -0.15   0.21  -0.22  -1.25  -1.87
1972    -1.99  -1.83  -2.09  -1.65  -1.57  -1.87  -0.83   0.25   0.17   0.11   0.57  -0.33
1973    -0.46  -0.61  -0.50  -0.69  -0.76  -0.97  -0.57  -1.14  -0.51  -0.87  -1.81  -0.76
1974    -1.22  -1.65  -0.90  -0.52  -0.28  -0.31  -0.08   0.27   0.44  -0.10   0.43  -0.12
1975    -0.84  -0.71  -0.51  -1.30  -1.02  -1.16  -0.40  -1.07  -1.23  -1.29  -2.08  -1.61
1976    -1.14  -1.85  -0.96  -0.89  -0.68  -0.67   0.61   1.28   0.82   1.11   1.25   1.22
1977     1.65   1.11   0.72   0.30   0.31   0.42   0.19   0.64  -0.55  -0.61  -0.72  -0.69
1978     0.34   1.45   1.34   1.29   0.90   0.15  -1.24  -0.56  -0.44   0.10  -0.07  -0.43
1979    -0.58  -1.33   0.30   0.89   1.09   0.17   0.84   0.52   1.00   1.06   0.48  -0.42
1980    -0.11   1.32   1.09   1.49   1.20  -0.22   0.23   0.51   0.10   1.35   0.37  -0.10
1981     0.59   1.46   0.99   1.45   1.75   1.69   0.84   0.18   0.42   0.18   0.80   0.67
1982     0.34   0.20   0.19  -0.19  -0.58  -0.78   0.58   0.39   0.84   0.37  -0.25   0.26
1983     0.56   1.14   2.11   1.87   1.80   2.36   3.51   1.85   0.91   0.96   1.02   1.69
1984     1.50   1.21   1.77   1.52   1.30   0.18  -0.18  -0.03   0.67   0.58   0.71   0.82
1985     1.27   0.94   0.57   0.19   0.00   0.18   1.07   0.81   0.44   0.29  -0.75   0.38
1986     1.12   1.61   2.18   1.55   1.16   0.89   1.38   0.22   0.22   1.00   1.77   1.77
1987     1.88   1.75   2.10   2.16   1.85   0.73   2.01   2.83   2.44   1.36   1.47   1.27
1988     0.93   1.24   1.42   0.94   1.20   0.74   0.64   0.19  -0.37  -0.10  -0.02  -0.43
1989    -0.95  -1.02  -0.83  -0.32   0.47   0.36   0.83   0.09   0.05  -0.12  -0.50  -0.21
1990    -0.30  -0.65  -0.62   0.27   0.44   0.44   0.27   0.11   0.38  -0.69  -1.69  -2.23
1991    -2.02  -1.19  -0.74  -1.01  -0.51  -1.47  -0.10   0.36   0.65   0.49   0.42   0.09
1992     0.05   0.31   0.67   0.75   1.54   1.26   1.90   1.44   0.83   0.93   0.93   0.53
1993     0.05   0.19   0.76   1.21   2.13   2.34   2.35   2.69   1.56   1.41   1.24   1.07
1994     1.21   0.59   0.80   1.05   1.23   0.46   0.06  -0.79  -1.36  -1.32  -1.96  -1.79
1995    -0.49   0.46   0.75   0.83   1.46   1.27   1.71   0.21   1.16   0.47  -0.28   0.16
1996     0.59   0.75   1.01   1.46   2.18   1.10   0.77  -0.14   0.24  -0.33   0.09  -0.03
1997     0.23   0.28   0.65   1.05   1.83   2.76   2.35   2.79   2.19   1.61   1.12   0.67
1998     0.83   1.56   2.01   1.27   0.70   0.40  -0.04  -0.22  -1.21  -1.39  -0.52  -0.44
1999    -0.32  -0.66  -0.33  -0.41  -0.68  -1.30  -0.66  -0.96  -1.53  -2.23  -2.05  -1.63
2000    -2.00  -0.83   0.29   0.35  -0.05  -0.44  -0.66  -1.19  -1.24  -1.30  -0.53   0.52
2001      .60    .29   0.45  -0.31  -0.30  -0.47  -1.31  -0.77  -1.37  -1.37  -1.26  -0.93
2002     0.27  -0.64  -0.43  -0.32  -0.63  -0.35  -0.31   0.60   0.43   0.42   1.51   2.10
2003     2.09   1.75   1.51   1.18   0.89   0.68   0.96   0.88   0.01   0.83   0.52   0.33
2004     0.43   0.48   0.61   0.57   0.88   0.04   0.44   0.85   0.75  -0.11  -0.63  -0.17
2005     0.44   0.81   1.36   1.03   1.86   1.17   0.66   0.25  -0.46  -1.32  -1.50   0.20
2006     1.03   0.66   0.05   0.40   0.48   1.04   0.35  -0.65  -0.94  -0.05  -0.22   0.14
2007     0.01   0.04  -0.36   0.16  -0.10   0.09   0.78   0.50  -0.36  -1.45  -1.08  -0.58
2008    -1.00  -0.77  -0.71  -1.52  -1.37  -1.34  -1.67  -1.70  -1.55  -1.76  -1.25  -0.87
2009    -1.40  -1.55  -1.59  -1.65  -0.88  -0.31  -0.53   0.09   0.52   0.27  -0.40   0.08
2010     0.83   0.82   0.44   0.78   0.62  -0.22  -1.05  -1.27  -1.61  -1.06  -0.82  -1.21
2011    -0.92  -0.83  -0.69  -0.42  -0.37  -0.69  -1.86  -1.74  -1.79  -1.34  -2.33  -1.79
2012    -1.38  -0.85  -1.05  -0.27  -1.26  -0.87  -1.52  -1.93  -2.21  -0.79  -0.59  -0.48
2013    -0.13  -0.43  -0.63  -0.16   0.08  -0.78  -1.25  -1.04  -0.48  -0.87  -0.11  -0.41
2014     0.30   0.38   0.97   1.13   1.80   0.82   0.70   0.67   1.08   1.49   1.72   2.51
2015     2.45   2.30   2.00   1.44   1.20   1.54   1.84   1.56   1.94   1.47   0.86   1.01
2016     1.53   1.75   2.40   2.62   2.35   2.03   1.25   0.52   0.45   0.56   1.88   1.17
2017     0.77   0.70   0.74   1.12   0.88   0.79   0.10   0.09   0.32   0.05   0.15   0.50
2018     0.70   0.37  -0.05   0.11   0.11  -0.04   0.11   0.18   0.09   0.26  -0.05   0.52
2019     0.66   0.46   0.37   1.07   1.03   1.09   1.03   0.38   0.41  -0.45   0.15   0.97
2020    -0.23  -0.68  -0.82  -0.57   0.09  -0.08  -0.38  -0.28  -0.70  -0.69  -1.12  -0.90
2021    -0.16  -0.54  -1.17  -0.91  -0.94  -1.18  -1.87  -1.12  -1.53  -2.55  -2.52   9.90"""


def arctic_oscillation(year: typing.Optional[typing.Union[range, int]] = None) -> dict:
    """Returns the Arctic Oscillation index."""
    _ao = {year: [*map(float, line.split()[1:])]
           for year, line in zip(range(1950, 2022), _AO.split("\n"))}

    if isinstance(year, range):
        return {year_: _ao[year_] for year_ in year}
    elif isinstance(year, int):
        return _ao[year]
    else:
        return _ao


def north_american_oscillation(year: typing.Optional[typing.Union[range, int]] = None) -> dict:
    """Returns the North American Oscillation index."""
    _nao = {year: [*map(float, line.split()[1:])]
            for year, line in zip(range(1821, 2022), _NAO.split("\n"))}
    if isinstance(year, range):
        return {year_: _nao[year_] for year_ in year}
    elif isinstance(year, int):
        return _nao[year]
    else:
        return _nao


def pacific_decadal_oscillation(year: typing.Optional[typing.Union[range, int]] = None) -> dict:
    """Returns the Pacific Decadal Oscillation index."""
    _pdo = {year: [*map(float, line.split()[1:])]
            for year, line in zip(range(1950, 2022), _PDO.split("\n"))}

    if isinstance(year, range):
        return {year_: _pdo[year_] for year_ in year}
    elif isinstance(year, int):
        return _pdo[year]
    else:
        return _pdo

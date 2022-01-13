# Exercise 1

Calculate the partial widths of the Z and W bosons and the t quark.

## Results

To obtain the following results, `cd` in the current directory and run:

```bash
mg5_aMC mg5_ex1_1.dat
```

This will produce the results in a directory called `output_pp_ttx`, with the
`Cards/param_card.dat` file containing the following values:

```text
#      PDG        Width
DECAY  6   1.491472e+00
#  BR             NDA  ID1    ID2   ...
   1.000000e+00   2    24  5 # 1.491472143911391
#
#      PDG        Width
DECAY  23   2.441755e+00
#  BR             NDA  ID1    ID2   ...
   1.523651e-01   2    3  -3 # 0.37203838150610674
   1.523651e-01   2    1  -1 # 0.37203838150610674
   1.507430e-01   2    5  -5 # 0.36807751028246966
   1.188151e-01   2    4  -4 # 0.29011739100943007
   1.188151e-01   2    2  -2 # 0.29011739100943007
   6.793735e-02   2    16  -16 # 0.16588638484251644
   6.793735e-02   2    14  -14 # 0.16588638484251644
   6.793735e-02   2    12  -12 # 0.16588638484251644
   3.438731e-02   2    13  -13 # 0.08396539434583974
   3.438731e-02   2    11  -11 # 0.08396539434583974
   3.430994e-02   2    15  -15 # 0.08377647844690979
#
#      PDG        Width
DECAY  24   2.047910e+00
#  BR             NDA  ID1    ID2   ...
   3.333605e-01   2    4  -3 # 0.6826922397972374
   3.333605e-01   2    2  -1 # 0.6826922397972374
   1.111202e-01   2    14  -13 # 0.2275640799324124
   1.111202e-01   2    12  -11 # 0.2275640799324124
   1.110388e-01   2    16  -15 # 0.2273974118539395
```

## Reference values

The results can be compared with:

- `W` and `Z`: [PDG _gauge and higgs_ bosons section](https://pdg.lbl.gov/2018/tables/rpp2018-sum-gauge-higgs-bosons.pdf)
- `t`: [PDG _quarks_ section](https://pdg.lbl.gov/2019/tables/rpp2019-sum-quarks.pdf)

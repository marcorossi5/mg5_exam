# Exercise 1c

Verify that the differential cross section of `e+ e- > q qbar g` contains no
collinear divergencies to be regulated.  
The cross section is finite with just a minimum cut on the gluon energy `E_g`.

Plot the cross section as a function of the quark mass and verify that it has a
logarithmic behaviour.

## Results

To obtain the following results, `cd` in the current directory and run:

```bash
mg5_aMC ex2_1c.mg5
```

The script will output the
[cross_section_eex_bbxg_Egmin0.01.txt](cross_section_eex_bbxg_Egmin0.01.txt)
file containing a short description of the runs and the correspondent cross
sections.

Run the following command to plot the cross section as a function of the `b`
quark mass:

```bash
python plot_xsec.py cross_section_eex_bbxg_Egmin0.01.txt
```

This produces the following image:

<div style="text-align:center">
<img src="xsec(mb)_Egmin0.01.png" alt="xsec(mb) Egmin0.01" width="400"/>
</div>

The cross section varies logarithmically with the `b` quark mass: the logarithmic
scale on the x axis shows that a straight line interpolates well the given points.  
Still, the cross section with the gluon cut of `0.01 GeV` is rather unstable, given
the large error bars.
Increasing the cut to `10 GeV` shows a rather smoother behavior:

<div style="text-align:center">
<img src="xsec(mb)_Egmin10.0.png" alt="xsec(mb) Egmin0.01" width="400"/>
</div>

This is reflected also in the decreasing of the percentage error on the fitted
parameters:

|`E_g` cut | `0.01 GeV` | `10 GeV` |
| --- | --- | --- |
| `delta m` | `2.60 %` | `1.44 %` |
| `delta q` | `5.98 %` | `4.44 %` |

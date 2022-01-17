# mg5_aMC@NLO exam

Computational, simulation and machine learning methods in high energy physics
and beyond: Automated computational tools

June 2020 course edition.

## Run the exercises

In order to correctly run the commands in the exercises' READMEs, it is
recommended to add the `mg5amcnlo/bin` and `madanalysis5/bin` ([day3](day3)
exercise) folders to `PATH`.

```bash
cd <mg5 directory>/bin
export MADGRAPH_PATH=$PWD
export PATH=$MADGRAPH_PATH:$PATH
export PATH=$MADGRAPH_PATH/HEPTools/madanalysis5/madanalysis5/bin:$PATH # madanalysis
```

Please, navigate the folders in the present directory and find instructions to
solve the exercises given in [exam_sheet.pdf](exam_sheet.pdf).
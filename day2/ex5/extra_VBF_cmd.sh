# according to HC_NLO_X0 UFO model README
# when generating Higgs in VBF
# set to -1 the parameters 'IRPoleCheckThreshold' and 'PrecisionVirtualAtRunTime'
# in Cards/FKS_params.dat
sed -i '/IRPoleCheckThreshold/{n;s/.*/-1.0d0/}' output_pp_qqH/Cards/FKS_params.dat
sed -i '/PrecisionVirtualAtRunTime/{n;s/.*/-1.0d0/}' output_pp_qqH/Cards/FKS_params.dat
# change the line: tests.append('check_poles') >> pass # tests.append('check_poles')
# in bin/internal/amcatnlo_run_interface.py
sed -i 's/tests.append/pass \# &/' output_pp_qqH/bin/internal/amcatnlo_run_interface.py
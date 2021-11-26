# !/bin/bash

# SBATCH -A ds-m21
# SBATCH -N 1
# SBATCH -n 5
# SBATCH --mem-per-cpu=1024

# load the module
module load hdfs

hdfs dfs -rm -r -f /ds-m21/team_16/outputs
# run streaming job, use absolute paths for all except -input and -output. For them use paths from HDFS which you can find using commands like : hdfs fs -ls /ds-m21
hadoop jar /usr/local/apps/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar  -file /home/ds-m21-user0/HW4_team16/project/Graph-colouring-Map-Reduce/mapper.py -mapper /home/ds-m21-user0/HW4_team16/project/Graph-colouring-Map-Reduce/mapper.py  -file  /home/ds-m21-user0/HW4_team16/project/Graph-colouring-Map-Reduce/reducer.py -reducer /home/ds-m21-user0/HW4_team16/project/Graph-colouring-Map-Reduce/reducer.py  -input /ds-m21/team_16/inputs/* -output /ds-m21/team_16/outputs/
rm -rf part-00000
hdfs dfs -copyToLocal /ds-m21/team_16/outputs/part-00000
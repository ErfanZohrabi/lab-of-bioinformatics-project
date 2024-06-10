less PDB_report.csv

cat PDB_report.csv |tr -d '"' |less

cat PDB_report.csv | tr -d '"' | awk -F "," '{print $1, $2, $3}' |less

#generaly if we use this command, we can exclude empty columns
cat PDB_report.csv | tr -d '"' | awk -F "," '{if ($1!="") {print $1, $2, $3}}' |less

#  remove the initial part because we are not interested.
cat PDB_report.csv | tr -d '"' |tail -n +3 |awk -F "," '{if ($1!="") {print ">" $1 "\n", $2}}' |less

cat PDB_report.csv | tr -d '"' | tail -n +3 | awk -F "," '{if ($1!="") {print ">"$5$3"\n"$2}}' |less

# In this way we can get the chain ID and the sequence. then we can redirect using pdb_seq.fasta
cat PDB_report.csv | tr -d '"' | tail -n +3 | awk -F "," '{if ($1!="") {print ">"$5”_”$3"\n"$2}}' > pdb_seq.fasta

grep “>” pdb_seq.fasta |wc

# Use the command to see only the identifier
cat PDB_report.csv | tr -d '"' |tail -n +3 |awk -F "," '{if ($1!="") {print $5, $3}}' |less

## this is the result :  => 21 21 168


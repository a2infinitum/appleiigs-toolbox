# this cleans up the cdrom text file from antoine, but it depends on consistent spacing
# could replace with something that has a regex for all the tool names
grep  '^\$' textfile.txt | tr "\"" "'" | awk '{
  toolcall = substr($0, 2, 2);
  toolnum = substr($0, 6, 2);
  toolname = substr($0, 10, 15);
  callname = substr($0, 27, 15);
  description = substr($0, 49);
  gsub(/^[ \t]+|[ \t]+$/, "", toolcall);
  gsub(/^[ \t]+|[ \t]+$/, "", toolnum);
  gsub(/^[ \t]+|[ \t]+$/, "", toolname);
  gsub(/^[ \t]+|[ \t]+$/, "", callname);
  print "{ \"toolcall\": \"" toolcall "\", \"toolnum\": \"" toolnum "\", \"toolname\": \"" toolname "\", \"callname\": \"" callname "\", \"description\": \"" description "\" }";
}' | jq -s .

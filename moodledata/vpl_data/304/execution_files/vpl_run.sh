. common_script.sh
check_program python
cat common_script.sh > vpl_execution
echo "python3 $VPL_SUBFILE0" >>vpl_execution
chmod +x vpl_execution

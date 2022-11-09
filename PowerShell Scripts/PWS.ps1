$procs = get-process
$procs2 = get-process
Compare-Object -ReferenceObject $procs -DifferenceObject $procs2 -Property Name

get-process | stop-process -whatif
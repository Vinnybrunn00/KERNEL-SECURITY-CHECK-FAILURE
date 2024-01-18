from subprocess import run, PIPE

def _KERNEL_SECURITY_CHECK_FAILURE_SFC(command: list):
    run(command)

def _KERNEL_SECURITY_CHECK_FAILURE_DISM(command1: list, command2: list):
    run(command1)
    run(command2)
    
COMMANDS_SFC = ['SFC', '/SCANNOW']
COMMANDS_DISM1 = ['DISM', '/Online', '/Cleanup-Image', '/ScanHealth']
COMMANDS_DISM2 = ['DISM', '/Online', '/Cleanup-Image', '/RestoreHealth']
_KERNEL_SECURITY_CHECK_FAILURE_SFC(command=COMMANDS_SFC)
_KERNEL_SECURITY_CHECK_FAILURE_DISM(command1=COMMANDS_DISM1, command2=COMMANDS_DISM2)
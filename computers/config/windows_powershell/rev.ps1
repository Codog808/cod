function rmEnvVar {
	# Directory to remove
	param($directoryToRemove) 

# Get the current user-specific PATH
	$currentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)

# Split the PATH into individual directories
	$pathArray = $currentPath -split ';'

# Remove the unwanted directory
	$updatedPathArray = $pathArray | Where-Object { $_ -ne $directoryToRemove }

# Join the remaining directories back into a single string
	$newPath = $updatedPathArray -join ';'

# Set the updated PATH for the user
	[System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::User)

}

function grabEnvironmentName(){
	$userEnvironmentVariable = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)
	$splitVariables = $userEnvironmentVariable.Split(";")
	$count = 1
	foreach($i in $splitVariables){Write-Host "$count $i"; $count ++}
	$choice = Read-Host "pick a number to choose a PATH"
	$choice = $choice - 1
	$variable = $splitVariables[[int]$choice]
	$newPATHEnv = $splitVariables[0..($choice-1)] + $splitVariables[($choice+1)..$splitVariables.Length]
	return $variable, $choice, $newPATHEnv
}

function test(){
	$pythonEXECUTEpathFORgit = Join-Path $(Get-Location) "github\bin\gset.py"
	$b = "`$b"
	$u = "`$u"
	$r = "`$r"
	$t = "`$t"
	$tr = "`$true"
	$p = @"
param(
	 [Parameter(Mandatory=$tr)]
	 [string]$b,
	 
	 [Parameter(Mandatory=$tr)]
	 [string]$u,

	 [Parameter(Mandatory=$tr)]
	 [string]$r,

	 [Parameter(Mandatory=$tr)]
	 [string]$t
)

$pythonScriptPath = "$pythonEXECUTEpathFORgit"

& python $pythonScriptPath -b $b -u $u -r $r -t $t
"@
	$p | Set-Content -Path ahhh.ps1
}
function main(){
	Write-Warning "Deleting Environment Variables Script.`nCTRL-C to quit..."
	$envVarName, $position, $newPATHEnv = grabEnvironmentName 
	# using list indexes, pick one of the options to delete.
# Ask for confirmation
	$confirmation = Read-Host -Prompt "Are you sure you want to permanently remove the user environment variable '$envVarName'? (yes/no)"

# If user confirms, remove the environment variable
	if ($confirmation -eq 'yes') {
		rmEnvVar $envVarName	
	} else {
	  Write-Output "Operation cancelled."
	}
} # end bracket for main

main 

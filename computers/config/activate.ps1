$pythonEXECUTEpathFORgit = Join-Path $(Get-Location) "github\bin\gset.py"
$b = "`$b"
$u = "`$u"
$r = "`$r"
$t = "`$t"
$tr = "`$true"
$pythonScriptPath = '`$pythonScriptPath'
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
$fa = '`$false'
$m = '`$m'
$msg = '`$msg'
$en = @"
param(
	[Parameter(Mandatory=$fa)]
	[string]$m
) 
$pythonScriptPath = "$pythonEXECUTEpathFORgit"

if ($m -eq null){
$msg = "gfs"
} else {
$msg = $m
}

& python $pythonScriptPath -m $msg
"@

function call_py_from_ps1(){
		param($directory) 
		Write-Host "Calling python script from PS1 Files, initator..."
		if ($directory -eq "github"){
			continue
		}
	}

function main(){
		param ($p, $en)

# Get directories from Python script output
		$directories = & python directories.py -split "`n"

# Get existing PATH
		$existingPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)

# Create PowerShell scripts for Python files
		$path = "github/bin"

# Check and add directories to PATH
		foreach ($directory in $directories) {
			$directoryToAdd = $directory.Trim()
			if ($existingPath -split ';' -notcontains $directoryToAdd) {
				$newPath = "$existingPath;$directoryToAdd"
				[Environment]::SetEnvironmentVariable("Path", $newPath, [EnvironmentVariableTarget]::User)
				Write-Host "Directory added to PATH. You might need to reopen your terminal to see the changes."
				$env:path = $newPath

# Ensure the directory exists
				$path = $directory
				if (-not (Test-Path -Path $path -PathType Container)) {
					New-Item -Path $path -ItemType Directory
				}
				$py_path = "$path"
				foreach ($py in (Get-ChildItem $py_path -Filter *.py)) {
					if (-not ($py.BaseName -eq "gset")){
						$content = "python $py_path\$py"
						$ps1Path = Join-Path $path "$($py.BaseName).ps1"
					} else {
						$content = $p
					}
					$content | Set-Content -Path $ps1Path
				}
				Write-Host "Finished creating ps1 files."
			} else {
				Write-Host "Already in Path: $directoryToAdd"
				echo $existingPath
			} 
		}
} # main ending bracket
main $p $en

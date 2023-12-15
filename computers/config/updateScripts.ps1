$p = @'
param(
    [Parameter(Mandatory=$true)]
    [string]$b,
    
    [Parameter(Mandatory=$true)]
    [string]$u,

    [Parameter(Mandatory=$true)]
    [string]$r,

    [Parameter(Mandatory=$true)]
    [string]$t
)

$pythonScriptPath = "C:\Users\shita\Projects/config/github/bin/gset.py"

& python $pythonScriptPath -b $b -u $u -r $r -t $t
'@


# Ensure the directory exists
$path = "C:\Users\shita\Projects/config\github\bin"
if (-not (Test-Path -Path $path -PathType Container)) {
    New-Item -Path $path -ItemType Directory
}
$py_path = "$path"
foreach ($py in (Get-ChildItem $py_path -Filter *.py)) {
    if (-not ($py.BaseName -eq "gset")){
	    $content = "python $py_path\$py"
	       }
    else {
	$content = $p
    }
    $ps1Path = Join-Path $path "$($py.BaseName).ps1"
    $content | Set-Content -Path $ps1Path
}


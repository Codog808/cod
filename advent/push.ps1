param (
	[Parameter(Mandatory=$true)]
	[string]$commitMessage
	)
function main {
	param ($msg)
	git add .
	git commit -m $msg
	git push -u origin main
	}
main $commitMessage

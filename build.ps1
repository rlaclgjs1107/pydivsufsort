# build.ps1 - PowerShell build script for Windows

Set-Location -Path $PSScriptRoot

git submodule init
git submodule update

if (Test-Path tempbuild) {
    Remove-Item -Recurse -Force tempbuild
}
New-Item -ItemType Directory -Name tempbuild | Out-Null
Set-Location -Path tempbuild

Write-Host "Current location: $(Get-Location)"
Write-Host "Listing tempbuild contents before cmake:"
Get-ChildItem

cmake -G "MinGW Makefiles" -DBUILD_DIVSUFSORT64=ON -DBUILD_EXAMPLES=OFF -DUSE_OPENMP=ON -DCMAKE_POLICY_VERSION_MINIMUM='3.5' ..\libdivsufsort

cmake --build . --config Release

Set-Location -Path ..

Copy-Item -Path "tempbuild\examples\libdivsufsort64.dll" -Destination "pydivsufsort\" -Force
Copy-Item -Path "tempbuild\examples\libdivsufsort.dll" -Destination "pydivsufsort\" -Force

Remove-Item -Recurse -Force tempbuild
